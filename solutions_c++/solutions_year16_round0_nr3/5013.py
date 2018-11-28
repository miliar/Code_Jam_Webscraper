#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

int n, j;
int found = 0;

ll convert(string num, int base) {
	ll final = 0;
	ll powb = 1;
	for (int i = num.size() - 1; i >= 0; i--) {
		final += (num[i] - '0') * powb;
		powb *= base;
	}

	return final;
}

ll first_div(ll num) {
	for (ll i = 2; i * i <= num; i++) {
		if (num % i == 0) return i;
	}

	return -1;
}

string cur;
void solve0(int i) {
	if (found == j) return;

	//printf("::%d %d %s\n", i, n, cur.c_str());

	if (i == n - 1) {
		//printf("::%s\n", cur.c_str());

		bool valid = true;
		ll res[10];
		int b = 2;
		while (b <= 10 && valid) {
			//printf("-> %d %lld\n", b, convert(cur, b));
			res[b] = first_div(convert(cur, b));
			//if (cur == "100011") printf("!! %d %d\n", b, res[b]);
			valid &= res[b] != -1;
			if (b == 10) break;
			b++;
		}

		//if (cur == "100011") printf("::%d\n", valid);
			//printf("::%d %s %d\n", i, cur.c_str(), valid);

		if (valid) {
			printf("%s", cur.c_str());
			for (int k = 2; k <= 10; k++)
				printf(" %lld", res[k]);
			printf("\n");

			found++;
		}

		return;
	}

	cur[i] = '0';
	solve0(i + 1);

	cur[i] = '1';
	solve0(i + 1);
}

void solve() {
	found = 0;
	cur = "";
	for (int i = 0; i < n; i++) cur += "0";
	cur[0] = '1';
	cur[n - 1] = '1';

	solve0(1);

	//cur = "1111111111111111";
	//n = 16;
	//solve0(15);

	//cur = "1001";
	//n = 4;
	//solve0(3);

	//cur = "100011";
	//solve0(5);
}

int main() {
	int t;
	scanf("%d", &t);
	for (int ctest = 1; ctest <= t; ctest++) {
		scanf("%d %d", &n, &j);

		printf("Case #%d:\n", ctest);
		solve();
	}
	return 0;
}
