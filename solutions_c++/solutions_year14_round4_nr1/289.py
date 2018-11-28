

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
	freopen("F:/TDDOWNLOAD/A-large.in", "r", stdin);
	freopen("F:/TDDOWNLOAD/A-large.out", "w", stdout);

	int Te;
	cin>>Te;
	for(int te=1;te<=Te;te++) {
		int N, X; cin>>N>>X;
		vector<int> v;
		rep(i, 0, N) {
			int t; cin>>t;
			v.push_back(t);
		}
		sort(all(v));
		vector<bool> vst(sz(v), false);
		int ans = 0;
		for(int i=sz(v)-1;i>=0;i--) if(vst[i]==false) {
			int j;
			for(j=i-1;j>=0;j--) if(vst[j]==false && v[j]+v[i]<=X) break;
			if(j>=0) {
				vst[j] = true;
			}
			vst[i] = true;
			ans ++;
		}


		printf("Case #%d: ", te);

		cout<<ans<<endl;
	}
}








