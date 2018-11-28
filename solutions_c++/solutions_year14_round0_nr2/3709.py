#include<iostream>
#include<cstdio>

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
{   

    READ("2.in");
    WRITE("out");
    int t,cas;
    double c,f,x,temp1,temp2,ans,s;
    scanf("%d",&t);
    cas=0;
    while(t--)
    {cas++;
    scanf("%lf %lf %lf",&c,&f,&x);
    temp1=x/2.0;s=2.0;temp2=c/s;ans=temp2+x/(s+f);
    double fans=temp1;

    while(ans<fans)
    {
        fans=ans;s=s+f;temp2+=c/s;ans=temp2+x/(s+f);
    }

    printf("Case #%d: %.7lf\n",cas,fans);

}return 0;
}
