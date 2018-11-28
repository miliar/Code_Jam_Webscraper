/**************************************************
 * Author	 : xiaohao Z
 * Blog	 : http://www.cnblogs.com/shu-xiaohao/
 * Last modified : 2016-04-09 16:04
 * Filename	 : C.cpp
 * Description	 : 
 * ************************************************/

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <map>
#define MP(a, b) make_pair(a, b)
#define PB(a) push_back(a)

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<unsigned int,unsigned int> puu;
typedef pair<int, double> pid;
typedef pair<ll, int> pli;
typedef pair<int, ll> pil;

const int INF = 0x3f3f3f3f;
const double eps = 1E-6;
const int LEN = 1000000 + 10;
vector<pli> ans;
int n, k;

ll calc(int num, int jz) {
	ll ret = 0;
	for(int i=n-1; i>=0; i--) {
		ret *= jz;
		if((num>>i) & 1) {
			ret += 1;
		}
	}
	return ret;
}

int is(ll num) {
	for(int i=2; i<min(num, 1000000LL); i++) if(num%i == 0) 
		return i;
	return -1;
}

int solve(int num) {
	ans.clear();
	for(int i=2; i<=10; i++) {
		ll N = calc(num, i);
		int t = is(N);
		if(t == -1) return 0;
		ans.PB(MP(N,t));
	}
	return 1;
}

int main()
{
	//freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin >> n >> k;
	cout << "Case #1: " << endl;
	int Cnt = 0;
	for(int i=0; i<(1<<(n - 2)); i++) {
		int num = (1 << (n - 1)) + ((i << 1) | 1);
		int tt = solve(num);
		if(tt) {
			for(int i=n-1; i>=0; i--)
				cout << ((num>>i)&1);
			for(int i=0; i<ans.size(); i++) 
				cout << ' ' << ans[i].second ;
			cout << endl;
		}
		Cnt += tt;
		if(Cnt == k) break;
	}
	return 0;
}

