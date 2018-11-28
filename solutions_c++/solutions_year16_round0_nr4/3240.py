#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <cmath>
#include <bitset>
using namespace std;

const int N = 110;

long long a[N];

void work()
{
	int k, c, s;
	cin >> k >> c >> s;
	for(int i = 1; i <= k; ++i) {
		a[i] = i;
	}
	for(int j = 1; j < c; ++j) {
		for(int i = 1; i <= k; ++i) {
			a[i] = (a[i]-1)*k + i;
		}
	}
	for(int i = 1; i <= k; ++i) {
		cout << ' ' << a[i];
	}
	cout << endl;
}

int main()
{
	#define LOCAL_
	#ifdef LOCAL
	freopen("0.in", "r", stdin);
	freopen("0.out", "w", stdout);
	#endif

	int n;
	cin >> n;
	for(int i = 1; i <= n; ++i) {
		cout << "Case #" << i << ":";
		work();
	}
	return 0;
}
