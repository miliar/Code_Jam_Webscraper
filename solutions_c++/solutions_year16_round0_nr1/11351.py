#include <cstring>
#include <iostream>

int solve(int N);

int main(int argc, char **argv) {
  int T;
  std::cin >> T;

  for (int x = 1; x <= T; ++x) {
    int N;
    std::cin >> N;
    int sol = solve(N);
    std::cout << "Case #" << x << ": ";
    if (sol < 0) {
      std::cout << "INSOMNIA"; 
    } else {
      std::cout << sol;
    }
    std::cout << std::endl;
  }
  
  return 0;
}

bool hasSeenAll(bool seen[10]) {
  for (int i = 0; i < 10; ++i) {
    if (!seen[i]) return false;
  }
  return true;
}

void seeDigits(int n, bool seen[10]) {
  while (n > 0) {
    seen[n%10] = true;
    n /= 10;
  } 
}

int solve(int N) {
  if (N == 0) return -1;
  int magnitude = 1;
  while (N / 10 * 10 == N) {
    N /= 10;
    magnitude *= 10;
  }
  bool seen[10];
  std::memset(seen, false, sizeof seen);
  if (magnitude > 1) seen[0] = true;
  int i = 1;
  for (; !hasSeenAll(seen); ++i) {
    seeDigits(i*N, seen);
  }

  return (i-1)*N*magnitude;
}
