#include <bits/stdc++.h>

using namespace std;

#ifdef ACMTUYO
struct RTC{~RTC(){cerr << "Time: " << clock() * 1.0 / CLOCKS_PER_SEC <<" seconds\n";}} runtimecount;
#define DBG(X) cerr << #X << " = " << X << '\n';
#else
struct RTC{};
#define DBG(X)
#endif

#define fast_io() ios_base::sync_with_stdio(false)
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back
#define sz(x) ((int)(x).size())
#define all(c) (c).begin(),(c).end()
#define forn(i, n) for (int i = 0; i < (n); i++)
typedef long long int number;
int swap_bits(int num, int i, int j) {
  if (i == j) return num;
  int bi = (num & (1 << i))?1:0;
  int bj = (num & (1 << j))?1:0;
  // quito los bits
  num = num & (~((1 << i) | (1 << j)));
  //pongo los bits :V
  if (bi)
    num = num | (1 << j);
  if (bj)
    num = num | (1 << i);
  return num;
}
//swapea los i primeros bits y  los invierte
int flip(int num, int i) {
  for (int a = 0, b = i - 1; a < b; a++, b--)
    num = swap_bits(num, a, b);
  for (int j = 0; j < i; j++)
    num = num ^ (1 << j);
  return num;
}
int ans[11][1 << 10];
void calc(int n) {
  memset(ans[n], -1, sizeof(ans[n]));
  ans[n][0] = 0;
  queue<int> q;
  q.push(0);
  while (!q.empty()) {
    int u = q.front();
    q.pop();
    for (int i = 1; i <= n; i++) {
      int v = flip(u, i);
      if (ans[n][v] == -1) {
        ans[n][v] = ans[n][u] + 1;
        q.push(v);
      }
    }
  }
}
char s[110];
int main() {
  for (int i = 1; i <= 10; i++)
    calc(i);
  int casos;
  scanf("%d", &casos);
  for (int caso = 1; caso <= casos; caso++) {
    scanf("%s", s);
    int n = strlen(s);
    int num = 0;
    for (int i = 0; i < n; i++)
      if (s[i] == '-')
        num = num | (1 << i);
    printf("Case #%d: %d\n", caso, ans[n][num]);
  }
  return 0;
}

