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
    int c,d,v;
    scanf("%d%d%d",&c,&d,&v);
    vector<int> coins;
    FORN(j,d)
    {
      int x;
      scanf("%d",&x);
      coins.pb(x);
    }
    int ans = 0, z = 0;
    LL x = 1LL;
    while (x <= v)
    {
      if ((z < coins.sz()) && (coins[z] <= x))
      {
        x += (LL)coins[z]*(LL)c;
        z++;
      }
      else
      {
        ans++;
        x *= (LL)(c+1);
      }
    }
    printf("Case #%d: %d\n",i+1,ans);
  }
}