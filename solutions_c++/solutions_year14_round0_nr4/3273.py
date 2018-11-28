#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <string>
#include <bitset>
#include <vector>
#include <list>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;

const int N = 1000 + 10;

double a[N], b[N];
int n;
int testCases;

int main()
{
	cin >> testCases;
	for (int index = 1; index <= testCases; ++index) {
		cin >> n;
		for (int i = 0; i < n; ++i) cin >> a[i];
		sort(a, a + n);
//		for (int i = 0; i < n; ++i) cerr << a[i] << ' '; cerr << endl;
		for (int i = 0; i < n; ++i) cin >> b[i];
		sort(b, b + n);
//		for (int i = 0; i < n; ++i) cerr << b[i] << ' '; cerr << endl;
		
		int ans = 0;
		deque<double> que(b, b + n);
		for (int i = 0; i < n; ++i)
			if (a[i] > que.front()) {
				++ans;
				que.pop_front();
			}
			else que.pop_back();
		printf("Case #%d: %d ", index, ans);
		
		ans = 0;
		que = deque<double>(b, b + n);
		for (int i = n - 1; i >= 0; --i)
			if (a[i] < que.back()) que.pop_back();
			else {
				++ans;
				que.pop_front();
			}
		printf("%d\n", ans);
	}
	return 0;
}
