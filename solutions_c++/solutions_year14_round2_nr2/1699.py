#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <vector>
#include <queue>
#include <string>
#include <iostream>
#include <algorithm>
#include <climits>
#include <cmath>
#include <unordered_map>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
int ri() { int a; scanf( "%d", &a ); return a; }
char sbuf[100005];
string rs() { scanf( "%s", sbuf ); return sbuf; }

/*-------------------------------------------------------*/



int main() {
	freopen("C:\\Users\\Administrator\\Desktop\\B-small-attempt0.in","rt",stdin);
	freopen("C:\\Users\\Administrator\\Desktop\\output.txt","wt",stdout);

	int T = ri();
	for (int t = 1; t <= T; ++t) {
		printf("Case #%d: ", t);
		int A = ri(), B = ri(), K = ri();
		int res = 0;
		for (int i = 0; i < A; ++i) {
			for (int j = 0; j < B; ++j) {
				if ((i & j) < K) {
					res++;
				}
			}
		}
		printf("%d\n", res);
	}
	return 0;
}
