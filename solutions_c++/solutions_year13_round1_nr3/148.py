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


void solve(){
	int prime[] = {2, 3, 5, 7};

	int R, N, M, K;
	cin >> R >> N >> M >> K;
	vint v(K);
	
	for(int r = 0; r < R; ++r){
		for(int j = 0; j < K; ++j){
			cin >> v[j];
		}

		vvint fact;
		initvv(fact, K, 4);
		for(int j = 0; j < K; ++j){
			int x = v[j];
			for(int t = 0; t < 4; ++t){
				while(x % prime[t] == 0){
					x /= prime[t];
					++fact[j][t];
				}
			}
		}

		vint lst(4);
		for(int j = 0; j < K; ++j){
			for(int t = 0; t < 4; ++t){
				lst[t] = max(lst[t], fact[j][t]);
			}
		}

		string ans;
		for(int i = 1; i < 4; ++i){
			ans += string(lst[i], prime[i] + '0');
		}

		while(ans.size() < N && lst[0] > 0){
			int u = rand() >> 6 & 1;
			if(u){
				lst[0] -= 2;
				ans += '4';
			}
			else{
				--lst[0];
				ans += '2';
			}
		}

		for(int i = 0; i < ans.size() && lst[0] > 0; ++i){
			if(ans[i] == '2'){
				ans[i] = '4';
				--lst[0];
			}
		}

		while(ans.size() < N){
			ans.push_back(rand() % (M - 1) + '2');
		}
		
		if(ans.size() > N){ ans.resize(N); }
		
		cout << ans << endl;
	}
}


int main(){
	srand(time(0));

	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i){
		cout << "Case #" << i << ":\n";
		solve();
	}
}
