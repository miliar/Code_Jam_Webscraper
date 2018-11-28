#include <iterator>
#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <bitset>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <fstream>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <numeric>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <valarray>
#ifdef _MSC_VER
#include <hash_set>
#include <hash_map>
using namespace stdext;
#else
#include <ext/hash_set>
#include <ext/hash_map>
using namespace __gnu_cxx;
#endif
using namespace std;

#define SZ(v)                   (int)v.size()
#define FOR(i,a,b)				for(int i=(a);i<(b);++i)
#define rev(i,a,b)				for(int i=(b);i>=(a);--i)
#define sz(v)                   (int)v.size()
#define all(v)					v.begin(), v.end()
#define rall(v)					v.rbegin(), v.rend()
#define pb						push_back
#define mp						make_pair
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<pi> vpi;
const int OO = 1 << 28;

int di[] = { -1, 0, 1, 0 };
int dj[] = { 0, 1, 0, -1 };
#define Nd 0
#define Ed 1
#define Sd 2
#define Wd 3



int main() {
#ifndef ONLINE_JUDGE
	freopen("in.in", "rt", stdin);
		freopen("out.out", "wt", stdout);
#endif
	int t;
	cin >> t;
	vector<vector<int> > v;
	vector<int> mxrow,mxclmn;
	FOR(cs,1,t+1){
		printf("Case #%d: ",cs);
		int n, m;
		cin >> n >> m;
		mxrow.clear();
		mxclmn.clear();
		v.clear();
		v.resize(n,vector<int>(m));
		int mxr,mxc;
		FOR(i,0,n){
			mxr = 0;
			FOR(j,0,m){
				cin >> v[i][j];
				mxr = max(mxr, v[i][j]);
			}
			mxrow.pb(mxr);
		}
		FOR(j,0,m){
			mxc = 0;
			FOR(i,0,n){
				mxc = max(mxc, v[i][j]);
			}
			mxclmn.pb(mxc);
		}
		FOR(i,0,n){
			FOR(j,0,m){
				if(v[i][j] < mxrow[i] && v[i][j] < mxclmn[j]){
					printf("NO\n");
					goto bla;
				}
			}
		}
		printf("YES\n");
		bla:;

	}
	return 0;
}




