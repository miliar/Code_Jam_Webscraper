#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;
#define ALL(i,n) for(i = 0; i < (n); i++)
#define FOR(i,a,b) for(i = (a); i < (b); i++)
#define SET(p) memset(p,-1,sizeof(p))
#define CLR(p) memset(p,0,sizeof(p))
#define S(n) scanf("%d",&n)
#define P(n) printf("%d\n",n)
#define Sl(n) scanf("%lld",&n)
#define Pl(n) printf("%lld\n",n)
#define Sf(n) scanf("%lf",&n)
#define Ss(n) scanf("%s",n)
#define LL long long
#define ULL unsigned long long
#define pb push_back
#define READ(f) freopen(f,"r",stdin);
#define WRITE(f) freopen(f,"w",stdout);

double a[1010],b[1010];
int main()
{
    READ("3.in");
    WRITE("out");
    int t,n,cas;
    S(t);
    cas=0;
    while(t--)
    {
        cas++;
    S(n);
       for(int i=0;i<n;i++)
       Sf(a[i]);
       for(int i=0;i<n;i++)
       Sf(b[i]);
       sort(a,a+n);
       sort(b,b+n);
       int wcnt=0,dwcnt=0,c=n-1;


       for(int i=n-1;i>=0;i--)
          if(a[i]<=b[c]) c--;
          else wcnt++;

        int r=0;int l=0;

        for(int i=0;i<n;i++)
        (a[l]<b[r])?(l++):(dwcnt++,l++,r++);

        printf("Case #%d: %d %d\n",cas,dwcnt,wcnt);

    }
       return 0;
    }
