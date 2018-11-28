

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
		int N; cin>>N;
		vector<int> v;
		rep(i, 0, N) {
			int x; cin>>x;
			v.push_back(x);
		}
		int ans = 0;
		while(sz(v)>1) {
			int mi = 1e9 + 1, id;
			rep(i, 0, sz(v)) {
				if(v[i]<mi) {
					mi = v[i];
					id = i;
				}
			}
			ans += min(id, sz(v)-1-id);
			v.erase(v.begin()+id);
		}


		printf("Case #%d: ", te);

		cout<<ans<<endl;
	}
}








