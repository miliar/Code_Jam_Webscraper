#include<iostream>
#include<string>
#include<fstream>
using namespace std;
 ifstream fin;

    ofstream fout;
int top=-1,co,h,l,temp,count=0;
char a[100];//={'\0','\0','\0','\0','\0','\0','\0','\0','\0','\0'};
void push(char n)
{

    top++;
    a[top]=n;
  //  cout<<a[top];
}

void check()
{
   co=0;
  // cout<<"inside";

    int j=99;

    for(j=99;j>=0;j--){
        if(a[j]=='+' || a[j]=='-')
           // j--;
           break;
        //cout<<j;
    }
//cout<<"\nj="<<j;
 for(int i=0;i<l;i++)
        {
            if(a[i]=='+')
                co++;
        }

        if(co==l){
                if(temp<1)
                fout<<"Case #"<<++count<<": "<<"0";
               else{
        fout<<"Case #"<<++count<<": "<<temp;
        h=1;}
        }
        else if (h!=1){
        co=0;//temp++;
    for(int i=0;i<l;i++)
        {
            if(a[i]=='-')
                co++;
        }

        if(co==l)
        {
            temp++;
            fout<<"Case #"<<++count<<": "<<temp;
        }
        else
          {
             // temp--;
                if(a[j]=='-')
{
     temp++;
     //cout<<"temp="<<temp;
    while(a[j]!='+')
    {
      // co++;

        a[j]='+';
        j--;
    }
     //cout<<"check of -";
check();
}

else if (a[j]=='+')
{
    temp++;
    //cout<<"temp="<<temp;

    while(a[j]!='-')
    {

        a[j]='-';
        j--;
    }
   // cout<<"check of +";
    check();
}


          }
        }


}
int main()
{
    fin.open("input.in");

    fout.open("output.txt");
    int t;
    fin>>t;
    for(int q=0;q<t;q++)
    {
 for(int p=0;p<100;p++){
     a[p]='\0';

    }

    string  s;
    //cout<<"\n";
    fin>>s;
    //cout<<"\n";
    l=s.length();
    //cout<<s;
     for(int i=l-1;i>=0;i--)
       push(s[i]);
       temp=0;
       h=0;
       top=-1;
       check();

        if(q<t-1)
       fout<<"\n";
    }
    return 0;
}
