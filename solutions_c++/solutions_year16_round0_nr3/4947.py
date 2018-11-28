#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<fstream>
using namespace std;
long long a[64];
int idx=1,n,t,j;
ofstream fout("jamcoin.out");
long long power(int x,int pow)
{
    if(pow==0)return (long long)1;
    if(pow==1)return (long long)x;
    if(pow%2)return (long long)x*(long long)power(x,pow-1);
    long long ok=power(x,pow/2);
    return ok*ok;
}
long long two()
{
    long long ret=0;
    for(int i=0;i<n;++i)
    {
        ret+=power(2,i)*a[i];
    }
    for(long long i=2;i<=sqrt(ret);++i)
    {
        if(ret%i==0)return i;
    }
    return 0;
}
long long three()
{
    long long ret=0;
    for(int i=0;i<n;++i)
    {
        ret+=power(3,i)*a[i];
    }
    for(long long i=2;i<=sqrt(ret);++i)
    {
        if(ret%i==0)return i;
    }
    return 0;
}
long long four()
{
    long long ret=0;
    for(int i=0;i<n;++i)
    {
        ret+=power(4,i)*a[i];
    }
    for(long long i=2;i<=sqrt(ret);++i)
    {
        if(ret%i==0)return i;
    }
    return 0;
}
long long five()
{
    long long ret=0;
    for(int i=0;i<n;++i)
    {
        ret+=power(5,i)*a[i];
    }
    for(long long i=2;i<=sqrt(ret);++i)
    {
        if(ret%i==0)return i;
    }
    return 0;
}
long long six()
{
    long long ret=0;
    for(int i=0;i<n;++i)
    {
        ret+=power(6,i)*a[i];
    }
    for(long long i=2;i<=sqrt(ret);++i)
    {
        if(ret%i==0)return i;
    }
    return 0;
}
long long seven()
{
    long long ret=0;
    for(int i=0;i<n;++i)
    {
        ret+=power(7,i)*a[i];
    }
    for(long long i=2;i<=sqrt(ret);++i)
    {
        if(ret%i==0)return i;
    }
    return 0;
}
long long eight()
{
    long long ret=0;
    for(int i=0;i<n;++i)
    {
        ret+=power(8,i)*a[i];
    }
    for(long long i=2;i<=sqrt(ret);++i)
    {
        if(ret%i==0)return i;
    }
    return 0;
}
long long nine()
{
    long long ret=0;
    for(int i=0;i<n;++i)
    {
        ret+=power(9,i)*a[i];
    }
    for(long long i=2;i<=sqrt(ret);++i)
    {
        if(ret%i==0)return i;
    }
    return 0;
}
long long ten()
{
    long long ret=0;
    for(int i=0;i<n;++i)
    {
        ret+=power(10,i)*a[i];
    }
    for(long long i=2;i<=sqrt(ret);++i)
    {
        if(ret%i==0)return i;
    }
    return 0;
}
void solve()
{
    ///cout<<idx<<endl;
    if(j==0)return;
    if(idx==n-1)
    {
        long long tw=two();
        long long th=three();
        long long fo=four();
        long long fi=five();
        long long si=six();
        long long se=seven();
        long long ei=eight();
        long long ni=nine();
        long long te=ten();
        if(tw&&th&&fo&&fi&&si&&se&&ei&&ni&&te)
        {
            for(int i=n-1;i>=0;--i)fout<<a[i];
            fout<<" "<<tw<<" "<<th<<" "<<fo<<" "<<fi<<" "<<si<<" "<<se<<" "<<ei<<" "<<ni<<" "<<te<<"\n";
            --j;
        }
        return;
    }
    for(long long i=0;i<2;++i)
    {
        a[idx]=i;
        ++idx;
        solve();
        --idx;
    }
}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cin>>t;
    cin>>n;
    cin>>j;
    a[0]=1;
    a[n-1]=1;
    fout<<"Case #1:\n";
    solve();
    return 0;
}
