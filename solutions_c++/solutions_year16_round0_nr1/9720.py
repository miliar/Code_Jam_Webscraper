//610 A
#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define _ ios_base::sync_with_stdio(0), cin.tie(0), cin.tie(0), cout.tie(0), cout.precision(15);
#define INF 1000000000
#define FOR(i, a, b) for(int i=int(a); i<int(b); i++)
#define FORC(cont, it) for(decltype((cont).begin()) it=(cont).begin(); it!=(cont).end(); it++)
#define RFORC(cont, it) for(decltype((cont).rbegin()) it=(cont).rbegin(); it!=(cont).rend(); it++)
#define pb push_back
#define mp make_pair
#define eb emplace_back
#define mt make_tuple
#define fi first
#define se second
#define all(x) (x).begin(), (x).end()
using namespace std; typedef long long ll; typedef pair<int, int> ii; typedef vector<int> vi; typedef vector<ii> vii; typedef vector<vi> vvi;
using namespace __gnu_pbds;
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;

int main() { _
	int T;
	cin >> T;
	FOR(t, 1, T+1) {
		cout << "Case #" << t << ": ";
		vi seen(10, 0);
		int numS = 0;
		int n;
		cin >> n;
		bool found = 0;
		for(ll i = 1; i < 10000; i++) {
			ll k = i*n;
			while(k) {
				int d = k%10;
				if (!seen[d]) seen[d] = 1, numS++;
				k/=10;
				if (numS == 10) {
					found = true;
					cout << i*n << endl;
					break;
				}
			}

			if (found) break;
		}
		if (!found) cout << "INSOMNIA" << endl;
	}
}
