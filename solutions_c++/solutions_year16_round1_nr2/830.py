#include <bits/stdc++.h>
using namespace std;

#define mp(x, y) make_pair((x), (y))

typedef long long ll;

int t;
int n;
vector<int> a[123];
vector<vector<int> > b;

int main()
{
	scanf("%d", &t);
	for(int q=1; q<=t; q++) {
		scanf("%d", &n);
		for(int i=0; i<2*n-1; i++) {
			a[i].clear();
			a[i].resize(n);
			for(int j=0; j<n; j++) scanf("%d", &a[i][j]);
		}
		sort(a, a+2*n-1);
		for(int m=0; m<(1<<(2*n-1)); m++) {
			b.clear();
			for(int j=0, k=m; k>0; j++, k>>=1) {
				if(k&1) b.push_back(a[j]);
			}
			if(b.size()!=n) continue;
			int ok=1;
			for(int i=0; i<n-1; i++) {
				for(int j=0; j<n; j++) {
					if(b[i][j]>=b[i+1][j]) ok=0;
				}
			}
			if(!ok) continue;
			int l=0;
			vector<int> ans;
			ok=1;
			for(int j=0, k=m; ok && j<2*n-1; j++, k>>=1) {
				if(!(k&1)) {
					back:
					vector<int> c;
					for(int i=0; i<n; i++) c.push_back(b[i][l]);
					l++;
					if(c==a[j]) {
						continue;
					}
					else {
						if(ans.size()==0) ans=c;
						else ok=0;
						if(ok) goto back;
					}
				}
			}
			if(ok) {
				printf("Case #%d:", q);
				if(ans.size()==0) {
					for(int i=0; i<n; i++) ans.push_back(b[i][l]);
				}
				for(int i=0; i<n; i++) printf(" %d", ans[i]);
				printf("\n");
				break;
			}
		}
	}

	return 0;
}
