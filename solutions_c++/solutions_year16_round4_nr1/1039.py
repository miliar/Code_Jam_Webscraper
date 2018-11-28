#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cassert>
#include <climits>
#include <ctime>
using namespace std;

typedef long long     ll;
typedef double        dbl;

#define X             first
#define Y             second
#define mp            make_pair
#define pb            push_back
#define sz(x)         static_cast<int>((x).size())
#define all(x)        x.begin(),x.end()

#ifdef ROMCHELA
#    define D(x)          cout<<#x<<" = "<<(x)<<endl
#    define Ds()          cout<<"------------"<<endl
#    define eprintf(...)  printf(__VA_ARGS__);
#else
#    define D(c)             static_cast<void>(0)
#    define Ds(x)            static_cast<void>(0)
#    define eprintf(...)     static_cast<void>(0)
#endif

const int maxn = 1e6 + 10;

vector<int> dp[100][100];

vector<int> dfs(int v, int N) {
  if (N == 0) {
    vector<int> res;
    res.pb(v);
    return res;
  }

  if (sz(dp[v][N]))
      return dp[v][N];

  vector<int> vv1 = dfs(v, N - 1);
  vector<int> vv2 = dfs((v + 1) % 3, N - 1);
  
  vector<int> v1 = min(vv1, vv2);
  vector<int> v2 = max(vv1, vv2);

  for (int i = 0; i < sz(v2); i++)
    v1.pb(v2[i]);

  dp[v][N] = v1;
  return v1;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

#ifdef ROMCHELA
  freopen("2.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif

  int T;
  scanf("%d", &T);
  for (int n_test = 1; n_test <= T; n_test++) {
    int N;
    vector<int> cnt;
    scanf("%d", &N);
    int n = 0;
    for (int i = 0; i < 3; i++) {
      int x;
      scanf("%d", &x);
      cnt.pb(x);
      n += x;
    }

    swap(cnt[0], cnt[1]);

    int ppow = 1;
    for (int i = 1; i <= N; i++)
      ppow *= 2;

    vector<int> ans;
    for (int win = 0; win < 3; win++) {
      vector<int> cnt2(3, 0);
      vector<int> result = dfs(win, N);
      
      for (int i = 0; i < sz(result); i++)
        cnt2[result[i]]++;
      if (cnt2[0] == cnt[0] && cnt2[1] == cnt[1] && cnt2[2] == cnt[2]) {
        if (sz(ans) == 0) {
          ans = result;
        } else {
          ans = min(ans, result);
        }
      }

    }



    if (!sz(ans)) {
      printf("Case #%d: IMPOSSIBLE\n", n_test);
    } else {
      printf("Case #%d: ", n_test);
      string w = "PRS";
      for (int i = 0; i < sz(ans); i++) {
        printf("%c", w[ans[i]]);
      }
      puts("");
    }

  }

#ifdef ROMCHELA
  cerr << "\nTIME ELAPSED: " << 1. * clock() / CLOCKS_PER_SEC << " sec\n";
#endif
  return 0;
}
