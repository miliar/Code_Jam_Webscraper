

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



struct DD{
	DD* next[26];
	DD() {
		clr(next, NULL);
	}
};

void insert(DD*root, string s) {
	for(int i=0;i<s.length();i++) {
		int d = s[i] - 'A';
		if(root->next[d] == NULL) {
			root->next[d] = new DD();
		}
		root = root->next[d];
	}
}
int dfs(DD*root) {
	int ret = 1;
	rep(i, 0, 26) if(root->next[i]) ret += dfs(root->next[i]);
	return ret;
}

void release(DD* root) {
	rep(i, 0, 26) if(root->next[i]) release(root->next[i]);
	delete root;
}

int max_nodes, ways;
vector<string> lofters[4];

void dfs(vector<string> vs, int M, int N, int cur) {
	if(cur == sz(vs)) {
		bool can = true;
		rep(i, 0, N) if(lofters[i].size() == 0) can = false;
		if(!can) return;
		int tmp_node = 0;
		rep(i, 0, N) {
			DD *root = new DD();
			rep(j, 0, sz(lofters[i])) {
				insert(root, lofters[i][j]);
			}
			tmp_node += dfs(root);
			release(root);
		}
		if(tmp_node > max_nodes) {
			max_nodes = tmp_node;
			ways = 1;
		} else if(tmp_node == max_nodes) {
			ways ++;
		}
		return;
	}
	for(int i=0;i<N;i++) {
		lofters[i].push_back(vs[cur]);
		dfs(vs, M, N, cur+1);
		lofters[i].pop_back();
	}
}

int main() {
	freopen("F:/TDDOWNLOAD/D-small-attempt0.in", "r", stdin);
	freopen("F:/TDDOWNLOAD/D-small-attempt0.out", "w", stdout);

	int Te;
	cin>>Te;
	for(int te=1;te<=Te;te++) {
		int M, N; cin>>M>>N;
		vector<string> vs;
		rep(i, 0, M) {
			string s; cin>>s;
			vs.push_back(s);
		}
		max_nodes = 0;

		dfs(vs, M, N, 0);


		printf("Case #%d: ", te);

		cout<<max_nodes<<' '<<ways<<endl;
	}
}








