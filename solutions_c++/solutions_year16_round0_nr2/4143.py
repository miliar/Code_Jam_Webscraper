#include <cstdio>
#include <algorithm>
#include <string>
#include <iostream>
using namespace std;

typedef long long lld;
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int T;
	scanf("%d", &T);

	for (int TestCase = 1; TestCase <= T; TestCase++) {
		string str;
		cin >> str;

		int res = 0;
		printf("Case #%d: ", TestCase);
		for (int pos = 1; pos < str.size(); pos++) {
			if (str[pos] != str[pos - 1]) {
				res++;
			}
		}
		if (str.back() == '-')
			res++;
		printf("%d\n", res);
	}
	return 0;
}