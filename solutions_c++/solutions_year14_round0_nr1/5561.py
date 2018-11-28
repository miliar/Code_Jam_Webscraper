#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REV(i,b,a) for(int i=(a);i>=(b);i--)
#define mp make_pair
#define pb push_back
#define oo (1<<30)
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define mem(s,v) memset(s,v,sizeof(s))
#define ppc(x) __builtin_popcount((x))
#define iter(it,s) for(__typeof(s.begin())it = s.begin();it!=s.end();it++)

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<double> vd;
typedef vector<string> vs;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };

int main() {
#ifndef ONLINE_JUDGE
  freopen("test.in", "rt", stdin);
  freopen("ans.txt", "wt", stdout);
#endif
  int t;
  scanf("%d", &t);
  FOR (cs , 1 , t + 1)
  {
    int a, b;
    vector<vi> v1(4, vi(4)), v2(4, vi(4));
    scanf("%d", &a);
    FOR (i , 0 , 4)
      FOR (j , 0 , 4)
        scanf("%d", &v1[i][j]);
    scanf("%d", &b);
    FOR (i , 0 , 4)
      FOR (j , 0 , 4)
        scanf("%d", &v2[i][j]);
    a--, b--;
    int c = 0, res = -1;
    FOR (i , 0 , 4)
    {
      c += (count(all(v2[b]), v1[a][i]));
      if (c && res == -1)
        res = v1[a][i];
    }
    if (c == 0) {
      printf("Case #%d: Volunteer cheated!\n", cs);
    }
    if (c == 1) {
      printf ("Case #%d: %d\n", cs , res);
    }
    if (c > 1) {
      printf("Case #%d: Bad magician!\n", cs);
    }
  }
  return 0;
}
