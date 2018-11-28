#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

const int MAXN=40000;

typedef unsigned long long ll;
typedef pair<ll,int> hashele;

const int dir[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

char str[MAXN+10];
int n,m;
ll f[MAXN+10],sum[MAXN+10];
vector<hashele> hash[MAXN+10];
int tableSize;

int insert(ll x)
{
    int pos=x%tableSize;
    for(int i=0; i<(int)hash[pos].size(); ++i)
        if(hash[pos][i].first==x)
            return ++hash[pos][i].second;
    hash[pos].push_back(make_pair(x,1));
    return 1;
}
void getF()
{
    f[0]=1;
    for(int i=1; i<=MAXN; ++i)
        f[i]=f[i-1]*27;
}
void init()
{
    scanf("%s",str+1);
    n=strlen(str+1);
    for(int i=1; i<=n; ++i)
        sum[i]=sum[i-1]+(str[i]-'a'+1)*f[i];
}
int check(int len)
{
    int ret=-1;
    tableSize=n-len+1;
    for(int i=0;i<tableSize;++i)
        hash[i].clear();
    for(int i=len; i<=n; ++i)
        if(insert((sum[i]-sum[i-len])*f[MAXN-(i-len)])>=m)ret=i-len+1;
    return ret;
}
void solve()
{
    int l=0,r=n,mid,ans=-1;
    while(r>l)
    {
        mid=(l+r+1)>>1;
        int tem=check(mid);
        if(tem>=m)l=mid,ans=tem;
        else r=mid-1;
    }
    if(!~ans)puts("none");
    else printf("%d %d\n",l,ans-1);
}
int main()
{
//    freopen("in.txt","r",stdin);
    getF();
    int cas = 1;
    while(scanf("%d",&m),m)
    {
        printf("Case #%d: ", cas + 1);
        init();
        solve();
    }
    return 0;
}