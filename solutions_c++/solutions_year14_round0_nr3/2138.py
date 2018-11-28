#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REV(i,a,b) for(int i=(a);i>=(b);i--)
#define mp make_pair
#define pb push_back
#define oo 1e9
#define eps 1e-9
#define PI 3.14159265358979323846264338327950
#define MAX 2001
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define show(x) cerr<<#x<<" = "<<x<<endl;
#define mem(s,v) memset(s,v,sizeof(s))
#define iter(it,s) for (__typeof(s.begin()) it = s.begin(); it != s.end(); it++)

typedef long long ll;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

int dx[] = { 0, 0, 1, -1, 1, 1, -1, -1 };
int dy[] = { 1, -1, 0, 0, 1, -1, 1, -1 };

int vis[5][5], arr[5][5];
int rows, cols, mines;

bool isValid(int x, int y) {
  return x >= 0 && y >= 0 && x < rows && y < cols;
}

inline bool check(int x, int y) {
  bool ret = true;
  FOR (k , 0 , 8)
    if (isValid(dx[k] + x, dy[k] + y) && arr[dx[k] + x][dy[k] + y])
      ret = false;
  return ret;
}

void BFS(pi src) {
  queue<pi> q;
  q.push(src);
  vis[src.first][src.second] = 1;
  while (sz(q)) {
    pi cur = q.front();
    q.pop();
    FOR (k , 0 , 8)
    {
      int x1 = dx[k] + cur.first, y1 = dy[k] + cur.second;
      if (isValid(x1, y1) && !arr[cur.first][cur.second] && !vis[x1][y1]) {
        vis[x1][y1] = 1;
        if (check(x1, y1))
          q.push(mp(x1, y1));
      }
    }
  }
}

int main() {
  freopen("test.in", "rt", stdin);
  freopen("ret.txt", "wt", stdout);
  int t;
  cin >> t;
  FOR (tt , 1 , t +1)
  {
    scanf("%d%d%d", &rows, &cols, &mines);
    printf("Case #%d:\n", tt);
    int size = rows * cols;
    bool c2 = true;
    FOR (bits , 0 , (1 << (size)))
    {
      if (__builtin_popcount(bits) == mines) {
        memset(arr, 0, sizeof arr);
        FOR (i , 0 , size)
          if ((bits >> i) & 1)
            arr[i / cols][i % cols] = 1;
        int x = -1, y = -1;
        bool ok = false;
        FOR (i , 0 , rows)
        {
          bool c1 = 0;
          FOR (j , 0 , cols)
          {
            if (!arr[i][j] && check(i, j)) {
              memset(vis, 0, sizeof vis);
              x = i, y = j;
              BFS(mp(i, j));
              ok = c1 = true;
              break;
            }
          }
          if (c1)
            break;
        }
        bool c3 = true;
        if (ok) {
          FOR (i , 0 , rows)
          {
            FOR (j , 0 , cols)
            {
              if (!vis[i][j] && !arr[i][j])
                c3 = false;
            }
          }
        } else
          c3 = false;
        if (c3) {
          vs res(rows, string(cols, '3'));
          FOR (i , 0 , rows)
          {
            FOR (j , 0 , cols)
              res[i][j] = arr[i][j] ? '*' : '.';
          }
          res[x][y] = 'c';
          FOR (i , 0 , rows)
            cout << res[i] << endl;
          c2 = false;
          break;
        }
      }
    }
    if (c2) {
      if (size == mines + 1) {
        vs res(rows);
        FOR (i , 0 , rows)
          res[i] = string(cols, '*');
        res[0][0] = 'c';
        FOR (i , 0 , rows)
          cout << res[i] << endl;
      } else
        printf("Impossible\n");
    }
  }
  return 0;
}
