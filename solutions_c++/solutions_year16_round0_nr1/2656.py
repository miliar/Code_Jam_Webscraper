#define DEBUG

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

#define PROBLEM_NAME "A"

#define MP(x, y) make_pair(x, y)
#define PB(x) push_back(x)

typedef long long int64;
typedef long double ldouble;
typedef pair<int, int> pii;

int T;

bool seen[10];

void mark(int k) {
  while (k > 0) {
    seen[k % 10] = true;
    k /= 10;
  }
}

bool all() {
  for (int i = 0; i < 10; i++) {
    if (!seen[i]) return false;
  }
  return true;
}

int main() {
#ifdef DEBUG
	freopen(PROBLEM_NAME ".in", "rt", stdin);
	freopen(PROBLEM_NAME ".out", "wt", stdout);
#endif

	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		
		int N;
		scanf("%d", &N);
		
		if (N == 0) {
		  printf("INSOMNIA\n");
		  continue;
		}
		
    memset(seen, 0, sizeof(seen));

		int k = N;
    mark(k);

    while (!all()) {
      k += N;
      mark(k);
    }

    printf("%d", k);
    
		printf("\n");
	}
	return 0;
}