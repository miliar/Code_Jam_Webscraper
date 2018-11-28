#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <list>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <cmath>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cstring>
using namespace std;

#define rep(i,a) for(int i=0; i<a;i++)
#define repd(i,a) for(int i=a - 1; i>= 0;i--)
#define forn(i,a,b) for(int i=a;i<b;i++)
#define ford(i,a,b) for(int i=a; i>=b; i--)
#define repl(i,a) for(long long unsigned i=0; i<((long long unsigned) a);i++)
#define repdl(i,a) for(long long unsigned i=((long long unsigned) a) - 1; i >= 0;i--)
#define fornl(i,a,b) for(int i=((long long unsigned) a);i<((long long unsigned) b);i++)
#define fornld(i,a,b) for(int i=((long long unsigned) a);i>= ((long long unsigned) b);i--)
#define mp make_pair
#define ll long long unsigned
#define sz(x) (x).size()
#define pb push_back
#define endl '\n'
#define vi vector<int>
#define ii pair<int, int>

template <typename T>
  string NumberToString ( T Number ) {
     ostringstream ss;
     ss << Number;
     return ss.str();
  }

ll ex(ll a, ll b) {
	if (b == 0) return 1;
	if (b % 2) return a * ex(a, b - 1);
	ll c = ex(a, b / 2);
	return c * c;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int n;
	cin >> n;
	
	rep(tc, n) {
		ll k;
		cin >> k;
		string in;
		ll d[k + 1];
		cin >> in;
		rep(i, k + 1) {
			d[i] = in[i] - '0';
			//cout << d[i] << " ";
		}
		//cout << endl;
		
		long long int res = 0, c = -1;
		rep(i, k + 1) {
			if (d[i] == 0 && c < i) {
				res++;
				c++;
			}
			c += d[i];
		}
		
		cout << "Case #" << tc + 1 << ": "<< res << endl;
	}
	
	return 0;
}

