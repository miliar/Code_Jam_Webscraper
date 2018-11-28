#include<iostream>
#include<fstream>
using namespace std;

int min_neg,max_neg,tot_cakes,cases,answer;
string input;

inline void flip(int index)
{
    char ch;
    int i;
    for(i=0;(i<index);i++,index--)
    {
        ch=input[i];
        input[i]=input[index];
        input[index]=ch;

        if(input[index]=='+') input[index]='-';
        else
            input[index]='+';

        if(input[i]=='+') input[i]='-';
        else
            input[i]='+';
    }
     if(i==index)
     {
      if(input[i]=='+') input[i]='-';
        else
            input[i]='+';
     }
    return;
}

inline void process()
{
    bool mode;
    int index;

    if(input[0]=='+') mode=true;
    else
        mode=false;

    do
    {
        if(mode) //Flip till last continuous positive from start
        {
            index=1;
            while((input[index]=='+')&&(index<tot_cakes))
                index++;
            if(index==tot_cakes) return;
            flip(index-1);
            mode=false;
        }
        else
        {
            index=tot_cakes-1;
            while((input[index]=='+')&&(index>=0))
                index--;
            if(index==(-1)) return;
            flip(index);
            mode=true;
        }
        answer++;
    }while(true);
    return;
}

int main()
{
              ifstream fin("B-large.in");
              ofstream fout("B-large.out");

              int i,k;

              //cin>>cases;
              fin>>cases;

              for(k=1;k<=cases;k++)
              {

                  //cin>>input;
                  fin>>input;

                  tot_cakes=input.length();
                  answer=0;
                  process();

                  //cout<<"Case #"<<k<<": "<<answer<<"\n";
                  fout<<"Case #"<<k<<": "<<answer<<"\n";
              }

              fin.close();
              fout.close();
              return 0;
}
