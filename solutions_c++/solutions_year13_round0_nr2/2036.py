#include <bits/stdc++.h>
#define fr(i,a,b) for (int i = (a); i < (b); ++i)
using namespace std;

int in[105][105];
int aux[105][105];
int maxR[105], maxC[105];

int main() {
	int nt, n, m;
	scanf("%d", &nt); ++nt;
	fr(_,1,nt) {
		scanf("%d %d", &n, &m);
		fr(i,0,n) {
			maxR[i] = 0;
			fr(j,0,m) {
				scanf("%d", &in[i][j]);
				maxR[i] = max(maxR[i], in[i][j]);
			}
		}
		
		fr(j,0,m) {
			maxC[j] = 0;
			fr(i,0,n) {
				aux[i][j] = 100;
				maxC[j] = max(maxC[j], in[i][j]);
			}
		}
		
		fr(i,0,n) {
			fr(j,0,m) {
				aux[i][j] = min(aux[i][j], min(maxR[i], maxC[j]));
			}
		}
		
		bool yes = true;
		fr(i,0,n) {
			fr(j,0,m) {
				if (aux[i][j] != in[i][j]) {
					yes = false;
					break;
				}
			}
		}
		
		printf("Case #%d: %s\n", _, yes ? "YES" : "NO");
		
	}
	return 0;
}
