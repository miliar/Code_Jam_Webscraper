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
#define Sl(x) scanf("%lld",&x)
#define M(x,i) memset(x,i,sizeof(x))
#define debug(i,sz,x) F(i,0,sz){cout<<x[i]<<" ";}cout<<endl
ill ABS(ill a) { if ( a < 0 ) return (-a); return a; }
#define fr first
#define se second

/* Relevant code begins here */

/* Input from file or online */

void input() {
#ifndef ONLINE_JUDGE
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
#endif
}

/* Input opener ends */

int main() {
	// input();
	int t, tst = 1;
	cin >> t;
	while ( t-- ) {
		cout << "Case #" << tst++ << ": ";
		int r1,r2; cin >> r1;
		vector<int> x,y;
		F(i,0,4) {
			vector<int> tmp;
			F(j,0,4) {
				int xx; cin >> xx;
				tmp.pb(xx);
			}
			if ( i+1 == r1 ) x = tmp;
		}
		cin >> r2;
		F(i,0,4) {
			vector<int> tmp;
			F(j,0,4) {
				int xx; cin >> xx;
				tmp.pb(xx);
			}
			if ( i+1 == r2 ) y = tmp;
		}
		int res = 0, val = -1;
		F(i,0,4) {
			F(j,0,4) {
				if ( x[i] == y[j] ) {
					val = x[i];
					res++; break;
				}
			}
		}
		if ( res > 1 ) cout << "Bad magician!" << endl;
		else if ( res == 0 ) cout << "Volunteer cheated!" << endl;
		else cout << val << endl;

	}
	return 0;
}