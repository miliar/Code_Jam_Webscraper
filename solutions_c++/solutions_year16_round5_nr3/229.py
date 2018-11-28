#include <bits/stdc++.h>
using namespace std;
#define fo(i,a,b) for (int i = (a); i < (b); i++)
typedef long double ld;
#define N 1234

int tc;
int n, ss, x[N], y[N], z[N], _a;
ld dst[N][N], d[N];
char s[N];
int main() {
	scanf("%d", &tc);
	fo(_,1,tc+1) {
		printf("Case #%d: ", _);
		scanf("%d %d", &n, &ss);
		fo(i,0,n) {
			scanf("%d %d %d", x+i, y+i, z+i);
			fo(j,0,3) scanf("%d", &_a);
		}
		fo(i,0,n) fo(j,i+1,n) dst[i][j] = dst[j][i] = (ld)sqrt((x[i]-x[j])*(x[i]-x[j]) + (y[i]-y[j])*(y[i]-y[j]) + (z[i]-z[j])*(z[i]-z[j]));
		fo(i,0,n) d[i] = 1e18;
		fo(i,0,n) s[i] = 0;
		d[0] = 0;
		fo(i,0,n) {
			int bst = -1;
			fo(j,0,n) if (!s[j] && (bst==-1 || d[j] < d[bst])) bst = j;
			s[bst] = 1;
			fo(j,0,n) if (!s[j]) d[j] = min(d[j], max(d[bst], dst[bst][j]));
		}
		printf("%.9Lf\n", d[1]);
	}

	return 0;
}