#define _CRT_SECURE_NO_WARNINGS

#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <ctime>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <list>
#include <set>
#include <tuple>
#include<iterator>
#include<numeric>
#include <utility>
using namespace std;

typedef long long ll;

const int INF = 1 << 31;
const int N = (int)1e5;
const int MODULO = (int)1e9 + 7;

void task();

int main() {
#ifdef LUNAWYLL
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	task();

#ifdef LUNAWYLL
	cout << "\n---------------------\n";
	cout << clock() * 1000 / CLOCKS_PER_SEC << "ms";
#endif
	return 0;
}

void task() {
	int t;
	scanf("%d", &t);
	for (int num = 1; num <= t; ++num) {
		int cnt;
		scanf("%d ", &cnt);
		string s;
		getline(cin, s);
		int cur = 0, ans = 0;
		for (int i = 0; i <= cnt; ++i) {
			int val = s[i] - '0';
			if (cur < i) {
				ans += i - cur;
				cur = i;
			}
			cur += val;
		}
		printf("Case #%d: %d\n", num, ans);
	}
	return;
}