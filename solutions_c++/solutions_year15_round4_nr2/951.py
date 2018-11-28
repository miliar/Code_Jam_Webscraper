//darkstallion's template

#include<bits/stdc++.h>
#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define popb pop_back
#define del erase
#define sz size
#define ins insert
#define FOR(a,b,c) for(int a = b; a < c; a++)
#define FORS(a,b,c) for(int a = b; a <= c; a++)
#define FORN(a,b) for(int a = 0; a < b; a++)
#define FORD(a,b,c) for (int a = b; a >= c; a--)
#define RES(a,b) memset(a,b,sizeof(a))
#define LL long long
#define PII pair<int,int>
#define PLL pair<long long,long long>
#define PDD pair<double,double>
#define PCC pair<char,char>
#define PSS pair<string,string>
#define PI acos(-1)
#define eps 1e-9
using namespace std;

int main()
{
  int t;
  scanf("%d",&t);
  FORN(i,t)
  {
    int n;
    double v,x;
    scanf("%d%lf%lf",&n,&v,&x);
    double r[n],c[n];
    FORN(j,n)
      scanf("%lf%lf",&r[j],&c[j]);
    if (n == 1)
    {
      if (c[0] != x)
        printf("Case #%d: IMPOSSIBLE\n",i+1);
      else
        printf("Case #%d: %.6lf\n",i+1,v/r[0]);
    }
    else if (n == 2)
    {
      if (c[0] == c[1])
      {
        if (c[0] != x)
          printf("Case #%d: IMPOSSIBLE\n",i+1);
        else
          printf("Case #%d: %.6lf\n",i+1,v/(r[0]+r[1]));
      }
      else
      {
        if (((x > c[0]) && (x > c[1])) || ((x < c[0]) && (x < c[1])))
          printf("Case #%d: IMPOSSIBLE\n",i+1);
        else
        {
          double v0 = (v*x-v*c[1])/(c[0]-c[1]);
          printf("Case #%d: %.6lf\n",i+1,max(v0/r[0],(v-v0)/r[1]));
        }
      }
    }
  }
}