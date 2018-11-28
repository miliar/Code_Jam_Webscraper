#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <queue>
#include <fstream>
#include <cstring>

using namespace std;
typedef long long LL;

double r[110], c[110];

int main() {
	freopen("kiddie_pool.in","r",stdin);
	freopen("kiddie_pool.out","w",stdout);
	int tc, nt=1;
	cin>>tc;
	while (tc--) {
		int n;
		double v, x;
		cin>>n>>v>>x;
		for (int i=0;i<n;i++) cin>>r[i]>>c[i];
		cout<<"Case #"<<nt++<<": ";
		if (n==1) {
			if (c[0]==x) printf("%.7lf\n", v*1./r[0]);
			else cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		if (c[0]==c[1]) {
			if (c[0]==x) printf("%.7lf\n", v*1./(r[0]+r[1]));
			else cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		double v1=v*(x-c[0])*1./(c[1]-c[0]);
		double v0=v-v1;
		double eps=1e-9;
		if (v1+eps<=0 || v1-eps>=v || v0+eps<=0 || v0-eps>=v) cout<<"IMPOSSIBLE"<<endl;
		else printf("%.7lf\n", max(v0*1./r[0], v1*1./r[1]));
	}
}
