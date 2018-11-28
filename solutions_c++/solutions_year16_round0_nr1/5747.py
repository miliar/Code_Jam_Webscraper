#include <iostream>
#include <algorithm>

using namespace std;

typedef unsigned long long ull;

bool flag [10];


bool hasAllDigits() {
  bool has = true;
  for (int i = 0; i < 10; ++i) {
    has = has && flag[i];
  }
  return has;
}


ull solve(ull n) {

  fill_n(flag, 10, false);
  ull i = 1;
  ull current;
  ull last;
  int d;
  do {
    current =  i * n;
    last =  current;
    i++;

    do {
      d = current % 10ULL;
      flag[d] = true;
      current /= 10ULL;
    } while (current > 0);

  } while (!hasAllDigits());

  return last;
}


int main () {
  

  int T;
  ull N;
  cin >> T;

  for (int i = 1; i <= T; ++i) {
    cin >> N;

    cout <<"Case #"<<i<<": ";

    if (N == 0ULL) {
      cout << "INSOMNIA" << endl;
    } else {
      cout << solve(N) << endl;
    }

  }

  return 0;

}
