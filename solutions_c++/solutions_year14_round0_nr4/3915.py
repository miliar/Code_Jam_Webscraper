/**
  *	@author mzr_c0der
  *	Believe you can and you are halfway there
  */
#include<iostream>
#include<algorithm>
#include<cmath>
#include<climits>
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<deque>
#include<stack>
#include<bitset>
#include<set>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<ctime>
#include<map>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iomanip>
#include<cctype>
#ifdef mzr
//#include<debug.h>
#else
#define db(...) {}
#define dbt(...) {}
#define pprintf(...) {}
#endif

using namespace std;

#define assert(f) {if(!(f)){fprintf(stderr,"Line-->%d  Assertion failed: %s\n",__LINE__,#f);exit(1);}}
#define MOD 	 1000000007LL
#define ABS(x)   ((x)<0?-(x):(x))
#define SQR(x) 	 ((x)*(x))
#define CUBE(x)  ((x)*(x)*(x))
#define pnl      printf("\n")
#define REP(i,n)        for(__typeof(n) i=0;i<(n);i++)
#define FOR(i,a,b)      for(__typeof(b) i=(a);i<(b);++i)
#define FORE(i,a,b)     for(__typeof(b) i=(a);i<=(b);++i)
#define FORD(i,a,b,d)   for(__typeof(b) i=(a);i<(b);i+=(d))
#define FORR(i,n,e)     for(__typeof(n) i=(n);i>=(e);--i)
#define FORRD(i,n,e,d)  for(__typeof(n) i=(n);i>=(e);i-=(d))
#define REP_IT(it,m)    for(it=m.begin();it!=m.end();it++)
#define FORI(it,s) 	    for(__typeof((s).begin()) (it)=(s).begin();(it)!=(s).end();(it)++)
#define FOREACH(it, X)  for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define UNIQUE(v)       sort(ALL(v)),v.erase(unique(ALL(v)),v.end())
#define FILL(a,b)       memset(a,b,sizeof(a))
#define ALL(v)          (v).begin(), (v).end()
#define RALL(v)         (v).rbegin(), (v).rend()
#define checkbit(n,b)   (((n)>>(b))&1)
#define PB push_back
#define MP make_pair
#define XX first
#define YY second
#define lln long long int
#define gc getchar//_unlocked
#define pc putchar//_unlocked
inline void fr(int *a)
{
    char c=0;
    *a=0;
    while(c<33)
        c=getchar();
    while(c>33)
    {
        *a=*a*10+c-'0';
        c=getchar();
    }
}
int main()
{
    freopen("Input.txt","r",stdin);
    freopen("Output.txt","w",stdout);
    int t,n,i,j,b,c,k,l=1,f;
    fr(&t);
    while(t--)
    {
        fr(&n);
        double a[n],g[n],a1[n],g1[n];
        b=c=0;
        REP(i,n)
        {
            cin>>a[i];
            a1[i]=a[i];
        }
        REP(i,n)
        {
            cin>>g[i];
            g1[i]=g[i];
        }
        sort(a,a+n);
        sort(a1,a1+n);
        sort(g,g+n);
        sort(g1,g1+n);
        for(i=0;i<n;i++)
        {
            f=1;
            for(j=0;j<n;j++)
            {
                if(g[j]>a[i])
                {
                    f=0;
                    g[j]=0.0;
                    break;
                }
            }
            if(f==1)
            {
                b++;
            }
        }
        for(i=n-1;i>=0;i--)
        {
            f=1;
            for(j=n-1;j>=0;j--)
            {
                if(a1[i]>g1[j])
                {
                    f=0;
                    g1[j]=2.0;
                    break;
                }
            }
            if(f==0)
            {
                c++;
            }
        }
        printf("Case #%d: %d %d\n",l,c,b);
        l++;
    }
    return 0;
}
