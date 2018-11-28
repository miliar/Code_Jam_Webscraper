#include <bits/extc++.h>
#include <iostream>

using namespace std;

//#define NDEBUG
#ifdef NDEBUG
#define DEBUG if (false)
#else
#define DEBUG if (true)
#endif
#define WRITE(x) DEBUG { cout << (x) << endl; }
#define WATCH(x) DEBUG { cout << #x << " = " << (x) << endl; }
//#define ALL(x) (x).begin(), (x).end()
//#define FORN(i, a, b) for(typeof(b) i = (a); i < (b); ++i)
//#define FOREACH(i, c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)

typedef long long ll;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int ntc;
	cin >> ntc;
	for(int tc = 0; tc < ntc; tc++){
		int n, x;
		cin >> n >> x;
		vector<int> sz(n);
		for(auto& s : sz) cin >> s;
		sort(sz.begin(), sz.end());
		vector<bool> used(n);
		int sol = 0;
		for(int i = n - 1; i >= 0; i--){
			if(not used[i]){
				sol++;
				used[i] = true;
				for(int j = i - 1; j >= 0; j--){
					if(not used[j] and sz[i] + sz[j] <= x){
						used[j] = true;
						break;
					}
				}
			}
		}
		cout << "Case #" << (tc + 1) << ": " << sol << '\n';
	}
}
