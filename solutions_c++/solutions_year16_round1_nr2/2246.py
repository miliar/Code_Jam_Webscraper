#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;
typedef pair<int, int> pii;

int n, v[201][51], used[201];
vector<int> adj[201];
vector<int> curr; 
set<vector<int> > vis;

int solve(int pos) {
	curr.push_back(pos);
	if (curr.size() == n) {
		vis.clear();
		for(int i=0;i<2*n-1;i++) used[i]=0;
		for(int i=0;i<n;i++) used[curr[i]]=1;
		for(int i=0;i<n;i++) {
			vector<int> x(n);
			for(int j=0;j<n;j++) x[j] = v[curr[i]][j];
		}
		for(int i=0;i<n;i++) {
			vector<int> x(n);
			for(int j=0;j<n;j++) x[j] = v[curr[j]][i];
			vis.insert(x);
		}
		for(int i=0;i<2*n-1;i++) if(!used[i]) {
			vector<int> x(n);
			for(int j=0;j<n;j++) x[j] = v[i][j];
			if (vis.count(x) == 0) {
				curr.pop_back();
				return 0;
			}
			vis.erase(x);
		}
		return 1;
	}
	for(int i=0;i<adj[pos].size();i++)
		if (solve(adj[pos][i]))
			return 1;
	curr.pop_back();
	return 0;
}

int main() {
	int T;
	cin>>T;
	for(int t=1;t<=T;t++) {
		printf("Case #%d:", t);
		cin>>n;
		int m = 1e9;
		for(int i=0;i<2*n-1;i++) {
			adj[i].clear();
			for(int j=0;j<n;j++) scanf("%d", &v[i][j]);
			m = min(m, v[i][0]);
		}
		for(int i=0;i<2*n-1;i++) for(int j=0;j<2*n-1;j++) {
			int ok=1;
			for(int k=0;k<n;k++) if(v[i][k]>=v[j][k]) ok=0;
			if(ok) {
				adj[i].push_back(j);
			}
		}
		for(int i=0;i<2*n-1;i++) 
			if(v[i][0] == m) {
				curr.clear();
				if (solve(i)) {
					vector<int> ans = *vis.begin();
					for (int i=0;i<n;i++) cout << " " << ans[i];
					cout << endl;
					break;
				}
			}
	}
	return 0;
}
