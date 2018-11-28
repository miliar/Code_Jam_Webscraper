#include<cstdio>
#include<vector>

using namespace std;

int main(){
	int T;
	scanf("%d", &T);
	for (int t = 0; t<T; ++t) {
		int n,m;
		scanf("%d %d", &n, &m);
		vector < int > w (m,0);
		vector < vector < int > > v (n, w);
		for (int i = 0; i<n; ++i) {
			for (int j = 0; j<m; ++j) {
				int x;
				scanf("%d", &x);
				v[i][j] = x;
			}
		}
		vector<int> maxx;
		for (int i = 0; i<n; ++i) {
			int maxi = -1;
			for (int j = 0; j<m; ++j) {
				maxi = max(maxi, v[i][j]);
			}
			maxx.push_back(maxi);
		}	
		vector<int> maxy;
		for (int i = 0; i<m; ++i) {
			int maxi = -1;
			for (int j = 0; j<n; ++j) {
				maxi = max(maxi, v[j][i]);
			}
			maxy.push_back(maxi);
		}	
		bool b = true;
		for (int i = 0; i<n; ++i) {
			for (int j = 0; j<m; ++j) {
				if (v[i][j] < maxx[i] && v[i][j] < maxy[j]) {
					b = false;
					break;
				}
			}
			if (!b) break;
		}	
		if (b) printf("Case #%d: YES\n", t+1);
		else printf("Case #%d: NO\n", t+1);
	}		
	return 0;
}
