#include<stdio.h>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<algorithm>
#include<map>
#include<string>
#include<iostream>
#include<vector>
#include<queue>
#include<stack>
#include<cmath>
#include<ctype.h>
#include<deque>
#include<list>
#include<set>
#define INF 999999999
#define NEG -999999999
#define pi acos(-1.0)
#define LL long long int
#define LU unsigned long long int
#define EPS 1e-9
#define MOD 100000007
#define mem(a) memset(a,0,sizeof(a))

using namespace std;
LL n,m,i,j,k,l,a[1000009],b[1000009],p[1000009],ans,cn,t,x,y,z,mx,mn,s;
char c[1000009],ch;
map<pair<LL,LL>,LL>d;
LL dp(LL pos,LL sum)
{
    pair<LL,LL>pr;
    pr=make_pair(pos,sum);
    if(d[pr]!=0)
    {
        return d[pr];
    }
    if(pos>=n)
    {
        return d[pr]=0;
    }
    if(sum<=a[pos])
    {
        return d[pr]=min(1+dp(pos,sum+sum-1),1+dp(pos+1,sum));
    }
    else
    {
        return d[pr]=dp(pos+1,sum+a[pos]);
    }
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%I64d",&t);
    for(i=1;i<=t;i++)
    {
        d.clear();
        scanf("%I64d %I64d",&m,&n);
        for(j=0;j<n;j++)
        {
            scanf("%I64d",&a[j]);
        }
        sort(a,a+n);
        if(m==1)
        {
            ans=n;
        }
        else
        {
            ans=dp(0,m);
        }
        printf("Case #%I64d: %I64d\n",i,ans);
    }
    return 0;
}
