#include<cstdio>
#include<cstring>
#include<vector>
#include<string>
#include<cassert>
#include<cstdlib>


using namespace std;

const int maxn = 113;
int a[maxn][maxn];
int v[maxn][maxn];
int main() {
	vector<string> res;
	res.push_back("NO");
	res.push_back("YES");
	int _; scanf("%d", &_);
	for (int test = 1; test <= _; test++) {
		int n, m; scanf("%d%d", &n, &m);
		int ok = 1;
		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++)
				scanf("%d", &a[i][j]);
		for (int h = 1; h <= 100 && ok; h++) {
			for (int i = 0; i < n; i++)
				for (int j = 0; j < m; j++)
					v[i][j] = 0;
			for (int i = 0; i < n; i++) {
				int go = 1;
				for (int j = 0; j < m; j++) 
					go &= a[i][j] <= h;
				if (go)
					for (int j = 0; j < m; j++)
						v[i][j] = 1;
			}
			for (int j = 0; j < m; j++) {
				int go = 1;
				for (int i = 0; i < n; i++)
					go &= a[i][j] <= h;
				if (go)
					for (int i = 0; i < n; i++)
						v[i][j] = 1;
			}
			for (int i = 0; i < n; i++)
				for (int j = 0; j < m; j++)
				   if (a[i][j] <= h) ok &= v[i][j];	
		}
		printf("Case #%d: %s\n", test, res[ok].c_str());
	}
	return 0;
}
