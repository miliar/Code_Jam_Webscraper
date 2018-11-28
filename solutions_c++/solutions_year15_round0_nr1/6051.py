#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	int t, k;
	scanf("%d", &t);

	string s;

	for(int tc = 1; tc <= t; tc++) {
		cin >> k; cin >> s;
		int arr[k+1], before[k+1];

		arr[0] = s[0] - '0';
		before[0] = 0;

		for(int i = 1; i <= k; i++) {
			arr[i] = s[i] - '0';
			before[i] = before[i-1] + arr[i-1];
		}

		int req = -1;
		for(int i = 0; i <= k; i++) req = max(req, i - before[i]);

		printf("Case #%d: %d\n", tc, req);
	}

	return 0;
}
