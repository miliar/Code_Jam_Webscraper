#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <sstream>
#include <map>
#include <set>

#define REP(i,k,n) for(int i=k;i<n;i++)
#define rep(i,n) for(int i=0;i<n;i++)
#define INF 1<<30
#define pb push_back
#define mp make_pair

using namespace std;
typedef long long ll;
typedef pair<int,int> P;

int main() {
	int t;
	cin >> t;
	
	rep(q, t) {
		ll n;
		cin >> n;

		set<int> st;
		ll ans = -1;
		REP(i, 1, 50000) {
			ll t = n * i;

			while(t) {
				st.insert(t % 10);
				t /= 10;
			}

			if(st.size() == 10) {
				ans = n * i;
				break;
			}
		}


		cout << "Case #" << q + 1 << ": ";
		if(ans == -1) cout << "INSOMNIA" << endl;
		else cout << ans << endl;
	}
	
	return 0;
}
