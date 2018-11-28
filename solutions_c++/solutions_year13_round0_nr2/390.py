/*
 TASK:B.Lawnmower
 LANG:C++
 Muhammad Magdi Muhammad
 Email: moh_magdi@acm.org
 */
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>

#define all(v)          v.begin(),v.end()
#define allr(v)         v.rbegin(),v.rend()
#define rep(i,m)        for(int i=0;i<(int)m;i++)
#define REP(i,k,m)      for(int i=k;i<(int)m;i++)
#define mem(a,b)        memset(a,b,sizeof(a))
#define mp              make_pair
#define pb              push_back
#define OO ((int)1e9)
#define MAX 100000

typedef long long ll;

int diri[] = { -1, 0, 1, 0, -1, 1, 1, -1 };
int dirj[] = { 0, 1, 0, -1, 1, 1, -1, -1 };
int compare(double d1, double d2) {
	if (fabs(d1 - d2) < 1e-9)
		return 0;
	if (d1 < d2)
		return -1;
	return 1;
}
int I, J;
inline bool valid(const int &i, const int &j) {
	if (i < 0 || j < 0 || i >= I || j >= J)
		return false;
	return true;
}

using namespace std;

#define SMALL
#define LARGE
int T;
int n , m ;
int grid[101][101];
bool check(int i, int j, int row){
	if(row){
		for(int k = 0 ; k < m ; k++){
			if(grid[i][k] > grid[i][j])return 0 ;
		}
	}else{
		for (int k = 0; k < n; ++k) {
			if(grid[k][j] > grid[i][j])return 0 ;
		}
	}
	return 1 ;
}
int main() {

	freopen("1.in", "rt", stdin);
#ifdef SMALL
	freopen("B-small-attempt1.in","rt",stdin);
	freopen("B.Lawnmower-small1.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("B-large.in","rt",stdin);
	freopen("B.Lawnmower-large.out","wt",stdout);
#endif

	cin >> T;
	rep(tt,T) {
		printf("Case #%d: ", tt + 1);
//		int n, m;
		cin >> n >> m;
		rep(i,n) {
			rep(j,m) {
				cin >> grid[i][j] ;
			}
		}
		bool valid = 1 ;
		rep(i,n){
			rep(j,m){
				valid &= (check(i,j,0) | check(i,j,1)) ;
			}
		}
		if(valid) cout << "YES" << endl ;
		else cout << "NO" << endl ;
		cerr << tt << endl;
	}
	return 0;
}
//end

