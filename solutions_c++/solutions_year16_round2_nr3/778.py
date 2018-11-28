#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
#define pb(X) push_back(X)
#define mp(X,Y) make_pair(X,Y)
#define sz(X) (int)X.size()
#define clr(X) memset(X,0,sizeof(X));
#define xx first
#define yy second
typedef pair<int, int> pii;
typedef long long ll;
typedef unsigned long long ull;


vector< pair<string,string> > v;
int n, ret;

void testMask(int m) {
  map< string, bool> mleft;
  map< string, bool> mright;

  for(int i=0;i<n;i++) {
		if ( (m&(1<<i))) {
			mleft[v[i].first] = true;
			mright[v[i].second] = true;
		}
	}
	int cnt=0;
	for(int i=0;i<n;i++) {
		if (!(m&(1<<i))) {
			cnt++;
			if(!mleft[v[i].first] || !mright[v[i].second])
				return;
		}
	}
	if (cnt > ret) ret = cnt;
}

int main(){
	int T;
	scanf("%d", &T);
	for(int caso=1;caso<=T;caso++) {
		cin >> n;
		v.clear();
		ret =0;
		for(int i=0;i<n;i++) {
			string r,s;
			cin >> r >> s;
			v.pb(mp(r,s));
		}
		for(int m=0; m< (1<<n); m++) {
			testMask(m);
		}
		printf("Case #%d: %d\n",caso,ret);
	}
	return 0;
}
