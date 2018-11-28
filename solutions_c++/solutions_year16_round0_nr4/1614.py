#include <cstdint>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

uint8_t sol[101][101];

void solve(uint32_t k, uint32_t c, uint32_t s) {
  // k == s
  cout << "1";

  for(uint32_t i = 1; i < k; ++i)
    cout << " " << i+1;
}

int main() {
  uint32_t cases, k, c, s;

  memset(sol, 0xFF, sizeof(sol));

  cin >> cases;

  for(uint32_t i = 0; i < cases; ++i) {
    cin >> k >> c >> s;

    cout << "Case #" << i+1 << ": ";

    solve(k, c, s);

    cout << std::endl;
  }

  return 0;
}
