

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




void run() {
	int r1, r2;
	vector<int> v1;
	set<int> v2;
	cin>>r1;
	for(int i=1;i<=4;i++) {
		for(int j=1;j<=4;j++) {
			int x; cin>>x;
			if(i==r1) v1.push_back(x);
		}
	}
	cin>>r2;
	for(int i=1;i<=4;i++) {
		for(int j=1;j<=4;j++) {
			int x; cin>>x;
			if(i==r2) v2.insert(x);
		}
	}

	vector<int> ans;
	for(int i=0;i<4;i++) {
		if(v2.find(v1[i]) != v2.end()) ans.push_back(v1[i]);
	}
	if(sz(ans) == 1) printf("%d", ans[0]);
	else if(sz(ans) > 1) printf("Bad magician!");
	else printf("Volunteer cheated!");
}


int main() {
	freopen("F:/TDDOWNLOAD/A-small-attempt0.in", "r", stdin);
	freopen("F:/TDDOWNLOAD/A-small-attempt0.out", "w", stdout);
	
	int Te;
	cin>>Te;
	for(int te=1;te<=Te;te++) {
		printf("Case #%d: ", te);
		run();
		puts("");
	}
}








