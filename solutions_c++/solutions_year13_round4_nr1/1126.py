#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#define MAXN 105
#define MAXM 1000002013
using namespace std;
int N,M;
long long int sum;
struct ST
{
    long long int i,o;
}st[MAXN];
long long int v[MAXN];
int process()
{
    long long int cnt=0,s,m;
    long long int p=0,b;
    memset(v,0,sizeof(v));

    for(int i=1;i<=N;++i)
    {
        v[i]+=st[i].i;
        if(st[i].i) b=i;
        if(st[i].o)
        {
            while(v[b]==0) b--;
            while(st[i].o-v[b]>=0)
            {
                s=((N+(N-(i-b)+1))*(i-b)/2)%MAXM;
                s=(s*v[b])%MAXM;
                cnt=(cnt+s)%MAXM;
                st[i].o-=v[b];
                v[b]=0;
                if(st[i].o==0) break;
                //if(b==1) break;
                //b--;
                while(v[b]==0)
                {
                    if(b==1) break;
                    b--;
                }
            }
            if(st[i].o==0) continue;
            while(v[b]==0) b--;
            s=((N+(N-(i-b)+1))*(i-b)/2)%MAXM;
            s=(s*st[i].o)%MAXM;
            v[b]-=st[i].o;
            cnt=(cnt+s)%MAXM;
        }
    }
    return  (sum-cnt)%MAXM;
}
int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A-small-attempt2.out","w",stdout);
    int Case,T;
    scanf("%d",&Case);
    T=Case;
    long long int s;
    while(Case--)
    {
        scanf("%d%d",&N,&M);
        long long int a,b,m;
        memset(st,0,sizeof(st));
        sum=0;
        for(int i=0;i<M;++i)
        {
            scanf("%lld%lld%lld",&a,&b,&m);
            st[a].i+=m;
            st[b].o+=m;
            s=((N+(N-(b-a)+1))*(b-a)/2)%MAXM;
            s=(s*m)%MAXM;
            sum=(sum+s)%MAXM;
        }
        //cout<<sum<<"\n";
        printf("Case #%d: %d\n",T-Case,process());
    }
    return 0;
}
