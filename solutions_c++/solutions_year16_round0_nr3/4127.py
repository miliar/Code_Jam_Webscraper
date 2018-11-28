#include<cstdio>
#include<iostream>
#include<cstring>
#include<cmath>
#include<vector>
using namespace std;
long long fac[12][18];
long long check(long long n)
{
    for(long long i=2;i*i<=n;i++)
    if(n%i==0) return i;
    return 0;
}
long long change(long long p,int ix)
{
    long long ret=0;
    for(int i=0;i<=15;i++)
    if(p&(1LL<<i)) ret+=fac[ix][i];
    return ret;
}
int main()
{
    //freopen("B_large.in","r",stdin);
    //freopen("B_large.out","w",stdout);
    freopen("C.out","w",stdout);
    //int T;scanf("%d",&T);
    //int n,j;
    //scanf("%d%d",&n,&j);
    for(int i=2;i<=10;i++)
    {
        fac[i][0]=1;
        for(int j=1;j<=16;j++) fac[i][j]=1LL*fac[i][j-1]*i;
    }
    long long x=1LL<<15;
    int tot=0;
    puts("Case #1:");
    for(int i=1;i<=10000;i+=2)
    {
        long long p=x+i;
        vector<int> ans;
        for(int j=2;j<=10;j++)
        {
            long long q=change(p,j);
            int gg=check(q);
            if(gg) ans.push_back(gg);
            else break;
        }
        if(ans.size()==9)
        {
            cout<<change(p,10);
            for(int j=0;j<ans.size();j++) cout<<" "<<ans[j];
            cout<<endl;
            tot++;
            if(tot==50) break;
        }
    }
    return 0;
}
