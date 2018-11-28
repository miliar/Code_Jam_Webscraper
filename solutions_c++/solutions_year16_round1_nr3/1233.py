#include <bits/stdc++.h>
using namespace std;

int main() {
	freopen ("in.txt", "r", stdin);
	freopen ("res.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int tc = 1; tc <= t; tc++) {
		int n;
		int a[1005];
		scanf("%d", &n);
		for(int i = 1; i <= n; i++) scanf("%d", a + i);
//	/*	
		int ans = 1, b[1005];
		for(int i = 1; i <= n; i++) b[i] = i;
		do {
			for(int len = 2; len <= n; len++) {
				bool ok = 1;
				for(int i = 2; i < len; i++) ok &= a[b[i]] == b[i - 1] || a[b[i]] == b[i + 1];
				ok &= a[b[1]] == b[len] || a[b[1]] == b[2];
				ok &= a[b[len]] == b[len - 1] || a[b[len]] == b[1];
				if(ok) ans = max(ans, len);
			}
		} while(next_permutation(b + 1, b + n + 1));
//	*/	
		/*
		vector <int> g1[1005], g2[1005];
		for(int i = 1; i <= n; i++) {
			g1[i].push_back(a[i]);
			g2[a[i]].push_back(i);
		}
		
		int ans = 1;
		
		for(int i = 1; i <= n; i++) {
			bool vis[1005];
			memset(vis, 0, sizeof vis);
			vector <int> st;
			int pos = i;
			while(!vis[pos]) {
				vis[pos] = 1;
				st.push_back(pos);
				pos = a[pos];
			}
			if(a[st.back()] != st[st.size() - 2] && a[st.back()] != st[0])
				continue;

//			for(int j = 0; j < st.size(); j++) printf("%d ", st[j]); printf("\n");
//			for(int j = 1; j <= n; j++) printf("%d ", vis[j]); printf("\n");

			if(a[st.back()] == st[st.size() - 2]) {
				//find other first
				for(int ii = 1; ii <= n; ii++) if(!vis[ii]) {
					bool vis2[1005];
					for(int j = 1; j <= n; j++) vis2[j] = vis[j];
					vector <int> st2;
					pos = ii;
					while(!vis2[pos]) {
						vis2[pos] = 1;
						st2.push_back(pos);
						pos = a[pos];
					}
					if(a[st2.back()] == st2[st2.size() - 2]) 
						ans = max(ans, (int) (st.size() + st2.size()));
				}
				
				//last case
				//bfs from i and st.back() using g2
				queue <int> q, r;
				q.push(i); r.push(0);
				int ma1 = 0, ma2 = 0;
				while(!q.empty()) {
					int qq = q.front();
					int rr = r.front();
					q.pop(); r.pop();
					ma1 = max(ma1, rr);
					for(int j = 0; j < g2[qq].size(); j++) if(!vis[g2[qq][j]]) {
						vis[g2[qq][j]] = 1;
						q.push(g2[qq][j]);
						r.push(rr + 1);
					}
				}
				q.push(st.back()); r.push(0);
				while(!q.empty()) {
					int qq = q.front();
					int rr = r.front();
					q.pop(); r.pop();
					ma2 = max(ma2, rr);
					for(int j = 0; j < g2[qq].size(); j++) if(!vis[g2[qq][j]]) {
						vis[g2[qq][j]] = 1;
						q.push(g2[qq][j]);
						r.push(rr + 1);
					}
				}
				ans = max(ans, (int) st.size() + ma1 + ma2);
			} else ans = max(ans, (int) st.size());
	//		printf("%d %d\n", i, ans);
		}
	//	*/
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}