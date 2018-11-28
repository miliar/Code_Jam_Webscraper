#include<bits/stdc++.h>
using namespace std;
long long power(long long x, long long y)
{
    long long temp;
    if( y == 0)
        return 1;
    temp = power(x, y/2);
    if (y%2 == 0)
        return temp*temp;
    else
        return x*temp*temp;
}
string bin(long long n)
{
    long long counter=0,a[1000];
    while(n)
    {
        a[counter]=n%2;
        n/=2;
        counter++;
    }
    string s;
    for(long long i=counter-1;i>=0;i--)
    {
        s+=(a[i]+'0');
    }
    return s;
}
long long base(string s,int k)
{
    long long a[1000],counter=0,cnt=0;
    for(int i=0;s[i]!='\0';i++)
    {
        a[counter]=(s[i]-'0');
        counter++;
    }
    for(int i=0;i<counter;i++)
    {
        cnt+=a[i]*power(k,counter-i-1);
    }
    return cnt;
}
long long a[1000001]={0};
long long prime[1000001]={0};

int main()
{

    long long count=0;
    int qw=1;
        for(long long i=2;i*i<=100000;i++)
    {
        if(a[i]==0)
        {
           // prime[count]=i;
            //count++;


        for(long long j=i;j*i<=1000000;j++)
        {
            a[i*j]=1;

        }
        }
    }
    for(long long i=2;i<=1000000;i++)
    {
        if(a[i]==0)
        {
            prime[count]=i;
            count++;
        }
    }
    freopen("C-small-attempt2.in","r",stdin);
    freopen("output_small.txt","w",stdout);
    long long tc;
    cin>>tc;
    while(tc--)
    {
        long long n,j;
        int qw1=0;
        cin>>n>>j;
        long long x=power(2,n-2);
        string s,t;
        for(long long i=0;i<x;i++)
        {
            s=bin(i);
            long long len=s.length();
            t='1';
            for(long long q=0;q<n-2-len;q++)
            {
                t=t+'0';
            }
            for(long long q=0;s[q]!='\0';q++)
            {
                t=t+s[q];
            }
            t=t+'1';
            long long num;
            long long check=0;
            long long div[1000],div_count=0;
            for(long long u=2;u<=10;u++)
            {
                num=base(t,u);
                long long flag=0;
                for(long long y=1;prime[y]*prime[y]<=num&&y<count;y++)
                {
                    if(num%prime[y]==0)
                    {
                        flag=1;
                        div[div_count]=prime[y];
                        div_count++;
                        break;
                    }

                }
                if(flag==0)
                {
                   check=1;
                   break;
                }
            }
            if(check==0)
            {
                if(qw1==0)
                cout<<"Case #"<<qw<<":"<<endl;
                cout<<t<<" ";
                for(long long h=0;h<div_count;h++)
                {
                    cout<<div[h]<<" ";
                }
                cout<<endl;
                j--;
                if(j==0)
                    break;
                qw1++;
            }
        }
        qw++;
    }
}
