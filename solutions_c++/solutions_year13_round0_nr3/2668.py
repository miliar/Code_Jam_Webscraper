#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int t;long long a,b;
long long ans=0;
bool palin(long long x)
{
    int a[101]={0},l=0,f=1;
    while(x) {a[++l]=x%10;x=x/10;}
    for(int i=1;i<=l/2;++i)
    {
        if(a[i]!=a[l-i+1]) {f=0;break;}
    }
    return f;
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.txt","w",stdout);
    cin>>t;
    for(int k=1;k<=t;++k)
    {
        cin>>a>>b;ans=0;
        for(long long i=sqrt(a);i<=sqrt(b);++i)
        {
            if(i*i>=a&&i*i<=b)
            {
                if(palin(i))
                {
                    if(palin(i*i)) ans++;
                }
            }
        }
        cout<<"Case #"<<k<<": "<<ans<<endl;
    }
    return 0;
}
