#include <iostream>
#include <stack>
#include <set>
#include <map>
#include <queue>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>
#include <string>
#include <deque>
#include <cmath>
#include <iomanip>

using namespace std;

const int INF = 1000000007;
const int MOD = 1000000007;

const int N = 100007;

int main() {
	int T;cin>>T;
	for(int I=1;I<=T;++I) {
		int n;
		long double v,x;
		cin>>n>>v>>x;
		vector<long double> r(n), c(n);
		for(int i=0;i<n;++i)cin>>r[i]>>c[i];
		long double res = -1;
		const long double EPS = 1e-9;
		if (n == 1) {
			if (fabs(c[0] - x) < EPS) res = v/r[0];
			else res = -1;
		} else {
			if (fabs(c[0]-c[1]) > EPS) {
				long double a = v*(x-c[1])/(c[0]-c[1])/r[0],
					 b = v*(x-c[0])/(c[1]-c[0])/r[1];
				if (a >= 0 && b >= 0) {
					res = max(a,b);
				}
			} else {
				if (fabs(c[0] - x) < EPS) res = v/(r[0]+r[1]);
			}
		}
		printf("Case #%d: ", I);
		if (n > 2) cout<<"n>2\n";
		else if (res < 0) cout<<"IMPOSSIBLE\n";
		else cout<<fixed<<setprecision(12)<<res<<endl;
	}
	return 0;
}
