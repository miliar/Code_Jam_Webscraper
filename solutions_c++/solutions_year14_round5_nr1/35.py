#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <cmath>
#include <string>
#include <cstring>
using namespace std;
typedef long long i64;

int tr[1001001];
int N, P, Q, R, S;

bool test(i64 alm)
{
	int cnt = 0;
	i64 tmp = alm + 1;
	for(int i = 0; i < N; i++) {
		if(tr[i] > alm) return false;
		if(tmp + tr[i] > alm) {
			++cnt;
			tmp = 0;
		}
		tmp += tr[i];
	}

	return cnt <= 3;
}

int main()
{
	int T;
	scanf("%d", &T);

	for(int t = 0; t++ < T; ) {
		scanf("%d%d%d%d%d", &N, &P, &Q, &R, &S);

		for(int i = 0; i < N; i++) {
			tr[i] = ((i64)i * P + Q) % R + S;
		}
		i64 left=0, right=0;
		i64 sum = 0;
		for(int i=0;i<N;i++) right += tr[i];
		sum = right;

		while(left < right) {
			i64 mid = (left + right) / 2;

			if(test(mid)) {
				right = mid;
			}else left = mid + 1;
		}

		double ret = 1 - (double)left / sum;

		printf("Case #%d: %.12f\n", t, ret);

	}

	return 0;
}
