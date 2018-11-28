#include <iostream>
#include <cstdio>
#include <climits>
#include <algorithm>
#include <queue>
#include <cstring>
#include <cmath>
#include <vector>
#include <list>
#include <stack>
#include <bitset>
#include <string>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <ctime>

#define ALL(i,n)    for(i = 0; i < (n); i++)
#define FOR(i,a,b)  for(i = (a); i < (b); i++)
#define SET(p)      memset(p,-1,sizeof(p))
#define CLR(p)      memset(p,0,sizeof(p))
#define S(n)	    scanf("%d",&n)
#define P(n)	    printf("%d\n",n)
#define Sl(n)	    scanf("%lld",&n)
#define Pl(n)	    printf("%lld\n",n)
#define Sf(n)       scanf("%lf",&n)
#define Ss(n)       scanf("%s",n)
#define LL long long
#define ULL unsigned long long
#define pb push_back
using namespace std;

int key[205],type[20];
int dp[1<<20];
vector<int> vc[20];

int func(int msk,int n)
{
    if(msk==(1<<n)-1)
    {
        dp[msk]=100;
        return dp[msk];
    }

    if(dp[msk]!=0)
        return dp[msk];

    int i,j;
    dp[msk]=-1;

    for(i=0;i<n;i++)
    {
        if(!(msk&(1<<i)) && key[type[i]])
        {
            key[type[i]]--;
            for(j=0;j<vc[i].size();j++)
                key[vc[i][j]]++;

            func(msk|(1<<i),n);

            key[type[i]]++;
            for(j=0;j<vc[i].size();j++)
                key[vc[i][j]]--;

            if(dp[msk|(1<<i)]>=0)
            {
                dp[msk]=i;
                break;
            }
        }
    }

    return dp[msk];
}

void print(int msk,int n)
{
    if(msk==(1<<n)-1)
        return;

    printf(" %d",dp[msk]+1);
    print(msk|(1<<dp[msk]),n);
}

int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,n,m,i,j,k,l=0;
    S(t);
    while(t--)
    {
        S(k);  S(n);
        CLR(dp);
        CLR(key);

        for(i=1;i<=k;i++)
        {
            S(j);
            key[j]++;
        }

        for(i=0;i<n;i++)
        {
            S(j);
            type[i]=j;
            S(k);

            vc[i].clear();
            for(j=0;j<k;j++)
            {
                S(m);
                vc[i].pb(m);
            }
        }

        func(0,n);

        l++;
        if(dp[0]==-1)
        {
            printf("Case #%d: IMPOSSIBLE\n",l);
        }
        else
        {
            printf("Case #%d:",l);
            print(0,n);
            printf("\n");
        }

    }
    return 0;
}

