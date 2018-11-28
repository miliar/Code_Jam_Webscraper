#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;


typedef long long ll;
int A, B, K;

int solve()
{
	int ans = 0;
	for (int i = 0; i < A; i++)
	for (int j = 0; j < B; j++) {
		int candidate = i&j;
		if (candidate < K) {
			ans++;
		}
	}
	return ans;
}

int main()
{
	int T; cin >> T;
	for (int cas = 1; cas <= T; cas++) {
		cin >> A >> B >> K;
		printf("Case #%i: %i\n", cas, solve());
	}
	return 0;
}
