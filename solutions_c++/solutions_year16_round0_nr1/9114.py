#include<iostream>
#include<fstream>
using namespace std;
int a[10]= {0,1,2,3,4,5,6,7,8,9};
void searchi(int x)
{
    for(int i=0; i<10; i++)
    {
        if(x==a[i])
        {
            a[i]=10;
            return;
        }
    }
}
int check()
{
    for(int i=0; i<10; i++)
    {
        if(a[i]==10)
        {
        }
        else
        {
            return 1;
        }
    }
    return 0;
}
int main()
{
    int T;
    int i,j,N,temp,x,ANS,flag=0,che,N1;
    ifstream myfile;
    myfile.open("A-large.in");
    myfile>>T;
ofstream fout;
fout.open("out.txt",ios::app);


    for(i=0; i<T; i++)
    {
        myfile>>N;
        if(N==0)
        {
            fout<<"CASE #"<<(i+1)<<": "<<"INSOMNIA\n";
        }
        else
        {
            j=1;
            flag=0;
            while(1)
            {
                N1=N*j;
                temp=N1;
                while(N1>0)
                {
                    x=N1%10;
                    searchi(x);
                    che=check();
                    if(che==0)
                    {
                        flag=1;
                        break;
                    }
                    N1=N1/10;
                }
                if(flag==1)
                {
                    fout<<"CASE #"<<(i+1)<<": "<<temp<<"\n";
                    break;
                }
                else
                    j++;
            }
        }
      for(int q=0;q<10;q++)
      {
          a[q]=(q);
      }
    }
    return 0;
}
