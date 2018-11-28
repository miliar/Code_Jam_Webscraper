#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>

#define oo 1e9
#define pi 3.1415926536
#define all(x) x.begin(),x.end()
#define sorta(x) sort(all(x))
#define sortam(x,comp) sort(all(x),comp)
#define sortd(x) sort(x.rbegin(),x.rend())
#define pb push_back
#define mp make_pair
#define sf(x) scanf("%d", &x);
#define sfll(x) scanf("%I64d", &x);
#define pr(x) printf("%d ", x);

typedef long long ll;
using namespace std;

int main() {
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	sf(t);
	for(int tc = 1; tc <= t; tc++) {
		int n;
		cin >> n;
		vector<ll>a(n);
		for(int i = 0; i < n; scanf("%I64d", &a[i++]));
		ll y = 0, z = 0, t = 0;
		for(int i = 0; i + 1 < n; i++) {
			if(a[i] > a[i + 1]) y += a[i] - a[i + 1], t = max(t, a[i] - a[i + 1]);
		}

		for(int i = 0; i + 1 < n; i++) {
			z += min(t, a[i]);
		}

		printf("Case #%d: ", tc);
		cout << y << ' ' << z << endl;
	}
	return 0;
}
