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

LL pp[20][20];
int ans[20];
int N, J, found = 0, i = 0;

inline LL to_base(LL bin, int b){
	LL ans = 0;
	FOR(i,0,N)
		if((bin>>i)&1)
			ans += pp[b][i];
	return ans;
}

inline LL solve(LL bin, LL b){
	LL num = to_base(bin, b);
	for(LL i = 2; i*i <= num; i++)
		if(num%i == 0)
			return i;
	return -1;
}

int main(){
	ios_base::sync_with_stdio(false);

	FOR(i,1,20){
		pp[i][0] = 1;
		pp[i][1] = i;
		FOR(j,2,20)
			pp[i][j] = pp[i][j-1]*pp[i][1];
	}

	cin >> N >> N >> J;
	cout << "Case #1:\n";
	FOR(i,0,1<<(N-2)){
		LL bin = (1ll<<(N-1))+2*i+1;
		bool good = 1;
		FOR(b,2,11)
			if( (ans[b] = solve(bin,b)) == -1){
				good = 0;
				break;
			}
		if(good){
			J--;
			cout << to_base(bin,10) << to_base(bin,10);
			FOR(b,2,11)
				cout << " " << ans[b];
			cout << endl;
		}
		if(!J)
			break;
	}
	cerr << J << endl;

	return 0;
}
