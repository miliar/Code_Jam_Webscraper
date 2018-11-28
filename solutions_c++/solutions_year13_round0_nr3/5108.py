#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<queue>
#include<stack>
#include<map>
#include<vector>
#include<string>
#include<set>
#include<list>
#include<bitset>
#include<sstream>
#include<cstdlib>
#include<ctime>
using namespace std;
#define eps 1e-6
typedef long long ll;
const int inf=0x3f3f3f3f;
const ll linf=ceil(pow(2.0,62));
const double dinf=pow(2.0,62);
const int maxn=10000005;

ll ans[maxn];
ll a[40],b[40];
int num,cnt;
bool test(ll x)
{
    cnt=0;
    while(x>0LL)
    {
        a[++cnt]=x%10LL;
        x/=10LL;
    }
    for(int i=cnt; i>=1; i--)
        b[i]=a[cnt+1-i];
    for(int i=1; i<=cnt; i++)
        if(a[i]!=b[i])return 0;
    return 1;
}

int bs(int l,int r,ll val)
{
    int ret=0;
    while(l<=r)
    {
        //printf("**%d %d\n",l,r);
        int m=(l+r)/2LL;
        //  printf("** %lld %lld\n",ans[m],val);
        if(ans[m]<=val)
        {
            //printf("** %lld\n",m);
            ret=m;
            l=m+1;
        }
        else r=m-1;
    }
    //printf("%lld\n",ret);
    return ret;
}

int main()
{
    freopen("C-large-1.in","r",stdin);
    freopen("out2.out","w",stdout);
    for(int i=1; i<=10000000; i++)
        if(test(((ll)i)*i)&&test((ll)i))ans[++num]=((ll)i)*i;
    int T,ncase=0;
    //for(int i=1; i<=num; i++)
       // if(ans[i]>=100&&ans[i]<=1000)printf("%lld\n",ans[i]);
    //for(int i=1;i<=10;i++)printf("%lld\n",ans[i]);

    scanf("%d",&T);
    while(T--)
    {
        ncase++;
        ll l,r;
        scanf("%I64d%I64d",&l,&r);
        int x=bs(1,num,l-1LL);
        int y=bs(1,num,r);
        //printf("%d %d\n",x,y);
        printf("Case #%d: %d\n",ncase,y-x);
    }
    return 0;
}
