#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define forn(i, a, b) for(int i=(a);i<int(b);i++)
#define PB push_back
#define MP(X,Y) make_pair(X,Y)
#define SZ(X) ((int)(X.size()))
#define ALL(x)   (x).begin(),(x).end()
#define foreach(it, c)  for(typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
#define F first
#define S second
#define CLEAR(A, V) memset(A, V, sizeof(A))

typedef  long long   ll;
typedef vector<int> VI;
typedef vector<string> VS;
typedef pair<int,int> II;
typedef vector<II> VII;

template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}
template<class T> inline T gcd(T a, T b){ return b?gcd(b, a%b):a;}
const double EPS = 1e-9;
const double PI = acos(-1.0);


int n, m, e, s, p;
ll suben[111];
ll bajan[111];
ll estacion[111];

int main () {

	int casos;
	cin >> casos;
	forn(t, 0, casos) {

		memset(suben, 0, sizeof(suben));
		memset(bajan, 0, sizeof(bajan));
		memset(estacion, 0, sizeof(estacion));

		ll realprice = 0;
		cin >> n >> m;
		forn(i, 0, m) {
			cin >> e >> s >> p;
			e--, s--;
			ll l = (s-e);
			realprice += (l*n - (l*(l-1)/2)) * p;

			suben[e] += p;
			bajan[s] += p;
		}

		ll minprice = 0;
		forn(i, 0, n) {

			ll dif = suben[i]-bajan[i];
			if( dif >= 0) {
				estacion[i] += dif;
			} else {
				dif *= -1;

				int j = i;
				while(j>=0 && dif > 0) {
					ll cnt = min(dif, estacion[j]);
					dif -= cnt;
					estacion[j] -= cnt;
					ll l = (i-j);
					minprice += (l*n - (l*(l-1)/2)) * cnt;
					j--;
				}
			}
		}

		cout << "Case #" << t+1 << ": " << realprice - minprice << endl;
	}
	return 0;
}

