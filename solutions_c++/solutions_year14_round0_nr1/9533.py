#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>
#include <stdio.h>
#include <set>
#include <vector>
#include <stack>
#include <climits>
#include <functional>
#include <numeric>
#include <utility>
#include <ctime>
#include <map>
#include <ctype.h>
#include <cmath>
#include <sstream>
#include <cstdlib>
#include <queue>
#include <list>
using namespace std;


#define all(v)  v.begin(), v.end()
#define sz(v)   ((int)(v.size()))
#define vi      vector<int>
#define vii     vector<vector<int> >
#define vc vector<char>
#define vcc     vector<vector<char> >
#define allr(v) v.rbegin(), v.rend()
#define si set<int>
#define msi multiset<int>
#define pii pair<int,int>
#define pb push_back
#define ll long long
#define ull unsigned long long
const int INF = INT_MAX;


int main(int argc, char const *argv[])
{
  freopen("A-small-attempt0.in","r",stdin);
  int t,r,n;
  scanf("%d",&t);

  for (int i = 1; i <= t; ++i)
  {
    scanf("%d",&r);
    set<int> vls;
    for (int x = 1; x <= 4; ++x)
    {
      for (int z = 1; z <= 4; ++z)
      {
        scanf("%d",&n); if(x==r){vls.insert(n);}
      }
    }

    scanf("%d",&r);
    set<int> vls2;
    for (int x = 1; x <= 4; ++x)
    {
      for (int z = 1; z <= 4; ++z)
      {
        scanf("%d",&n); if(x==r){vls2.insert(n);}
      }
    }
    vi ans;
    set_intersection (all(vls),all(vls2),back_inserter(ans));
    if(sz(ans)==1)
      printf("Case #%d: %d\n", i,ans[0]);
    else if(sz(ans)==0)
      printf("Case #%d: Volunteer cheated!\n",i );
    else printf("Case #%d: Bad magician!\n",i );
  }


  return 0;
}