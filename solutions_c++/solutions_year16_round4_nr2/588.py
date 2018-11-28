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

const int Gmax = 220;

double dp[Gmax][Gmax][Gmax];

int N, K;
double p[Gmax];

int main(){
	ios_base::sync_with_stdio(false);

	int tests;
	cin >> tests;
	FOR(test_no,0,tests){
		cin >> N >> K;
		FOR(i,0,N)
			cin >> p[i];

		dp[0][0][0] = 1;
		FOR(n,1,N+1){
			dp[n][0][0] = 1;
			FOR(k,1,n+1){
				dp[n][k][0] = max(dp[n-1][k-1][0]*(1-p[n-1]), dp[n-1][k][0]);
				dp[n][k][k] = max(dp[n-1][k-1][k-1]*p[n-1], dp[n-1][k][k]);
				FOR(ky,1,k)
					dp[n][k][ky] = max(p[n-1]*dp[n-1][k-1][ky-1]+(1-p[n-1])*dp[n-1][k-1][ky], dp[n-1][k][ky]);
			}
		}
		cout << "Case #" << test_no+1 << ": " << fixed << setprecision(10) << dp[N][K][K/2] << endl;
	}

	
	return 0;
}
