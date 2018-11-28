//============================================================================
// Name        : Debug.cpp
// Author      : Yunan Luo
// Version     : 1.0.0
// Copyright   : cc
// Description : C++, Ansi-style
//============================================================================

#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
//#include <sstream>
#include <map>
#include <set>
#include <queue>
//#include <stack>
//#include <fstream>
//#include <cstdlib>
//#include <cctype>
//#include <numeric>
//#include <iomanip>
//#include <bitset>
//#include <list>
//#include <stdexcept>
//#include <functional>
//#include <utility>
//#include <ctime>
using namespace std;
#define cpr(n) cout.precision(n);
#define PB push_back
#define MP make_pair
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,l,h) for(int i=(l);i<=(h);++i)
#define FORD(i,h,l) for(int i=(h);i>=(l);--i)
#define long long LL
const int MONTH_DAY[13] = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
const double EPS = 1e-9;
const double PI = acos(-1.0);
const int INF = (int)(1e9 + 7.5);

inline int max(int a, int b) { return a > b ? a : b; }
inline int min(int a, int b) { return a < b ? a : b; }
inline int triangle_area(int x1, int y1, int x2, int y2, int x3, int y3) { return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1); }
int gcd(int x, int y){	if(y==0) return x;	else return gcd(y, x%y);}
//const int MAXN = 1000040;
int a[110][110],b[110][110];
int n,m;
int main() {
    freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	cin>>T;
	FOR(TestCase,1,T){
		cout<<"Case #"<<TestCase<<": ";
		cin>>n>>m;
		REP(i,n) REP(j,m) cin>>a[i][j];
		REP(i,n){
			int t=-1;
			REP(j,m) t=max(t,a[i][j]);
			REP(j,m) b[i][j] = t;
		}
		REP(j,m){
			int t=-1;
			REP(i,n) t=max(t,a[i][j]);
			REP(i,n) if(b[i][j]>=t) b[i][j] = t;
		}
		bool check=true;
		REP(i,n) REP(j,m) if(a[i][j]!=b[i][j]) check=false;
		if (check) cout<<"YES"<<endl;
		else cout<<"NO"<<endl;
	}
	fclose(stdin);
	fclose(stdout);
    return 0;
}
