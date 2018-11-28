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

const LL INF = (LLONG_MAX / 8LL);


double res;
vector<LL> x, y, bt;
LL b, s, g;
int k;

void func(LL h){
	for(int j = 0; j < k; ++j){
		y[j] += h - x[j];
		s += h - x[j];
		x[j] = h;
	}
	
	while(x[k] == h){
		++k;
	}

	double get = s;
	for(int j = 0; j <= b - s && j < k; ++j){
		res = max(res, 36.0 * get / (k - j) - (s + j));
		get -= y[k - j - 1];
	}
	g = h;
}


double solve(){
	int n;
	scanf("%lld%d", &b, &n);
	x.assign(38, 0);
	y.assign(38, 0);
	bt.clear();
	x[37] = INF;
	for(int i = 0; i < n; ++i){
		scanf("%lld", &x[i]);
		bt.push_back(x[i]);
		if(x[i] != 1){ bt.push_back(x[i] - 1); }
		if(x[i] > 2){ bt.push_back(x[i] - 2); }
	}
	bt.push_back(INF);
	sort(ALL(x));
	sort(ALL(bt));
	bt.erase(unique(ALL(bt)), bt.end());

	res = 0.0;
	g = x[0];
	k = 0;
	while(x[k] == g){ ++k; }
	s = 0;
	for(int i = 0; i < bt.size() && b >= s; ++i){
		if(bt[i] <= g){ continue; }
		LL h = min(bt[i], (b - s) / k + g);
		if(h <= g){ break; }
		
		for(LL j = max(g + 1, h - 40); j <= h; ++j){
			func(j);
		}
	}
	
	return res;
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
