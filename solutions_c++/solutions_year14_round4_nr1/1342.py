#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <map>
#include <set>
#include <string.h>

typedef long long ll;
using namespace std;

int solve(int N, int X, int *S) {
	sort(S, S+N);
	int left = 0;
	int right = N-1;
	int r = 0;
	while (left < right) {
		//printf("%d %d  %d %d %d\n", left, right, S[left], S[right], X);
		if (S[left] + S[right] > X) {
			r++;
			right--;
		} else {
			r++;
			right--;
			left++;
		}
	}
	if (left == right)
		r++;
	return r;
}

int main()
{
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		int N, X;
		scanf("%d%d", &N, &X);
		static int S[10010];
		for (int j = 0; j < N; j++) {
			scanf("%d", &S[j]);
		}
		int ans = solve(N, X, S);
		printf("Case #%d: %d\n", i+1, ans);
	}
}
