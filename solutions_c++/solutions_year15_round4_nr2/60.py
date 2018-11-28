#include <cstdio>
#include <cstring>
#include <algorithm>
#define FOR(i,s,e) for (int i=(s); i<(e); i++)
#define FOE(i,s,e) for (int i=(s); i<=(e); i++)
#define FOD(i,s,e) for (int i=(s)-1; i>=(e); i--)
#define CLR(a,x) memset(a, x, sizeof(a))
#define EXP(i,l) for (int i=(l); i; i=qn[i])
#define LLD long long
#define N 600
using namespace std;

void get(int &x){
	int a, b;
	scanf("%d.%d", &a, &b);
	x = a * 10000 + b;
}

int V, X, n;
int r[105], c[105];

double d[N][N];	
int id[N];
const double EPS = 1e-10;
double a[N][N], b[N], obj[N], xx[N];

double Simplex(double a[N][N], double b[N], double c[N], int n, int m, double x[N]){
	++m;
	int r = n, s = m - 1;
	memset(d, 0, sizeof(d));
	for (int i=0; i<n+m; i++) id[i] = i;
	for (int i=0; i<n; i++){
		for (int j=0; j<m-1; j++) d[i][j] = -a[i][j];
		d[i][m - 1] = 1;
		d[i][m] = b[i];
		if (d[r][m] > d[i][m]) r = i;
	}
	for (int j=0; j<m-1; j++) d[n][j] = c[j];
	d[n+1][m-1] = -1;
	while (1){
		double dd;
		if (r < n){
			swap(id[s], id[r+m]);
			d[r][s] = 1. / d[r][s];
			for (int j=0; j<=m; j++) if (j != s) d[r][j] *= -d[r][s];
			for (int i=0; i<=n+1; i++) if (i != r){
				for (int j=0; j<=m; j++) if (j != s) d[i][j] += d[r][j] * d[i][s];
				d[i][s] *= d[r][s];
			}
		}
		r = s = -1;
		for (int j=0; j<m; j++) if (s < 0 || id[s] > id[j]){
			if (d[n+1][j] > EPS || (d[n+1][j] > -EPS && d[n][j] > EPS)) s = j;
		}
		if (s < 0) break;
		for (int i=0; i<n; i++) if (d[i][s] < -EPS){
			double t;
			if (r < 0 || (t = d[r][m] / d[r][s] - d[i][m] / d[i][s]) < -EPS || (t < EPS && id[r+m] > id[i+m])) r = i;
		}
		if (r < 0) return 1e99;
	}
	if (d[n+1][m] < -EPS) return 0. / 0.;
	double ret = 0;
	for (int i=m; i<n+m; i++){
		if (id[i] < m - 1) {
			x[id[i]] = d[i-m][m];
			ret += x[id[i]] * c[id[i]];
		}
	}
	return ret;
}

void solve(int tc){
	scanf("%d", &n); get(V); get(X);
	FOR(i,0,n) get(r[i]), get(c[i]);
	
	int mn = (1 << 30), mx = -1;
	FOR(i,0,n) mn = min(mn, c[i]), mx = max(mx, c[i]);
	
	printf("Case #%d: ", tc);
	if (X < mn || X > mx){
		puts("IMPOSSIBLE");
		return;
	}
	
	CLR(a, 0);
	CLR(b, 0);
	CLR(obj, 0);
	FOR(i,0,n){
		a[i][i] = V * 1. / r[i];
		a[i][n] = -1;
	}
	
	FOR(i,0,n) a[n][i] = 1;
	b[n] = 1;
	FOR(i,0,n) a[n+1][i] = -1;
	b[n+1] = -1;
	
	FOR(i,0,n) a[n+2][i] = c[i] / 10000.;
	b[n+2] = X / 10000.;
	FOR(i,0,n) a[n+3][i] = -c[i] / 10000.;
	b[n+3] = -X / 10000.;
	obj[n] = -1;
	double ret = -Simplex(a, b, obj, n+4, n+1, xx);

	if (ret != ret){
		LLD RR = 0;
		FOR(i,0,n) if (X == c[i]) RR += r[i];
		ret = V * 1. / RR;	
		printf("%.9f\n", ret);
	}
	else printf("%.9f\n", ret);		
}

int main(){
	int tc;
	scanf("%d", &tc);
	FOE(i,1,tc) solve(i);
	return 0;
}
