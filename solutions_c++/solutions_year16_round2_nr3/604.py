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

typedef pair<string, string> pss;

int ans;
int n;
vector <pss> v;
int tp[100];
void try_all(int l){
	if(l == n){
		bool good = true;
		int cur = 0;
		FOR(i,0,n) if(tp[i] == 1){
			bool f1 = false;
			bool f2 = false;
			FOR(j,0,n) if(tp[j] == 0){
				if(v[j].FR == v[i].FR)
					f1 = true;
				if(v[j].SC == v[i].SC)
					f2 = true;
			}
			if(!f1 || !f2)
				good = false;
			cur++;
		}
		if(good)
			ans = max(ans, cur);
		return;
	}
	tp[l] = 0;
	try_all(l+1);
	tp[l] = 1;
	try_all(l+1);
}

int main(){
	ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	FOR(test,0,T){
		cin >> n;
		v.resize(n);
		FOR(i,0,n)
			cin >> v[i].FR >> v[i].SC;
		
		ans = 0;
		try_all(0);
		cout << "Case #" << test+1 << ": " << ans << endl;
		
	}

	return 0;
}
