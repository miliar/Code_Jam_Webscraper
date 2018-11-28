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
string s;
int smax, ans, sum;
int main()
{
	int T;
	freopen("E:\\My Code\\GCJ\\2015\\QR\\A-large.in", "r", stdin);
	freopen("E:\\My Code\\GCJ\\2015\\QR\\A-large.out", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d", &smax);
		cin >> s;
		sum = ans = 0;
		for (int i = 0; i <= smax; ++i) {
			if (s[i] > '0' && sum < i) {
				ans += (i-sum);
				sum = i;
			}
			sum += (s[i]-'0');
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
