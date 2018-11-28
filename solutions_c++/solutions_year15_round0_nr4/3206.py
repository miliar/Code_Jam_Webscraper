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
		string ans = "GABRIEL";
		int x, r, c;
		scanf("%d %d %d", &x, &r, &c);
		if (r > c)
			swap(r, c);
		if (x == 2) {
			if ((r == 1 && c == 3) || (r == c && (r == 1 || r == 3)))
				ans = "RICHARD";
		} else if (x == 3) {
			if (r ==1 || (r == c && r != 3) || (r ==2 && c == 4))
				ans = "RICHARD";
		} else if (x == 4) {
			if (r == 1 || r == 2 || (r == c && r == 3))
				ans = "RICHARD";
		}
		printf("Case #%d: %s\n", num, ans.c_str());
	}
	return;
}