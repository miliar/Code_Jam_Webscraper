#include<bits/stdc++.h>
using namespace std;

long long power(long long a,long long b)
{
    if(b==1)
        return a;
    if(b==0)
        return 1;
    if(b%2==0)
    {
        long long x=power(a,b/2);
        return x*x;
    }
    else
        return a*power(a,b-1);
}
int main()
{
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        int k,c,s;
        cin>>k>>c>>s;
        long long a=power(k,c);
        long long b=a/s;
        long long d=1;
        cout<<"Case #"<<i<<": ";
        while(d<=a)
        {
            cout<<d<<" ";
            d+=b;
        }
        cout<<"\n";
    }
}
