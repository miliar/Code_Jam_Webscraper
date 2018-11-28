#include<iostream>
#include<sstream>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<complex>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cassert>

#define rep(i,n) for(int i=0;i<(int)n;i++)
#define all(c) (c).begin(),(c).end()
#define mp make_pair
#define pb push_back
#define each(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
#define dbg(x) cerr<<__LINE__<<": "<<#x<<" = "<<(x)<<endl

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
const int inf = (int)1e9;
const double INF = 1e12, EPS = 1e-9;

ll n, p;
int mn, mn2;
int one[60][2]; //pos, sml
int zero[60][2]; //pos, gre

void solve(){
	mn = mn2 = inf;
	rep(i, 60) rep(j, 2) one[i][j] = zero[i][j] = inf;
	one[0][0] = zero[0][0] = 0;
	rep(i, n) rep(j, 2){
		if(zero[i][j] < inf) rep(k, 2){
			if(!j && (p >> (n - i - 1) & 1) < k) continue;
			int nj = j || (p >> (n - i - 1) & 1) > k;
			zero[i + 1][nj] = min(zero[i + 1][nj], zero[i][j] + (k == 0));
		}
		if(one[i][j] < inf) rep(k, 2){
			if(!j && (p >> (n - i - 1) & 1) > k) continue;
			int nj = j || (p >> (n - i - 1) & 1) < k;
			one[i + 1][nj] = min(one[i + 1][nj], one[i][j] + (k == 1));
		}
	}
	mn = min(zero[n][0], zero[n][1]);
	mn2 = one[n][1];
}

void run(){
	cin >> n >> p;
	p--;
	solve();
	
	ll a = (1ll << mn2) - 2, b = (1ll << n) - (1ll << mn);
	if(mn2 == 1) a = 0;
	if(mn2 == inf) a = (1ll << n) - 1;
	cout << a << " " << b <<endl;
}

int main(){
	int CS;
	cin >> CS;
	rep(cs, CS){
		cout << "Case #" << cs + 1 << ": ";
		run();
	}
	return 0;
}
