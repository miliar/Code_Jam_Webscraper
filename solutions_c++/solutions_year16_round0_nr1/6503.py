#include <bits/stdc++.h>
#define mp make_pair
#define vi vector<int>
#define pi pair<int,int>
#define vii vector<pi>
#define ll long long
using namespace std;
int arr[10];
int main() {
#ifndef ONLINE_JUDGE
	freopen("/home/shiva/Learning/1.txt", "r", stdin);
	freopen("/home/shiva/Learning/2.txt", "w", stdout);
#endif
	// ios::sync_with_stdio(false); cin.tie(0);
	ll t, n, temp;
	int i, x = 1;
	scanf("%lld", &t);
	while (t--) {
		memset(arr, 0, sizeof arr);
		scanf("%lld", &n);
		if (n == 0) printf("Case #%d: INSOMNIA\n", x);
		else {
			for (ll inc = n; inc && n; n += inc) {
				for (temp = n; temp; temp /= 10) arr[temp % 10] = 1;
				for (i = 0; i < 10; i++) if (arr[i] == 0) break;
				if (i == 10) { printf("Case #%d: %lld\n", x, n); break;}
			}
		}
		x++;
	}
}