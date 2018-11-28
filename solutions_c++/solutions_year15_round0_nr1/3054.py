#include <iostream>
#include <fstream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <cstdlib>
#include <cstdio>
#include <string>
#include <cstring>
#include <cassert>
#include <utility>
#include <iomanip>

using namespace std;

int tn;
int n;
string s;
int cur, ans;

int main() {
	//assert(freopen("input.txt","r",stdin));
	//assert(freopen("output.txt","w",stdout));

	scanf("%d\n", &tn);

	for (int test = 1; test <= tn; test++) {
		cin >> n;
		cin >> s;

		cur = 0;
		ans = 0;
		for (int i = 0; i <= n; i++) {
			int curnum = s[i] - '0';
			if (curnum == 0)
				continue;
			if (cur >= i) {
				cur += curnum;
			}
			else {
				ans += i - cur;
				cur += i - cur;
				cur += curnum;
			}
		}

		printf("Case #%d: %d\n", test, ans);
	}

	return 0;
}