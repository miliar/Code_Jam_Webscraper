#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <set>
#include <map>

using namespace std;

int test_case_number_ = 0;
#define gout printf("Case #%d: ", ++test_case_number_),cout

void solution() {
  int N;
  cin >> N;

  int answer = -1;
  int mask = 0;
  for (int mul = 1; mul <= 80; ++mul) {
    int X = N * mul;
    if (X == 0) {
      mask |= 1;
    }
    for (; X > 0; X /= 10) {
      mask |= 1 << (X % 10);
    }
    if (mask == (1 << 10) - 1) {
      answer = mul;
      break;
    }
  }

  if (answer == -1) {
    gout << "INSOMNIA\n";
  } else {
    gout << answer * N << endl;
  }
}

int main() {
  int test_cases;
  cin >> test_cases;
  for (int t_case = 0; t_case < test_cases; ++t_case) {
    solution();
  }

  return 0;
}
