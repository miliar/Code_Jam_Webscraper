

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
		int N;
		cin>>N;
		vector<string> vs;
		vector<int> id;
		for(int i=0;i<N;i++) {
			string s; cin>>s;
			vs.push_back(s);
			id.push_back(0);
		}

		int y = 0;
		while(true) {
			bool all = true;
			for(int i=0;i<N;i++) if(id[i] < vs[i].length()) all = false;
			if(all) break;
			set<char> st;
			vector<int> tmp;
			bool fail = false;
			for(int i=0;i<N;i++) {
				if(id[i] == vs[i].length()) {
					fail = true;
					break;
				}
				st.insert(vs[i][id[i]]);
				int j = id[i];
				while(j<vs[i].length() && vs[i][j]==vs[i][id[i]]) j++;
				tmp.push_back(j-id[i]);
				id[i] = j;
			}
			if(fail || st.size()>1) {
				y = 1000000000;
				break;
			}
			int mi = 1000000000;
			for(int l=1;l<=100;l++) {
				int tt = 0;
				for(int i=0;i<(int)tmp.size();i++) {
					tt += abs(tmp[i] - l);
				}
				mi = min(mi, tt);
			}
			y += mi;
		}
		printf("Case #%d: ", te);
		if(y > 100000000) puts("Fegla Won");
		else printf("%d\n", y);
	}
}








