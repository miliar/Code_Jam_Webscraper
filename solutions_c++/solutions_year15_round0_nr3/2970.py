#include <iostream>
#include <cstdio>
#include <cstring>
#include <cassert>

using namespace std;
#define SZ 10000
// 0 = 1, 1 = i, 2 = j, 3 = k, 4 = -1, 5 = -i, 6 = -j, 7 = -k
char m[8][8] = {
  { 0, 1, 2, 3, 4, 5, 6, 7},
  { 1, 4, 3, 6, 5, 0, 7, 2},
  { 2, 7, 4, 1, 6, 3, 0, 5},
  { 3, 2, 5, 4, 7, 6, 1, 0},
  { 4, 5, 6, 7, 0, 1, 2, 3},
  { 5, 0, 7, 2, 1, 4, 3, 6},
  { 6, 3, 0, 5, 2, 7, 4, 1},
  { 7, 6, 1, 0, 3, 2, 5, 4}
};

const char *solve(long l, long x, char *input) {
  char *c = &input[l];
  for (int i = 1; i < x; i++) {
    strncpy(c, input, l);
    c += l;
  }

  int ia[SZ];
  int ka[SZ];
  int numi = 0, numk = 0;

  int L = l * x;
  for (int i = 0; i < L; i++) {
    input[i] = input[i] - 'h';
    assert(input[i] >= 1 and input[i] <= 3);
  }

  int ires = 0;
  for (int i = 0; i < L - 2; i++) {
    ires = m[ires][input[i]];
    if (ires == 1) {
      int jres = 0;
      for (int j = i + 1; j < L - 1; j++) {
	jres = m[jres][input[j]];
	if (jres == 2) {
	  int kres = 0;
	  for (int k = j + 1; k < L; k++) {
	    kres = m[kres][input[k]];
	  }
	  if (kres == 3) return "YES";
	}
      }
    }
  }
  return "NO";
}

int main(int argc, char *argv[]) {
  int T;
  cin >> T;

  for (int t = 1; t <= T; t++) {
    long l, x;
    cin >> l >> x;
    char input[SZ];
    scanf("\n%s", input);
    cout << "Case #" << t << ": " << solve(l, x, input) << endl;
  }
}

