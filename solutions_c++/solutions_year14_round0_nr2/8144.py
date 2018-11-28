#include <set>
#include <map>
#include <stack>
#include <cmath>
#include <ctime>
#include <queue>
#include <string>
#include <vector>
#include <cstdio>
#include <sstream>
#include <cstring>
#include <climits>
#include <cstring>
#include <iostream>
#include <algorithm>
#define ff first
#define ss second
#define LL long long
#define pb push_back
#define mp make_pair
#define sqr(x) ((x) * (x))
#define PI 3.1415926535897932384626433832795
using namespace std;

int main() {
	
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int t, T = 1;
	cout.unsetf ( ios::floatfield );   
	cout.precision(7);
	cout.setf( ios::fixed, ios::floatfield );
	scanf("%d", &t);
	while(t--) {
		double n, m, k, f = 2, ans = 0;
		cin >> n >> m >> k;
		while(k / f > (n / f) + (k / (f + m))) {
			ans += (n / f);
			f += m;
		}
		ans += (k / f);
		cout << "Case #" << T++ << ": ";
		cout << ans + 0.000000001 << endl;
	}
	return 0;
}

