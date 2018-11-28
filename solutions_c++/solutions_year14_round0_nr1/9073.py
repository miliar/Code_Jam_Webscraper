//darkstallion's template

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<list>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<string>
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
    bool card[16];
    RES(card,false);
    int x;
    scanf("%d",&x);
    x--;
    FORN(j,4)
    {
      int z;
      FORN(k,4)
      {
        scanf("%d",&z);
        if (j == x)
          card[z-1] = true;
      }
    }
    scanf("%d",&x);
    x--;
    FORN(j,4)
    {
      int z;
      FORN(k,4)
      {
        scanf("%d",&z);
        if (j == x)
          card[z-1] &= true;
        else
          card[z-1] &= false;
      }
    }
    int ans = 0,ans2;
    FORN(j,16)
      if (card[j])
      {
        ans++;
        ans2 = j;
      }
    if (ans == 0)
      printf("Case #%d: Volunteer cheated!\n",i+1);
    else if (ans == 1)
      printf("Case #%d: %d\n",i+1,ans2+1);
    else
      printf("Case #%d: Bad magician!\n",i+1);
  }
}