#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <map>
#include <set>
#include <string>
#include <queue>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

#define foreach(e,x) for(__typeof(x.begin()) e=x.begin(); e!=x.end(); ++e)

const int N = 100000 + 10;

int vis[N];

void solve(int test)
{
	printf("Case #%d: ", test);
	int n, s;
	cin >> n >> s;
	vector<int> vec;
	memset(vis, 0, sizeof vis);
	for(int i = 0; i < n; ++ i) {
		int x;
		scanf("%d", &x);
		vec.push_back(x);
	}
	sort(vec.begin(), vec.end());
	reverse(vec.begin(), vec.end());
	int ptr = 0;
	int ret = 0;
	for(int i = n - 1; i >= 0; -- i) {
		if (vis[i]) continue;
		vis[i] = true;
		++ ret;
		for( ; ptr < n && (vis[ptr] || vec[ptr] + vec[i] > s); ) ++ ptr;
		if (ptr < n) {
			vis[ptr] = true;
		}
	}
	cout << ret << endl;
}

int main()
{
	//freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
	//freopen("A-small-attempt1.in", "r", stdin); freopen("A-small-attempt1.out", "w", stdout);
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
	int testcase;
	scanf("%d", &testcase);
	for(int i = 1; i <= testcase; ++ i) 
		solve(i);
	fclose(stdout);
	return 0;
}
