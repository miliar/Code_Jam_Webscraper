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

int a[105][105];

bool check(int n,int m)
{
    int i,j,k,f;

    for(i=1;i<=n;i++)
    {
        for(j=1;j<=m;j++)
        {
            f=1;
            for(k=1;k<=m;k++)
            {
                if(a[i][k]>a[i][j])
                {
                    f=0;
                    break;
                }
            }

            if(f)
                continue;

            f=1;
            for(k=1;k<=n;k++)
            {
                if(a[k][j]>a[i][j])
                {
                    f=0;
                    break;
                }
            }

            if(f==0)
                return false;
        }
    }

    return true;
}

int main()
{
    int t,n,m,i,j,k,l=0;
    S(t);
    while(t--)
    {
        S(n);  S(m);
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                S(a[i][j]);
            }
        }

        l++;
        if(check(n,m))
        {
            printf("Case #%d: YES\n",l);
        }
        else
        {
            printf("Case #%d: NO\n",l);
        }
    }
    return 0;
}

