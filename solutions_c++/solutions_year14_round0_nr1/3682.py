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

map<int,int>b;
int main()
{   
    READ("1.in");
    WRITE("out");
    int t,cas,ans1,ans2;
    cas=0;
    S(t);
    while(t--)
    {
       cas++;
       S(ans1);
       int a[4][4];
       b.clear();
       for(int i=0;i<4;i++)
          for(int j=0;j<4;j++)
             S(a[i][j]);

         for(int k=0;k<4;k++)
            b[a[ans1-1][k]]=1;

         S(ans2);

          for(int i=0;i<4;i++)
           for(int j=0;j<4;j++)
             S(a[i][j]);
         int cnt=0,num;
          for(int k=0;k<4;k++)
            if(b[a[ans2-1][k]])
                 {
                  cnt++;
                  num=a[ans2-1][k];
                 }
      if(cnt==1)
      printf("Case #%d: %d\n",cas,num);
      else if(cnt>1)
      printf("Case #%d: Bad magician!\n",cas);
      else if(cnt==0)
      printf("Case #%d: Volunteer cheated!\n",cas);










    }return 0;

}
