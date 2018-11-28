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



struct node{
	map<char,unique_ptr<node>> child;
};
int insstr(node *nd, const string &s){
	int ret = 0;
	for(char c : s){
		if(nd->child.count(c)){
			nd = nd->child.at(c).get();
		}
		else{
			node *next = new node;
			nd->child.insert(make_pair(c, unique_ptr<node>(next)));
			nd = next;
			++ret;
		}
	}
	return ret;
}

pll ans;
int m, n;
vector<string> ss;
vector<int> as;

void check(){
	vector<unique_ptr<node>> ts(n);
	for(int i = 0; i < n; ++i){
		ts[i].reset(new node);
	}
	
	LL cnt = n;
	for(int i = 0; i < m; ++i){
		cnt += insstr(ts[as[i]].get(), ss[i]);
	}

	if(ans.first < cnt){
		ans = pll(cnt, 0);
	}
	if(ans.first == cnt){
		++ans.second;
	}
}

void dfs(int k, int S){
	if(k == m){
		if((S + 1) >> n){
			check();
		}
	}
	else{
		for(int i = 0; i < n; ++i){
			as[k] = i;
			dfs(k + 1, S | 1 << i);
		}
	}
}


pll solve(){
	ans = pll(-1, -1);
	cin >> m >> n;
	ss.resize(m);
	for(int i = 0; i < m; ++i){
		cin >> ss[i];
	}
	as.assign(m, 0);
	dfs(0, 0);
	
	return ans;
}


int main(){
	int T = 0;
	cin >> T;
	for(int cnum = 1; cnum <= T; ++cnum){
		fprintf(stderr, "%4d / %d\n", cnum, T);
		cout << "Case #" << cnum << ": " << flush;
		auto ans = solve();
		cout << ans.first << ' ' << ans.second << endl;
	}
}
