#include <algorithm>
#include <cstring>
#include <iostream>


#define INF 2000000000


int T, A, N, m[100];

int memo[16][2048];


int dfs(int i, int A)
{
  if (i == N)
    return 0;

  if (memo[i][A] >= 0)
    return memo[i][A];

  int r = INF;

  if (A > 1 && A <= m[i])
    r = std::min(dfs(i, A + A - 1) + 1, r);

  if (A > m[i]) {
    r = std::min(dfs(i + 1, A + m[i]), r);
  }

  r = std::min(dfs(i + 1, A) + 1, r);

  return memo[i][A] = r;
}

int main(int argc, char** argv)
{
  std::cin.tie(0);
  std::ios_base::sync_with_stdio(0);

  std::cin >> T;

  for (int t = 1; t <= T; t ++) {
    std::cin >> A >> N;

    for (int i = 0; i < N; i ++)
      std::cin >> m[i];

    std::sort(m, m + N);

    memset(memo, -1, sizeof(memo));

    std::cout << "Case #" << t << ": " << dfs(0, A) << std::endl;
  }
}
