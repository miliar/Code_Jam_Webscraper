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

#if __cplusplus >= 201103L
#include <array>
#include <tuple>
#include <initializer_list>
#include <unordered_set>
#include <unordered_map>
#include <forward_list>

#define cauto const auto&
#endif

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


#define MOD 1000000009LL
#define EPS 1e-8


LL solve(){
	LL w, h;
	int b;
	cin >> w >> h >> b;
	vll x0(b + 2), x1, y0, y1;
	x1 = y0 = y1 = x0;
	x0[0] = -1;
	x1[0] = 0;
	x0[1] = w;
	x1[1] = w + 1;
	y0[0] = y0[1] = 0;
	y1[0] = y1[1] = h;
	for(int i = 2; i < b + 2; ++i){
		cin >> x0[i] >> y0[i] >> x1[i] >> y1[i];
		++x1[i];
		++y1[i];
	}
	
	VV(LL) dist;
	initvv(dist, b + 2, b + 2);
	for(int i = 0; i < b + 2; ++i)
	for(int j = i + 1; j < b + 2; ++j){
		LL dx, dy;
		if(x1[i] <= x0[j]){
			dx = x0[j] - x1[i];
		}
		else if(x1[j] <= x0[i]){
			dx = x0[i] - x1[j];
		}
		else{
			dx = 0;
		}
		if(y1[i] <= y0[j]){
			dy = y0[j] - y1[i];
		}
		else if(y1[j] <= y0[i]){
			dy = y0[i] - y1[j];
		}
		else{
			dy = 0;
		}
		
		dist[i][j] = dist[j][i] = max(dx, dy);
	}
	
	vector<LL> ds(b + 2, LLONG_MAX / 2);
	ds[0] = 0;
	priority_queue<pll> pq;
	pq.emplace(0, 0);
	while(!pq.empty()){
		int u = pq.top().second;
		LL d = pq.top().first;
		pq.pop();
		if(ds[u] != d){ continue; }
		
		for(int v = 0; v < b + 2; ++v){
			LL nd = d + dist[u][v];
			if(ds[v] > nd){
				ds[v] = nd;
				pq.emplace(nd, v);
			}
		}
	}
	
	return ds[1];
}


int main(){
	int T = 0;
	cin >> T;
	for(int cnum = 1; cnum <= T; ++cnum){
		fprintf(stderr, "%4d / %d\n", cnum, T);
		cout << "Case #" << cnum << ": " << flush;
		auto ans = solve();
		cout << ans << endl;
	}
}
