

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


vector<int> adj[110], orderId;
int N, M, val[55];
bool vst[55], tvst[55];


void dfs(int u) {
	tvst[u] = true;
	for(int i=0;i<adj[u].size();i++) {
		int v = adj[u][i];
		if(tvst[v]) continue;
		dfs(v);
	}
}

vector<int> ansId;



int main() {
	freopen("F:/TDDOWNLOAD/C-large.in", "r", stdin);
	freopen("F:/TDDOWNLOAD/C-large.out", "w", stdout);

	int Te;
	cin>>Te;
	for(int te=1;te<=Te;te++) {
		cin>>N>>M;
		vector<pair<int, int> > vv;
		for(int i=1;i<=N;i++) {
			cin>>val[i];
			vv.push_back(make_pair(val[i], i));
			adj[i].clear();
		}
		for(int i=1;i<=M;i++) {
			int a, b;
			cin>>a>>b;
			adj[a].push_back(b);
			adj[b].push_back(a);
		}

		sort(all(vv));
		orderId.clear();
		for(int i=0;i<vv.size();i++) {
			orderId.push_back(vv[i].second);
		}

		memset(vst, false, sizeof(vst));
		vector<int> sta; // stack

		ansId.clear();

		sta.push_back(orderId[0]);
		ansId.push_back(orderId[0]);
		vst[orderId[0]] = true;

		while(true) {
			int vv = -1;
			for(int i=0;i<orderId.size();i++) if(vst[orderId[i]]==false) {
				bool ff = false;
				for(int j=sta.size()-1;j>=0;j--) {
					bool find = false;
					for(int k=0;k<adj[sta[j]].size();k++) {
						if(adj[sta[j]][k] == orderId[i]) {
							find = true;
							break;
						}
					}
					if(find==false) continue;

					memcpy(tvst, vst, sizeof(vst));
					for(int k=j;k>=0;k--) dfs(sta[k]);
					int num = 0;
					for(int s=1;s<=N;s++) num += tvst[s];
					if(num == N) {
						for(int k=sta.size()-1;k>j;k--) sta.pop_back();
						sta.push_back(orderId[i]);
						vst[orderId[i]] = true;
						ansId.push_back(orderId[i]);
						ff = true;
						break;
					}
				}
				if(ff) {
					vv = 0;
					break;
				}
			}
			if(vv==-1) break;
		}

		printf("Case #%d: ", te);
		for(int i=0;i<ansId.size();i++) {
			cout<<val[ansId[i]];
		}
		cout<<endl;
	}
}








