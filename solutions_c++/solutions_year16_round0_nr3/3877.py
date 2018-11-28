///////////////////////IN THE NAME OF GOD
#include <iostream>
#include <vector>
#include <stack>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>
#include <queue>
#include <map>
#include <fstream>
#include <utility>
#include <sstream>
#include <list>
#include <iomanip>
#include <functional>
#include <deque>
#include <ctime>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <complex>
#include <climits>
#include <cctype>
#include <cassert>
#include <bitset>
#include <limits>
#include <numeric>

using namespace std;

#define     For(i,a,b)      for (int i=a; i<(int)b; i++)
#define     Rep(i,a)        for (int i=0; i<(int)a; i++)
#define     ALL(v)          (v).begin(),(v).end()
#define     Set(a,x)        memset((a),(x),sizeof(a))
#define     EXIST(a,b)      find(ALL(a),(b))!=(a).end()
#define     Sort(x)         sort(ALL(x))
#define     UNIQUE(v)       Sort(v); (v).resize(unique(ALL(v)) - (v).begin())
#define     SF              scanf
#define     PF              printf
#define     timestamp(x)    printf("Time : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC)
#define     INF             1e9
#define     pii             pair < int , int >
#define     MP              make_pair
#define     MOD             1000000007
#define     EPS             1e-9
#define     ll              long long
#define     MAXN            100000+10
#define     Dbug            cout<<""
#define     PI                3.1415926535897932384626433
//int month[]={0,31,29,31,30,31,30,31,31,30,31,30,31};

ll is_prime(ll c) {
	ll x = sqrt((double)c) + 10;
	For(i, 2, x) {
		if ( i != c && c % i == 0) return i;
	}
	return -1;
}

int main(int argc, char *argv[]) {
	ios::sync_with_stdio(false);
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	cout << "Case #1:" << endl;
	ll x = 1;
	ll n, J, cnt = 0;
	cin >> n >> n >> J ;
	x = (1 << n);
	For(i , 2 , x + 1 ) {
		if (cnt == J) break;
		if (i & 1) {
			bool flag = 1;
			vector < ll > res;
			ll ii = i;
			ll tmpcnt = 0;
			while (ii) {
				ii >>= 1;
				tmpcnt++;
			}
			if (tmpcnt != n) continue;
			for (ll j = 2; j <= 10; j++) {
				ll c = i ;
				ll num = 0, p = 1;
				while (c) {
					if (c & 1) num += p;
					c >>= 1;
					p *= j;
				}
				ll pri = is_prime(num);
				if ( pri == -1 ) {
					flag = 0;
					break;
				}
				res.push_back(pri);
			}
			if (flag) {
				ll c = i;
				string tmp;
				while (c) {
					tmp.push_back((c & 1) ? '1' : '0');
					c >>= 1;
				}
				reverse(ALL(tmp));
				//if (tmp.size() < 2) continue;
				cout << tmp << " ";
				Rep(j, res.size()) {
					cout << res[j];
					if (j != res.size() - 1) cout << ' ';
				}
				cout << endl;
				cnt++;
			}
		}
	}
	return 0;
}