#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;
const int MAXN = 10;

bool visited[MAXN];
int T;
unsigned long long N;

int main(void) {

  //freopen("A-large.in", "r", stdin);
  //freopen("A-large.out", "w", stdout);

  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    cin >> N;

    if (!N) {
      printf("Case #%d: INSOMNIA\n", t);
      continue;
    }

    int seen = 0;
    int n = N;
    int i = 1;

    memset(visited, 0, sizeof(visited));

    while (seen < 10) {
      while (n) {
        seen += !visited[n % 10];
        visited[n % 10] = true;
        n /= 10;
      }
      n = i * N;
      ++i;
    }
    cout << "Case #" << t << ": " << n - N << '\n';
  }

  return 0;
}
