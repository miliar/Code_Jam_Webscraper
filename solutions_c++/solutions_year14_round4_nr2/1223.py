#include <map>
#include <vector>
#include <cstdio>
#include <queue>
#include <algorithm>

using namespace std;

map<vector<int>,int> vis;
queue<vector<int> > q;

int n;
int a[1111];

int updown(vector<int> &o) {
	int ix=1;
	while(ix<n && a[o[ix-1]] < a[o[ix]]) ix++;
	while(ix<n && a[o[ix-1]] > a[o[ix]]) ix++;
	return ix==n;
}

void solve() {
	int i;
	vis.clear();
	q=queue<vector<int> >();
	scanf("%d",&n);
	for(i=0;i<n;i++) scanf("%d",&a[i]);
	vector<int> cur;
	for(i=0;i<n;i++) cur.push_back(i);
	q.push(cur); vis[cur]=0;
	if(updown(cur)) { puts("0"); return; }
	while(!q.empty()) {
		cur=q.front(); q.pop(); int moves=vis[cur];
		for(i=0;i<n-1;i++)  {
			vector<int> next=cur;
			swap(next[i],next[i+1]);
			if(vis.find(next)!=vis.end()) continue;
			if(updown(next)) { printf("%d\n",moves+1); return; }
			vis[next]=moves+1;
			q.push(next);
		}
	}
	printf("error");
}

int main() {
	int T,no=1;
	scanf("%d",&T);
	while(T--) printf("Case #%d: ",no++),solve();
	return 0;
}
