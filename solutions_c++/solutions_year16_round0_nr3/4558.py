#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <vector>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <algorithm>
#include <deque>
#include <queue>
#include <ctime>
#include <cstring>
#include <iomanip>

#define SZ(x) ((int)x.size())
#define X first
#define Y second 
#define PB push_back 
#define MP make_pair 

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<pii, int> piii;

int n, J;
vector <int> v;

ll bs(ll x, ll b){
	ll ret = 0;
	ll c = 1;
	while(x){
		ret += (x % 2) * c;
		x /= 2;
		c *= b;
	}
	return ret;
}

int main(){
	ios::sync_with_stdio(0);
	cin.tie(0);
	freopen("output", "w", stdout);
	int T; cin >> T;
	cout << "Case #1:\n";
	cin >> n >> J;
	for(int i = 1 << (n - 1); J && i < 1 << n; i ++){
		if(!(i & 1)) continue;
		v.clear();
		for(int j = 2; j <= 10; ++j){
			ll t = bs(i, j);
		//	cout << i << " " << j << " " << t << "\n";
			for(ll k = 2; k * k <= t; ++k){
				if(t % k == 0){
					v.PB(k);
					break;
				}
			}
		}
		if(SZ(v) == 9){
			string s = "";
			int x = i;
			while(x){
				char ch = x % 2 + '0';
				s =  ch + s;
				x /= 2;
			}
			cout << s << " ";
			for(int k = 0; k < SZ(v); ++k)
				cout << v[k] << " ";
			cout << "\n";
			J --;
		}
	}
	return 0;
}
