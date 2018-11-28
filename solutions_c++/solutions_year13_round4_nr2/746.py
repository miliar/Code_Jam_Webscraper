#include <iostream>

long long power(int n) {
  long long res = 1;
  for (int i = 0; i < n; ++i) {
    res = res * 2;
  }
  return res;
}

int get_lose(long long record, int N) {
  long long res = 1, i;
  //std::cout << record << "," << N << std::endl;
  for (i = 0; record >= res; res = res * 2, ++i);
  return N - i;
}

int get_win(long long record, long long n) {
  int res = 0;
  //std::cout << record << "," << n << std::endl;
  for (long long sum = 0; sum < record; ++res, n = n / 2, sum += n);
  return res;
}

int solve(long long &res1, long long &res2) {
  res1 = res2 = 0;
  int N;
  long long n, P;
  std::cin >> N >> P;
  n = power(N);
  int indepP = get_lose(n - P, N);
  //std::cout << indepP << std::endl;
  if (indepP > 0) {
    res1 = 1;
    for (int i = 0; i < indepP; ++i) {
      res1 = res1 * 2 + 1;
    }
    res1--;
  }
  if (res1 >= n) {
    res1 = n - 1;
  }
  int depP = get_win(n - P, n);
  //std::cout << depP << std::endl;
  res2 = n - power(depP);
  return 0;
}

int main(int argc, char *argv[]) {
  int T;
  long long res1, res2;
  std::cin >> T;
  for (int i = 1; i <= T; ++i) {
    std::cout << "Case #" << i << ": ";
    solve(res1, res2);
    std::cout << res1 << " " << res2 << std::endl;
  }
  return 0;
}
