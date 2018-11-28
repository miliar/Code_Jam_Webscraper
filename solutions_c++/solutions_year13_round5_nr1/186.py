#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <memory.h>
#include <math.h>
#include <assert.h>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <functional>
#include <vector>
#include <deque>
#include <utility>
#include <bitset>

using namespace std;
typedef long long ll;
const int INF = 987654321;
const ll LINF = (ll)1e15;
typedef long double lf;

int TC, TCC;
int N, B, X[100], A[100];

int main() {
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

    int i, j, k;

	scanf("%d", &TC);
	while(++TCC <= TC) {
		printf("Case #%d: ", TCC);
		
		scanf("%d%d", &B, &N);
		memset(X, 0, sizeof X);
		for(i = 0; i < N; i++) scanf("%d", X+i);
		sort(X, X+37);

		lf ret = 0.0;

		for(int b = 1; b <= 1000; b++) {
			int budget = 0, cnt = 0, sub = 0, mybet = 0;
			for(i = 0; i <= 36; i++) if(X[i] <= b) {
				budget += b - X[i]; 
				mybet += b - X[i]; ++cnt;
				if(budget > B) break;
			}

			if(budget <= B) {
				for(i = 36; i >= 0; i--) if(X[i] <= b) {
					lf v = (lf)36 * mybet / cnt - budget;
					ret = max(ret, v);
					mybet -= b - X[i]; --cnt; ++budget;
					if(budget > B) break;
				}
			}
		}

		printf("%.10Lf\n", ret);
	}

	return 0;
}