#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <map>
#include <set>
#include <iterator>
#include <string>
#include <queue>
#include <cctype>
using namespace std;
#define LL long long
const LL l1 = 1LL;
const int inf = (1<<30);
const int Len = 1000;
int n, m;
int A[Len+5];
int ans;
int main()
{
	//freopen("E:\\My Code\\GCJ\\2015\\QR\\B-large.in", "r", stdin);
	//freopen("E:\\My Code\\GCJ\\2015\\QR\\B-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d", &n);
		m = 0;
		for (int i = 0; i < n; ++i) {
			scanf("%d", &A[i]);
			m = max(m, A[i]);
		}
		ans = inf;
		for (int cur = 1; cur <= m; ++cur) {
			int sum = cur;
			for (int i = 0; i < n; ++i) {
				if (A[i] > cur) {
					sum += (A[i]+cur-1)/cur-1;
				}
			}
			ans = min(ans, sum);
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
