#include <bits/stdc++.h>

using namespace std;

long long int getdigits(long long int n, long long int c, bool arr[10])
{
    while(n>0)
    {
        long long int temp=n%10;
        if(!arr[temp])
        {
            arr[temp]=true;
            c++;
        }
        n/=10;
    }
    return c;
}

long long int func(long long int n)
{
    long long int c=0;
    bool arr[10]={false};
    long long int i=1;
    while(c!=10)
    {
        c=getdigits(n*i,c,arr);
        if(c==10)
            return n*i;
        i++;
    }
}

int main()
{
    fstream f,f2;
    f.open("A-large.in",ios::in);
    f2.open("A-large.out",ios::out);
    long long int t,n;
    f>>t;
    for(long long int i=0;i<t;i++)
    {
        f>>n;
        if(n==0)
            f2<<"Case #"<<i+1<<": INSOMNIA\n";
        else
        {
            f2<<"Case #"<<i+1<<": "<<func(n)<<"\n";
        }
    }
}
