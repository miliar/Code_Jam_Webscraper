#include <stdio.h>
#include <iostream>
#include <string>
#include <string.h>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
using namespace std;

typedef long long ll;

int N;
int A[1010];

int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		scanf("%d", &N);
		for (int i = 0; i < N; i++)
			scanf("%d", &A[i]);

		int ans1 = 0, ans2 = 0;
		int mx = 0;
		for (int i = 1; i < N; i++) {
			int v = A[i-1]-A[i];
			if (v > 0) {
				ans1 += v;
				mx = max(mx, v);
			}
		}

		for (int i = 0; i < N-1; i++) {
			ans2 += min(mx, A[i]);
		}
		printf("Case #%d: %d %d\n", t, ans1, ans2);
	}
	return 0;
}
