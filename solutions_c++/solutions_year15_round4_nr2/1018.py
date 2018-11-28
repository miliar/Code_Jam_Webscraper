#include <string>
#include <cstring>
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
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
using namespace std;
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).rbegin(),(v).rend()
#define pb(x) push_back(x)
#define REP(i,x,y) for(int (i)=(x);(i)<(y);(i)++)
#define REPIT(it,A) for(typeof(A.begin()) it = (A.begin()); it!=A.end();it++)
#define sqr(x) ((x)*(x))
#define mp(x,y) make_pair((x),(y))
#define trace(x) cerr << #x << ": " << x << endl;
#define fst first
#define snd second
#define itm1 fst.fst
#define itm2 fst.snd
#define itm3 snd
#define mt(a,b,c) mp(mp(a,b),c)
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long int64;
typedef unsigned long long uint64;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<ii, int> tri;
typedef pair<ll, ll> pll;
typedef pair<pll, ll> tri64;
typedef set<int> seti;
typedef set<ii> setii;
typedef stack<int> stki;
typedef stack<ii> stkii;
typedef queue<int> qi;
typedef queue<ii> qii;
typedef map<int,int> mapii;
typedef map<string,int> mapsi;
typedef unsigned int uint;

const double PI = 3.14159265359;
const double EPS = 1e-6;

double ans;

int n, flg;
double v[5], t[5], vf, tf;
double a, b;

int eq(double x, double y){
	return abs(x-y) < EPS;
}

int lt(double x, double y){
	return (x < y) && !eq(x,y);
}

int main(){
	int nCases;
	scanf("%d", &nCases);
	REP(casenum,0,nCases){
		flg = 0;
		scanf("%d %lf %lf", &n, &vf, &tf);
		REP(i,0,n) scanf("%lf %lf", &v[i], &t[i]);
		if (n == 1) {
			if (eq(t[0], tf)) ans = vf/v[0];
			else flg = 1;
		}
		if (n == 2) {
			ans = 2000000000;
			if (eq(t[1], tf) && eq(t[0], tf)){
				ans = min(ans, vf / (v[0]+v[1]));
			}
			else if (eq(t[0], tf))	{
				//b = 0.9*1e-6*vf/(v[1]*t[1]);
				ans = min(ans, vf/v[0]);// - b*v[1]/v[0]);
			}
			else if (eq(t[1], tf)){
				//a = 0.9*1e-6*vf/(v[0]*t[0]);
				ans = min(ans, vf/v[1]);// - a*v[0]/v[1]);
			}
			else {
				a = vf*(t[1]-tf)/(v[0]*(t[1]-t[0]));
				b = vf*(tf-t[0])/(v[1]*(t[1]-t[0]));
				if (lt(a,0) || lt(b,0)) flg = 1;
				else ans = max(a,b);
			}
		}
		printf("Case #%d: ", casenum+1);
		if (!flg) printf("%.9lf\n", ans);
		else printf("IMPOSSIBLE\n");
	}  
	return 0;
}

