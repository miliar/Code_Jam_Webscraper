#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>

using namespace std;

const double pi = acos(-1.0);
const double eps = 1E-7;

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
#define sqr(x) ((x)*(x))
#define Abs(x) ((x) < 0 ? (-(x)) : (x))
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)
#define ME(a) memset((a), 0, sizeof((a)))
#define MM(a, b) memcpy((a), (b), sizeof((a)))
#define FOR(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define REP(i,a,b) for (int (i) = (a); (i) < (b); ++(i))

int n, m;
int Tests;
int v[20];
int main() {
	freopen("C-small-attempt1.in", "r", stdin);
	freopen("C-small-attempt2.out", "w", stdout);
	scanf("%d", &Tests); 
	for (int tts = 0; Tests--; ) {
		scanf("%d%d", &n, &m);
		printf("Case #%d:\n", ++tts);
		int cnt = 0;
		for (int s = 0; s < two(n - 2); ++s) {
			bool flag = true;
			for (int j = 2; j < 11; ++j) {
				long long t = 1, p = j;
				for (int i = 0; i < n - 2; ++i) {
					if (contain(s, i)) t += p;
					p *= j;
				}
				t += p;
				v[j] = 1;
				for (long long k = 2; k * k <= t; ++k)
					if ((t % k) == 0) {
						v[j] = (int)k;
						break;
					}
				if (v[j] == 1) {
					flag = false;
					break;
				}
			}
			if (flag) {
				putchar('1');
				for (int i = n - 3; i >= 0; --i)
					if (contain(s, i)) putchar('1'); else putchar('0');
				putchar('1');
				for (int j = 2; j < 11; ++j)
					printf(" %d", v[j]);
				printf("\n");
				++cnt;
				if (cnt == m) break;
			}
		}
	}
	return 0;
}