

#include <deque>
#include <queue>
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
#include <set>
#include <cstdlib>
#include <hash_map>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cassert>
#include <ctime>

using namespace std;

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector<string> VS;

#define rep(i,s,e) for(int i=s;i<e;i++)
#define sz(X) ((int)(X.size()))
#define tr(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define all(x) x.begin(),x.end()
#define clr(x,c) memset(x,c,sizeof(x))
//---------------------------------------------------------------



int main() {
	freopen("F:/TDDOWNLOAD/B-large.in", "r", stdin);
	freopen("F:/TDDOWNLOAD/B-large.out", "w", stdout);
	
	int Te;
	cin>>Te;
	for(int te=1;te<=Te;te++) {
		double C, F, X;
		cin>>C>>F>>X;
		double ans = 1e100, curT = 0.0, rate = 2.0;
		while(true) {
			if(curT+X/rate > ans) break;
			ans = min(ans, curT+X/rate);
			double tmp = C/rate;
			curT += tmp;
			rate += F;
		}

		printf("Case #%d: %.13lf\n", te, ans);
	}
}








