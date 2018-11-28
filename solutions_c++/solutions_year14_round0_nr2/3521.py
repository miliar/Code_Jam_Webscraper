#include <iostream>
#include <functional>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <memory>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <utility>
#include <iterator>
#include <bitset>
#include <sstream>
#include <numeric>
#include <complex>

#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define pdd pair<double,double>
#define LL long long
#define ULL unsigned LL
#define VI vector<int>
#define X first
#define Y second
#define sz(_v) ((int)_v.size())
#define all(_v) (_v).begin(),(_v).end()
#define FOR(i,a,b) for (int i(a); i<=(b); ++i)
#define rep(i,a) FOR(i,1,a)
#define rept(i,a) FOR(i,0,(LL)(a)-1)
#define x1 X1
#define y1 Y1
#define sqr(a) ((a)*(a))
#define C(a) memset((a),0,sizeof (a))
#define MS(a,x) memset((a),(x),sizeof (a))
#define INF 1150000000
#define PI 3.141592653589
#define eps 1e-8
#define MOD 1000000007
#define PRIME 149

using namespace std;

void solvePart() {
	double c,f,x;
	cin>>c>>f>>x;
	double rs(0);
	double now(2);
	while (true) {
		double without(x/now);
		double with((c/now)+(x/(now+f)));
		if (with<without)
			rs+=c/now,now+=f;
		else
			break;
	}
	printf("%.8lf\n",rs+(x/now));
}

void solve() {
	int tst;
	scanf("%d",&tst);
	rept(t,tst) {
		printf("Case #%d: ",t+1);
		solvePart();
	}
}

void bruteforce() {
}

int main() {
#ifndef ONLINE_JUDGE
    {
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    }
#endif
    solve();
    bruteforce();
    return 0;
}
