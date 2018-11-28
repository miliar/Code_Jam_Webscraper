#include <stdio.h>
#include<iostream>
using namespace std;
int check(int a[])
{   int cnt=0;
    for(int i=1;i<10;i++)
        if(a[i]==i)
            cnt++;
    if(cnt==9)
        return 1;
    else
        return 0;
}

int input(long num,int n[10],int &f)
{
    int i=0;
    long cn=num;
   // cout<<"cn"<<cn<<"\n";
    for(;cn!=0;)
    {   if(cn%10==0)
            f=1;
        n[(int)cn%10]=(int)cn%10;
       // cout<<"cn%10 :"<<cn%10<<"\n";
        //cout<<"n[(int)cn%10"<<n[(int)cn%10]<<"\n";
        cn=cn/10;
        i=check(n);
        //cout<<"i"<<i<<"\n";
        if(i==1&&f==1)
        {
            return 1;
            break;
        }

    }
    return 0;
}

int main()
{
    int t,i,j,l;
    cin>>t;
    long  num[t];
    long last[t];
    for(i=0;i<t;i++)
    {   cin>>num[i];
        int f=0,k;
        int a[10]= {0,0,0,0,0,0,0,0,0,0};

        if(num[i]==0)
            last[i]=-1;
        else
        {   last[i]=num[i];
            for(j=2;;j++)
            {
                k=input(last[i],a,f);
               for(int l=0;l<10;l++)
                   cout<<a[l]<<" ";
                cout<<"\n";
                if(k==1)
                    break;
                else
                {
                    last[i]=j*num[i];
                }
            }
        }
    }
    for(i=0;i<t;i++)
        if(last[i]==-1)
            cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<"\n";
        else
            cout<<"Case #"<<i+1<<": "<<last[i]<<"\n";
    return 0;
}

