#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cmath>
#include <iostream>
#include <algorithm>

using namespace std;

int test, n;
string str;

int main() {
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	scanf("%d", &test);
	for (int uu = 1; uu <= test; uu++) {
		int ans = 0;
		cin >> str; n = str.size();
		if (str[0] == '-') --ans;
		for (int j = 0; j < n; j++)
			if (!j || str[j] != str[j - 1])
				if (str[j] == '-') ans += 2;
		printf("Case #%d: %d\n", uu, ans);
	}
}
					
