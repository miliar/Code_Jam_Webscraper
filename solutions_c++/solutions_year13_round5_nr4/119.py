#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <deque>
#include <complex>
#include <stack>
#include <queue>
#include <cstdio>
#include <cctype>
#include <cstring>
#include <ctime>
#include <iterator>
#include <bitset>
#include <numeric>
#include <list>
#include <iomanip>
using namespace std;


typedef long long LL;
typedef pair<int,int> pii;
typedef pair<LL,LL> pll;

typedef vector<int> vint;
typedef vector<vector<int> > vvint;
typedef vector<long long> vll, vLL;
typedef vector<vector<long long> > vvll, vvLL;

#define VV(T) vector<vector< T > >

template <class T>
void initvv(vector<vector<T> > &v, int a, int b, const T &t = T()){
	v.assign(a, vector<T>(b, t));
}

template <class F, class T>
void convert(const F &f, T &t){
	stringstream ss;
	ss << f;
	ss >> t;
}


#define REP(i,n) for(int i=0;i<int(n);++i)
#define ALL(v) (v).begin(),(v).end()
#define RALL(v) (v).rbegin(),(v).rend()
#define PB push_back
#define ITR ::iterator


#define MOD 1000000009LL
#define EPS 1e-8


double dp[1 << 20];
double cnt[1 << 20];


double solve(){
	string s;
	cin >> s;
	
	int n = s.size();
	int S = 0;
	int em = 0;
	for(int i = 0; i < s.size(); ++i){
		if(s[i] == 'X'){ S |= 1 << i; }
		else{ ++em; }
	}
	
	double rt = pow((double)n, -em);

	fill(dp, dp + (1 << 20), 0.0);
	fill(cnt, cnt + (1 << 20), 0.0);
	cnt[S] = 1;
	
	for(int T = S; T + 1 < (1 << n); ++T){
		if(!cnt[T]){ continue; }
		for(int j = 0; j < n; ++j){
			int k = j;
			int c = n;
			while(T >> k & 1){
				--c;
				if(++k == n){ k = 0; }
			}

			int U = T | 1 << k;
			dp[U] += dp[T] + c * cnt[T];
			cnt[U] += cnt[T];
		}
	}
	return dp[(1 << n) - 1] * rt;
}



int main(){
	cout << fixed << setprecision(10);

	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i){
		fprintf(stderr, "Case %d / %d\n", i, T);
		cout << "Case #" << i << ": " << solve() << endl;
	}
}
