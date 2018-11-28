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
	int n;
	scanf("%d",&n);
	vector<double> f(n),s(n);
	set<double> tmp;
	rept(i,n) cin>>f[i];
	rept(i,n) cin>>s[i],tmp.insert(s[i]);
	sort(all(f)); sort(all(s));
	int rs1(0),cr(0);
	rept(i,n) {
		if (f[i]>s[cr])
			++cr,++rs1;
	}
	int ind(0);
	while (ind<n && tmp.lower_bound(f[ind])!=tmp.end())
		tmp.erase(tmp.lower_bound(f[ind])),++ind;
	printf("%d %d\n",rs1,n-ind);
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
