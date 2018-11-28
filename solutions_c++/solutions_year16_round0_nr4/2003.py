#include<bits/stdc++.h>
using namespace std;
vector<long long int> ans;
long long int pow(long long int x,long long int y)
{
    long long int s=1;
    while(y)
    {
        if(y&1) s=s*x;
        x*=x;
        y>>=1;
    }
    return s;
}
long long int get(long long int l,long long int k,long long int i,long long int c)
{
    if(c==-1) return l;
    return get(l+pow(k,c)*i,k,min(i+1,k-1),c-1);
}
long long int get(long long int k,long long int c)
{
    for(long long int i=0;i<k;i+=c)
    {
        ans.push_back(get(0,k,i,c-1));
    }
}
void solve()
{
    long long int k,c,s;
    ans.clear();
    scanf("%lld %lld %lld",&k,&c,&s);
    get(k,c);
    if(ans.size()>s) printf("IMPOSSIBLE\n");
    else{
        for(long long int i=0;i<ans.size();i++) printf("%lld ",ans[i]+1);
        printf("\n");
    }
}
int main()
{
    long long int t;
    freopen("test.inp","r",stdin);
    freopen("test.out","w",stdout);
    scanf("%lld",&t);
    for(long long int i=1;i<=t;i++)
    {
        printf("Case #%lld: ",i);
        solve();
    }
}
