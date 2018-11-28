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

int di[] = { 0, 0, 1, -1, 1, 1, -1, -1 };
int dj[] = { 1, -1, 0, 0, 1, -1, 1, -1 };

bool vis[5][5];
bool grid[5][5];
int n, m, cnt;

inline bool bound(int i, int j) {
  return i >= 0 && j >= 0 && i < n && j < m;
}

inline bool goodCell(int i, int j) {
  int c = 0;
  FOR (k , 0 , 8)
  {
    int ii = di[k] + i, jj = dj[k] + j;
    if (bound(ii, jj) && grid[ii][jj]) {
      c++;
    }
  }
  return c == 0;
}

void dfs(int i, int j) {
  if (vis[i][j])
    return;
  vis[i][j] = 1;
  FOR (k , 0 , 8)
  {
    int ii = di[k] + i, jj = dj[k] + j;
    if (bound(ii, jj) && !grid[i][j]) {
      if (goodCell(ii, jj))
        dfs(ii, jj);
      else
        vis[ii][jj] = 1;
    }
  }
}

int main() {
#ifndef ONLINE_JUDGE
  freopen("test.in", "rt", stdin);
  freopen("ans.txt", "wt", stdout);
#endif
  int t;
  cin >> t;
  FOR (cs , 1 , t +1)
  {
    printf("Case #%d:\n", cs);
    cin >> n >> m >> cnt;
    if (n * m - cnt == 1) {
      FOR (i , 0 , n)
      {
        FOR (j , 0 , m)
        {
          if (!i && !j)
            printf("c");
          else
            printf("*");
        }
        printf("\n");
      }
      continue;
    }
    FOR (msk , 0 , (1 << (n * m)))
    {
      if (ppc(msk) != cnt)
        continue;
      mem(grid, 0);
      FOR (i , 0 , n * m)
        if ((msk >> i) & 1)
          grid[i / m][i % m] = 1;
      int x = -1, y = -1, gd = 0;
      FOR (i , 0 , n)
      {
        FOR (j , 0 , m)
        {
          if (grid[i][j])
            continue;
          // found 0
          if (goodCell(i, j)) {
            mem(vis, 0);
            x = i, y = j;
            dfs(i, j);
            gd = 1;
            goto fin1;
          }
        }
      }
      fin1: ;
      if (gd) {
        FOR (i , 0 , n)
        {
          FOR (j , 0 , m)
          {
            if (!vis[i][j] && !grid[i][j])
              goto fin2;
          }
        }
      } else
        goto fin2;
      // grid traversed
      FOR (i , 0 , n)
      {
        FOR (j , 0 , m)
        {
          if (i == x && j == y)
            printf("c");
          else
            printf("%c", grid[i][j] ? '*' : '.');
        }
        printf("\n");
      }
      goto res;
      fin2: ;
    }
    printf("Impossible\n");
    res: ;
  }
  return 0;
}
