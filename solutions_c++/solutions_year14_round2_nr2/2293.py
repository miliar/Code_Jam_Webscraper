#include<iostream>
#include<cstdio>
#include<map>

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


int main()
{    READ("1.in");
     WRITE("1.out");
    int t,a,b,c,k;
    scanf("%d",&t);
    int cas=0;
    while(t--)
    {   int cnt=0;
    cas++;
        scanf("%d %d %d",&a,&b,&k);
        for(int i=0;i<a;i++)
            for(int j=0;j<b;j++)
            {  if((i&j)<k)
                cnt++;
            }
       printf("Case #%d: %d\n",cas,cnt);



    }
    return 0;
    }

