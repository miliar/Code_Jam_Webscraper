#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

const int N = 1024;
const int INF = 1 << 29;

int psum[N + 1][N]; // N個数字を使って合計がMになる組み合わせに含まれる数字の最小の最大値
int cnt[N];
ll table[N][N];
int P[N];

void build()
{
  for (int i = 0; i < N; i++) for (int j = 0; j < N; j++) psum[i][j] = INF;
  for (int i = 1; i < N; i++){
    psum[1][i] = i;
  }
  for (int a = 1; a < N; a++){
    for (int k = 2; k < N; k++){
      for (int nx = a + 1; nx < N; nx++){
        if (psum[k - 1][nx - a] == INF) continue;
        psum[k][nx] = min(psum[k][nx], max(psum[k - 1][nx - a], a));
      }
    }
  }
  for (int i = 0; i < N; i++){
    for (int j = 0; j < N; j++){
      table[i][j] = i > j ? INF : 0;
    }
  }
  for (int i = 1; i < N; i++){
    for (int j = 1; j < N; j++){
      int ps = psum[i][j];
      if (ps == INF) continue;
      for (int k = ps; k < j; k++){
        table[j][k] = min(table[j][k], (ll)i - 1);
      }
    }
  }
}

inline int in(){int x; scanf("%d", &x); return x;}
int main()
{
  build();
#if 0
  for (int i = 1; i < 9; i++){
    for (int j = 1; j < 9; j++){
      printf("%10d", psum[i][j]);
    }
    puts("");
  }
  puts("---------");
  for (int i = 1; i < 9; i++){
    for (int j = 1; j < 9; j++){
      printf("%10d", table[i][j]);
    }
    puts("");
  }
#endif
  int T = in();
  for (int i = 1; i <= T; i++){
    memset(cnt, 0, sizeof(cnt));
    int D = in();
    for (int j = 0; j < D; j++){
      P[j] = in();
      cnt[P[j]]++;
    }
    int maxp = *max_element(P, P + D);
    ll ans = maxp;
    for (int j = maxp - 1; j > 0; j--){
      ll score = 0;
      for (int d = N - 1; d > 0; d--){
        score += cnt[d] * table[d][j];
      }
      ans = min(ans, score + j);
    }
    printf("Case #%d: %lld\n", i, ans);
  }

  return 0;
}

