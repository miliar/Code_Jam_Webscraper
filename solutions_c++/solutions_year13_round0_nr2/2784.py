#include<vector>
#include<list>
#include<map>
#include<set>
#include<queue>
#include<deque>
#include<stack>
#include<bitset>
#include<sstream>
#include<algorithm>
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
using namespace std;
#define S(n) scanf("%d",&n)
#define SL(n) scanf("%lld",&n)
#define SS(n) scanf("%s",&n)
#define FOR(i,n) for(i=0;i<n;i++)
#define REP(i,j,n) for(i=j;i<n;i++)

int main()
{
    freopen("Codejam_B_in.txt","r",stdin);
    freopen("Codejam_B_out.txt","w",stdout);
    int t,n,m,i,j,cas=1;
    S(t);
    while(t--)
    {
              int a[11][11];
              bool ans=true;
              bool r[11],c[11];
              FOR(i,11)
              r[i]=true,c[i]=true;
              S(n);S(m);
              FOR(i,n)
              FOR(j,m)
              S(a[i][j]);
              FOR(i,n)
              {
                      FOR(j,m)
                      {
                              if(a[i][j]==2)
                              {
                                         c[j]=false;
                                         r[i]=false;
                              }
                      }
              }
              FOR(i,n)   
              {
                         FOR(j,m)
                         {
                                 if(a[i][j]==1 && !r[i] && !c[j])
                                 ans=false;
                         }
              }
              if(!ans)
              printf("Case #%d: NO\n",cas);
              else
              printf("Case #%d: YES\n",cas);
              cas++;
    }
    return 0;
}
