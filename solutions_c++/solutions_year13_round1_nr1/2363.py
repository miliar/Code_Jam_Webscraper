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
#include <complex>
using namespace std;
 
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;
typedef complex<int> pnt;
typedef pair<int, int> pii;

#define FOR(i,a,b) for(i=a;i<b;i++) 
#define RA(x) (x).begin(), (x).end()
#define REV(x) reverse(RA(x))
#define FE(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define SZ(x) ((int) (x).size())
#define X first
#define Y second
#define MOD 1000000007
int main(){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	ll t=1, n, tot, a, d, k, lo, hi, i, test;
	cin >> t;
	FOR(test, 0, t){
		cin >> n >> tot;
		a = 2*n+1; d = 4;
		lo = 0, hi = 1LL<<61;
		FOR(i, 0, 100){
			k = lo + (hi-lo) / 2;
			double x = 1.0*k*a + (1.0*k*(k-1)/2)*d;
			if(x > tot)
				hi = k;
			else lo = k;
		}
		printf("Case #%lld: %lld\n", test+1, lo);
	}
}

