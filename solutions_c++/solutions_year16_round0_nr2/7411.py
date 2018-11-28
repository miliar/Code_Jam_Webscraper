#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <tuple>
#include <vector>
#include <queue>
#include <utility>
#include <algorithm>
#include <cstdlib>
#include <stack>
#include <map>

using namespace std;

#define INF 1987654321
#define MAX 1000000
#define MOD 1000000007
#define CHK 1023

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("large.out", "w", stdout);

	int TC;
	long long int N, tmp;
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		string str;
		cin >> str;
		int ret = 0;
		char ch = str[0];
		for (int i = 1; i < str.size(); i++) {
			if (ch != str[i]) {
				ret++;
				ch = str[i];
			}
		}
		if (str[str.size() - 1] == '-') ret++;

		printf("Case #%d: ", tc);
		printf("%d\n", ret);
	}

	return 0;
}