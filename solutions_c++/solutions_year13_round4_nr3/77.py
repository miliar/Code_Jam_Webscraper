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


vint solve(){
	int n;
	cin >> n;
	vint a(n + 1), b(n + 1);
	for(int i = 1; i <= n; ++i){
		cin >> a[i];
	}
	for(int i = 1; i <= n; ++i){
		cin >> b[i];
	}

	vvint G(n + 1);
	vint ans(n);
	int z = 0;
	vint tbl(n + 1, -1);
	tbl[0] = 0;

	for(int i = 1; i <= n; ++i){
		G[tbl[a[i] - 1]].push_back(i);
		if(tbl[a[i]] != -1){
			G[i].push_back(tbl[a[i]]);
		}
		tbl[a[i]] = i;
	}
	
	reverse(b.begin() + 1, b.end());
	fill(ALL(tbl), -1);
	tbl[0] = 0;
	for(int i = 1; i <= n; ++i){
		int k = n - i + 1;
		G[tbl[b[i] - 1]].push_back(k);
		if(tbl[b[i]] != -1){
			G[k].push_back(tbl[b[i]]);
		}
		tbl[b[i]] = k;
	}
	vint cnt(n + 1);
	for(int i = 0; i <= n; ++i){
		for(int j = 0; j < G[i].size(); ++j){
			++cnt[G[i][j]];
		}
	}

	priority_queue<int,vint,greater<int> > q;
	q.push(0);
	while(!q.empty()){
		int v = q.top();
		q.pop();
		if(v != 0){
			ans[v - 1] = ++z;
		}
		for(int i = 0; i < G[v].size(); ++i){
			if(!--cnt[G[v][i]]){
				q.push(G[v][i]);
			}
		}
	}

	return ans;
}


int main(){
	cout << fixed << setprecision(10);

	int T = 0;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i){
		fprintf(stderr, "%4d / %4d\n", i, T);
		vint res = solve();
		cout << "Case #" << i << ":";
		for(int i = 0; i < res.size(); ++i){
			cout << ' ' << res[i];
		}
		cout << endl;
	}
}
