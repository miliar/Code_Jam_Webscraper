#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<vector>
using namespace std;

int M[1000][1000];
vector <int> B[1000]; // *
bool U[2][110]; // *
int t, n, m;

int main() {
	scanf ("%d", &t);
	int caze = 0;
	while (t --) {
		caze ++;
		
		scanf ("%d%d", &n, &m);
		for (int i = 0; i < n; i ++) {
			for (int j = 0; j < m; j ++) {
				scanf ("%d", &M[i][j]);
				B[M[i][j]].push_back (i);
				B[M[i][j]].push_back (j);
			}
		}
		
		bool ans = true;
		for (int i = 100; i >= 0; i --) {
			for (int j = 0, f = B[i].size(); j < f; j += 2) {
				if (U[0][B[i][j]] and U[1][B[i][j+1]])
					ans = false;
			}
			if (!ans)
				break;
			
			for (int j = 0, f = B[i].size(); j < f; j += 2) {
				U[0][B[i][j]] = true;
				U[1][B[i][j+1]] = true;
			}
		}
		
		if (ans)
			printf ("Case #%d: YES\n", caze);
		else
			printf ("Case #%d: NO\n", caze);
			
		memset (U, false, sizeof U);
		for (int i = 0; i < 111; i ++) {
			B[i].clear ();
		}
	}
	return 0;
}
