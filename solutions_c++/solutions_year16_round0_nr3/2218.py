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

#define PROBLEM_NAME "C"

#define MP(x, y) make_pair(x, y)
#define PB(x) push_back(x)

typedef long long int64;
typedef long double ldouble;
typedef pair<int, int> pii;

int T;

const int MAXN = 48;
bool bits[MAXN];

int main() {
#ifdef DEBUG
	freopen(PROBLEM_NAME ".in", "rt", stdin);
	freopen(PROBLEM_NAME ".out", "wt", stdout);
#endif

	scanf("%d\n", &T);
	for (int t = 1; t <= T; t++) {
		printf("Case #%d:\n", t);
		
		int N, J;
		scanf("%d %d\n", &N, &J);
		
		for (int k = (1 << (N-1)) + 1; k < (1 << N) && J > 0; k += 2) {
		  cerr << k << endl;
		  int x = k;
		  int l = 0;
		  while (x > 0) {
		    bits[l++] = x % 2;
		    x /= 2;
		  }
		  
		  vector<int64> divs;
		  bool is_prime = false;
		  for (int64 base = 2; base <= 10; base++) {
		  	int64 t = 0;
        for (int i = l - 1; i >= 0; i--) {
		      t = t * base;
		      if (bits[i]) t++;
		    }
// 		    cerr << "T " << t << endl;
		    
		    bool found = false;
		    for (int64 d = 2; d*d <= t; d++) {
		      if (t % d == 0) {
		        found = true;
		        divs.PB(d);
		        break;
		      }
		    }
		    
		    if (!found) {
		      is_prime = true;
		      break;
		    }
		  }
		  
		  if (!is_prime) {
  		  assert(divs.size() == 9);
  		  for (int i = l - 1; i >= 0; i--) {
  		    cout << bits[i];
		    }
  		  for (int p = 0; p < 9; p++) {
  		    cout << " " << divs[p];
  		  }
  		  cout << endl;
  		  J--;
		  }
		}
		
		printf("\n");
	}
	return 0;
}