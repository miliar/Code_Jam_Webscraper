#include<iostream>
using namespace std;

long long x[100000000];
long long an=0;

char s[111];
bool aaa(long long a)
{
    long long n=0;
    long long g=a;
    while(g>0)
    {
        n++;
        s[n]=g%10;
        g/=10;
    }
    for(long long i=1;i<n+1-i;i++)
    {
        if(s[i]!=s[n+1-i])return 0;
    }
    return 1;
}
int main()
{
x[1]=1;
x[2]=4;
an=2;

for(long long i=3;i<=10000000;i++)
{
    if(aaa(i))
    {
        if(aaa(i*i))
        {
            x[++an]=i*i;
        }
    }
}
//for(long long i=1;i<=an;i++)cout<<x[i]<<endl;cout<<"=="<<an<<endl;
long long t;
cin>>t;
for(long long i=1;i<=t;i++)
{
long long a,b;
    cin>>a>>b;
    long long aa,bb;
    for(long long i=1;i<=an;i++)
    {
        if(a<=x[i])
        {
            aa=i;
            break;
        }
    }
    bb=an+1;
    for(long long i=1;i<=an;i++)
    {
        if(b<x[i])
        {
            bb=i;
            break;
        }
    }
cout<<"Case #"<<i<<": "<<(bb-aa)<<endl;
}
return 0;
}
