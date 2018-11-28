// In The Name of God
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <fstream>
#define cin fin
#define cout fout
#define pb push_back
#define popb pop_back
using namespace std;
typedef long long ll;

ifstream fin("A-small-attempt0.in");
ofstream fout("A-small-attempt0.out");

const ll MOD = 1000002013ll;
ll T, n, m, o, e, p, road[150];
bool mark[150];

int main() {
	ios_base::sync_with_stdio(false);
	cin >> T;
	for(int i = 1; i <= T; ++i) {
		cin >> n >> m;
		fill(mark, mark + 150, false);
		fill(road, road + 150, 0);
		ll pool = 0, asl = 0;
		for(int j = 0; j < m; ++j) {
			cin >> o >> e >> p;	
			road[o] += p;
			road[e] -= p;
			asl += (ll) ((n * (n + 1) / 2) - (ll) ( (n - e + o) * (n - e + o + 1) / 2)) * p;
		}
		for(int j = 1; j <= n; ++j)
			road[j] += road[j - 1];
		for(ll j = 1; j <= n;) {
			if(road[j] < road[j - 1]) {
				ll a = j - 1;
				while(road[a] >= road[j - 1] || mark[a])
					a--;
				//cerr << a << endl;
				ll r = 1;
				for(int h = a + 1; h < j; ++h)
					road[h]--;
				//road[j - 1] -= r;
				//road[a] -= r;
				pool += (ll)((n * (n + 1) / 2) - (ll) ((n - j + a + 2) * (n - j + a + 1) / 2)) * (r);	
				//mark[a] = true;
				//mark[j] = true;
				
			}
			else
				++j;
		}
		ll ans = asl - pool;
		cout << "Case #" << i << ": " << ans % MOD << endl;
		//cerr << asl << ' ' << pool << endl;
	}
	//system("pause");
	return 0;
}
