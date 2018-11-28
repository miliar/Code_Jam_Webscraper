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

const int N = 1000 + 10;

int n;
pair<int, int> a[N];

void solve(int test)
{
	printf("Case #%d: ", test);
	cin >> n;
	for(int i = 0; i < n; ++ i) {
		cin >> a[i].first;
		a[i].second = i;
	}
	sort(a, a + n);
	int ret = 0;
	for(int i = 0; i < n; ++ i) {
		int tmp = 0;
		int tot = 0;
		for(int j = i + 1; j < n; ++ j) {
			if (a[i].first < a[j].first) {
				tmp += a[i].second > a[j].second;
				++ tot;
			}
		}
		ret += min(tot - tmp, tmp);
	}
	cout << ret << endl;
}

int main()
{
	//freopen("B-small-attempt0.in", "r", stdin); freopen("B-small-attempt0.out", "w", stdout);
	//freopen("B-small-attempt1.in", "r", stdin); freopen("B-small-attempt1.out", "w", stdout);
	freopen("B-large.in", "r", stdin); freopen("B-large.out", "w", stdout);
	int testcase;
	scanf("%d", &testcase);
	for(int i = 1; i <= testcase; ++ i) 
		solve(i);
	fclose(stdout);
	return 0;
}
