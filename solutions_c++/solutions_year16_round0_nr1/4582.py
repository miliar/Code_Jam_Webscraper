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

ll res[1000000 + 10];

ll check(ll x) {
	ll n = x;
	bool arr[11] = { 0 };
	while (1) {
		ll t = x;
		while (t) {
			arr[t % 10] = 1;
			t /= 10;
		}
		bool flag = 1;
		Rep(i, 10) {
			if (!arr[i]) {
				flag = 0;
				break;
			}
		}
		if (flag) return x;
		x += n;
	}
	return -1;
}

int main(int argc, char *argv[]) {
	ios::sync_with_stdio(false);
#ifndef ONLINE_JUDGE
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	Set(res, -1);
	For(i, 1, 1000000+1) {
		ll x = -1;
		x = check(i);
		res[i] = x;
		//PF("%d ========= %I64d\n", i, x);
	}
	//timestamp(end);
	int n , t , tc = 1 ;
	SF("%d", &t);
	while (t--) {
		SF("%d", &n);
		PF("Case #%d: ", tc++);
		if ( res[n] != -1 ) PF ( "%I64d\n", res[n]);
		else PF("INSOMNIA\n");
	}
	return 0;
}