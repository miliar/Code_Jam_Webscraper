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

int e, r, n;
int v[100];
ll ret;

void bt(int i, int d, ll acm) {

	if(i == n-1) {
		ret = max(ret, acm+d*v[i]);
		return;
	}

	for(int j=d ; j>= 0 ; j--) {
		bt(i+1, min(e, d-j+r), acm + j*v[i]);
	}
	return;
}

int main () {

	int casos;
	cin >> casos;
	forn(t, 0, casos) {
		cin >> e >> r >> n;
		forn(i, 0, n) cin >> v[i];

		ret = 0;
		bt(0, e, 0);

		cout << "Case #" << t+1 << ": " << ret << endl;
	}

	return 0;
}



