#include <cstdio>
#include <iostream>
using namespace std;
const int MAXN = 1000+5;
int T, S;
char str[MAXN];
int main() {
//	freopen("put.in", "r", stdin);
	cin>>T;
	for (int cas = 1; cas <= T; cas++) {
		cin>>S>>str;
		int sum = 0, ans = 0;
		for (int i = 0; i <= S; i++) {
			if (sum < i) {
				ans += i-sum;
				sum = i;
			}
			sum += str[i]-'0';
		}
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}
