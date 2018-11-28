#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int n,m,t,tes,i,ans,maxx,a[10];
string s[10];

void DFS(int pos) {
	int i,j,k;

	if (pos == n + 1) {
		vector<string> tmp[10];
	
		for (i = 1; i <= n; i++) {
			tmp[a[i]].push_back(s[i]);
		}
	
		for (i = 1; i <= m; i++) if (tmp[i].size() == 0) return;
		
		int maxxx = 0;
		
		for (i = 1 ; i <= m; i++) sort(tmp[i].begin(),tmp[i].end());
		
		for (i = 1 ; i <= m; i++) {
			maxxx += tmp[i][0].length();
			for (j = 1; j < tmp[i].size(); j++) {
				bool sama = true;
				
				for (k = 0; k < tmp[i][j].length(); k++) {
					if (tmp[i][j][k] != tmp[i][j-1][k]) sama = false;
					if (!sama) maxxx++;
				}
			}
		}
	
		if (maxxx > maxx) {
			maxx = maxxx;
			ans = 1;
		} else if (maxxx == maxx) {
			ans++;
		}
	
		return;
	}
	
	for (i = 1; i <= m; i++) {
		a[pos] = i;
		DFS(pos+1);
	}
}

int main() {
	scanf("%d",&t);
	for (tes=1 ; tes<=t ; tes++) {
		scanf("%d%d",&n,&m);
		for (i=1 ; i<=n ; i++) cin >> s[i];
		
		ans = 0;
		maxx = 0;
		DFS(1);
		
		printf("Case #%d: %d %d\n",tes,maxx+m,ans);
	}
}