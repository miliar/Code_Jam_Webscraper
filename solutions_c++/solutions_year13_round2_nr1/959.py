#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
/*#include <hash_map>
using namespace __gnu_cxx;*/
typedef long long ll;
using namespace std;

#define pb push_back
#define mp make_pair
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vector<pii> > adjL;
int oo = (int) 1e9;
const int MX = 109;
ll mot[MX];
ll csz[MX];
int main() {
	std::ios_base::sync_with_stdio(false);

	freopen("A-large.in", "rt", stdin);
	freopen("A-large.txt", "wt", stdout);

	int t;
	cin>>t;
	for (int ii = 0; ii < t; ++ii) {
		cerr<<ii<<endl;
		cout<<"Case #"<<ii+1<<": ";
		ll a, n;
		cin>>a>>n;
		for (int i = 0; i < n; ++i)
			cin>>mot[i];

		sort(mot, mot+n);
		if(a == 1) {
			cout<<n<<endl;
			continue;
		}
		ll curS = a;
		int cnt = 0;
		for (int i = 0; i < n; ++i) {
			while(curS <= mot[i]) {
				curS+=(curS-1);
				++cnt;
			}
			curS+=mot[i];
			csz[i] = cnt;
		}
		ll ans = n;
		for (int i = 0; i < n; ++i) {
			ans = min(n-i-1+csz[i], ans);
		}
		cout<<ans<<endl;
	}
	return 0;
}
