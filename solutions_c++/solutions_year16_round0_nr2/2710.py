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

#define PROBLEM_NAME "B"

#define MP(x, y) make_pair(x, y)
#define PB(x) push_back(x)

typedef long long int64;
typedef long double ldouble;
typedef pair<int, int> pii;

int T;

const int MAXN = 128;
char s[MAXN];

// inline char chg(char c) {
//   if (c == '+') return '-';
//   else return '+';
// }
// 
// void flip(int i) {
//   int p1 = 0, p2 = i;
//   while (p1 < p2) {
//     char t = s[p1];
//     s[p1] = s[p2];
//     s[p2] = t;
//     p1++;
//     p2--;
//   }
//   for (int k = 0; k <= i; k++) {
//     s[k] = chg(s[k]);
//   }
// }

int main() {
#ifdef DEBUG
	freopen(PROBLEM_NAME ".in", "rt", stdin);
	freopen(PROBLEM_NAME ".out", "wt", stdout);
#endif

	scanf("%d\n", &T);
	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		
		int flips = 0;
		
		gets(s);
		int n = strlen(s);
		
		int pp = n-1;
		while (pp >= 0 && s[pp] == '+') {
		  pp--;
		}
		int size = pp+1;
		
		int spans = 0;
		for (int i = 0; i < size; i++) {
		  if (i == 0 || s[i] != s[i-1]) {
		    spans++;
		  }
		}
		
		printf("%d", spans);
// 		
// 		while (true) {
//   		bool done = false;
//       for (int i = n-1; i >= 0; i--) {
//         if (s[i] == '-') {
//           if (s[0] == '+') {
//             int j = i;
//             while (0 <= j && s[j] == '-') j--;
//             // s[j] == +
//             // +--+++...+++----
//             flip(j);
//             // <---flip--->
//             // ---...---++-----
//             flip(i);
//             // <-----flip----->
//             // +++++--+++...+++
//             // ---...---++-----
//             flips += 2;
//           } else {
//             flip(i);
//             flips++;
//           }
//           
//           done = true;
//           break;
//         }
//       }
//       
//       if (!done) break;
//     }
// 		
// 		printf("%d", flips);
		printf("\n");
	}
	return 0;
}