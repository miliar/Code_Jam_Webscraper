#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cfloat>
#include <cmath>
#include <algorithm>
#include <vector>
#include <map>
#include <set>

using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define pb push_back
#define mp make_pair
int gcd(int u, int v) {
return (v != 0)?gcd(v, u%v):u;
}
int main() {
	int tc;
	cin >> tc;
	for (int t = 0; t < tc; t++) {
		int b, n;
		cin >> b >> n;
		set<pair<long long, int>> s;
		vector<long long> bs(b);
		FOR(i, 0, b) {
			cin >> bs[i];
		}
		if (n <= b) {
			cout << "Case #" << t+1 << ": " << n << endl;
		} else {
			long long wenig = 0, viel = 100000000000005ll;
			while (wenig + 1 < viel) {
				long long mid = (viel + wenig) / 2;
				long long sum = 0;
				FOR(i, 0, b) {
					sum += mid / bs[i] + 1;
				}
				if (sum < n) {
					wenig = mid;
				} else {
					viel = mid;
				}
			}
			long long sum = 0;
			vector<int> fertig;
			FOR(i, 0, b) {
				sum += viel / bs[i] + 1;
				if (viel % bs[i] == 0) {
					sum--;
					fertig.pb(i);
				}
			}
			n -= sum;
			cout << "Case #" << t+1 << ": " << fertig[n-1]+1 << endl;
		}
	}
	return 0;
}
