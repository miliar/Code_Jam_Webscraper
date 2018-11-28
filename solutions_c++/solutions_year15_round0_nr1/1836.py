#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<ctime>
#include<algorithm>
#include<iomanip>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<cassert>
#include<bitset>

using namespace std;

const int lim = 1e5;

int main() {
	//freopen("a.out", "w", stdout);
	int TT;
	scanf("%d", &TT);
	for (int s = 1; s <= TT; s++) {
		int n;
		scanf("%d", &n);
		char st[lim];
		scanf("%s", st);
		int cnt = 0, ans = 0;
		for (int i = 0; i <= n; i++) {
			if (cnt < i) {
				ans += i - cnt;
				cnt = i;
			}
			cnt += st[i] - '0';
		}
		printf("Case #%d: %d\n", s, ans);
	}
	return 0;
}

