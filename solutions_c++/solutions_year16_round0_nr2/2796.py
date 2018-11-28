#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <complex>
#include <numeric>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <deque>
#include <queue>
#include <set>
#include <map>

//#include <unordered_map>
//#include <unordered_set>

using namespace std;
#define FOR(i,m,n) for(int i = (m); i < (n); i++)
#define ROF(i,m,n) for(int i = (n)-1; i >= (m); i--)
#define foreach(x,i) for( __typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
typedef long long LL;
typedef long long ll;
typedef unsigned long long uLL;
typedef vector<int> VI;
typedef vector<LL> VLL;
#define SZ(x) ((int)(x).size())
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;
#define FR first
#define SC second
typedef complex<double> point;
#define X first
#define Y second
//#define X real()
//#define Y imag()

template<class T> ostream& operator << (ostream &o, const vector<T> &t){
	o << "[" << SZ(t);
	bool f = false;
	foreach(t,it)
		o << (f++ ? ", " : ": ") << (*it);
	return o << "]";
}

template<class T1, class T2> ostream& operator << (ostream &o, const pair<T1, T2> &p){
	return o << "(" << p.FR << ", " << p.SC << ")";
}

int main(){
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	FOR(cnt,0,T){
		string s;
		int ans = 0;
		cin >> s;
		s = s+"+";
		FOR(i,0,SZ(s)-1)
			if(s[i] != s[i+1])
				ans++;
		cout << "Case #" << cnt+1 << ": " << ans << endl;
	}

	return 0;
}
