/* Divanshu Garg */

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <climits>
#include <cctype>
#include <cassert>

using namespace std;

#define ull unsigned long long
#define ill long long int
#define pii pair<int,int>
#define pb(x) push_back(x)
#define F(i,a,n) for(int i=(a);i<(n);++i)
#define FD(i,a,n) for(int i=(a);i>=(n);--i)
#define FE(it,x) for(it=x.begin();it!=x.end();++it)
#define V(x) vector<x>
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%llu",&x)
#define M(x,i) memset(x,i,sizeof(x))
#define debug(i,sz,x) F(i,0,sz){cout<<x[i]<<" ";}cout<<endl
#define MAX(a,b) ((a)>(b)?(a):(b))
int ABS(int a) { if ( a < 0 ) return (-a); return a; }
#define fr first
#define se second

/* Relevant code begins here */

/* Input from file or online */

void input() {
#ifndef ONLINE_JUDGE
    // freopen("input.txt","r",stdin);
    freopen("B-small-attempt4.in","r",stdin);
    // freopen("out.txt","w",stdout);
#endif
}

#define INF 10000000

int n;
int a[1005];
int b[1005];
int dp[10][1<<10][2][10];
int mx;

int f(int idx,int mask,bool peak,int last) {

	if ( idx == n ) {
		return 0;
	}

	int &res = dp[idx][mask][peak][last];
	if ( res != -1 ) return res;

	res = INF;

	if ( peak == true) {
		int cnt = 0;
		F(i,0,n) {
			if ( ((1<<i)&mask) == 0 ) {
				if ( a[last] < a[i] )
					res = min(res, cnt+f(idx+1,mask|(1<<i),true,i));
				cnt++;
			}
		}
		res = min (res, f (idx, mask, false, last));
	} else {
		int cnt = 0;
		F(i,0,n) {
			if ( ((1<<i)&mask) == 0 ) {
				if (a[last] > a[i] )
					res = min(res, cnt+f(idx+1,mask|(1<<i),false,i));

				cnt++;
			}
		}
	}

	return res;


}

int main() {
    input();
    int t;
    cin >> t;
    int tst = 1;
    while ( t-- ) {
        cin >> n;
        F(i,0,n) {
            cin >> a[i];
            if ( i == 0 ) mx = a[0];
            else mx=max(mx,a[i]);
        }
        M(dp,-1);
        int ans = 10000000;

        int cnt = 0;
        for (int i = 0; i < n; i++) {
            ans = min (ans, cnt + f (1, (1LL<<i), true, i));
            cnt++;
        }

        cout << "Case #" << tst++ << ": ";
        cout << ans << endl;
    }
    return 0;
}