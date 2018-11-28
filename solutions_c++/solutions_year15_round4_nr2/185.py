#include <iostream>
#include <iomanip>
#include <cstring>
#include <algorithm>

using namespace std;
typedef long double ld;
const int MAXM = 200;
const int MAXN = 200;
const ld EPS = 1e-10;
const ld INF = 1e20;


void pivot(int m,int n,ld a[MAXM][MAXN],
           int B[MAXM],int N[MAXN],int r,int c) {
  int i,j; swap(N[c], B[r]); a[r][c]=1/a[r][c];
  for(j=0;j<=n;j++) if(j!=c) a[r][j]*=a[r][c];
  for(i=0;i<=m;i++) if(i!=r) {
    for(j=0;j<=n;j++) if(j!=c) a[i][j]-=a[i][c]*a[r][j];
    a[i][c] = -a[i][c]*a[r][c]; } }
int feasible(int m,int n,ld a[MAXM][MAXN],int B[MAXM],int N[MAXN]) {
  int r,c,i; ld p,v;
  while(1) {
    for(p=INF,i=0; i<m; i++) if(a[i][n]<p) p=a[r=i][n];
    if(p>-EPS) return 1;
    for(p=0,i=0; i<n; i++) if(a[r][i]<p) p=a[r][c=i];
    if(p>-EPS) return 0;
    p = a[r][n]/a[r][c];
    for(i=r+1; i<m; i++) if(a[i][c]>EPS) {
      v = a[i][n]/a[i][c];
      if(v<p) r=i,p=v; }
    pivot(m,n,a,B,N,r,c); } }
int simplex(int m,int n,ld a[MAXM][MAXN],ld b[MAXN],ld& ret) {
	/*
	cerr << "calling simplex: " << endl;
	for (int i = 0; i < m+1; i++) {
		for (int j = 0; j < n+1; j++) {
			cerr << a[i][j] << ' ';
		}
		cerr << endl;
	}
	*/
  int B[MAXM],N[MAXN],r,c,i; ld p,v;
  for(i=0; i<n; i++) N[i]=i;
  for(i=0; i<m; i++) B[i]=n+i;
  if(!feasible(m,n,a,B,N)) return 0;
  while(1) {
    for(p=0,i=0; i<n; i++) if(a[m][i]>p) p=a[m][c=i];
    if(p<EPS) {
      for(i=0; i<n; i++) if(N[i]<n) b[N[i]]=0;
      for(i=0; i<m; i++) if(B[i]<n) b[B[i]]=a[i][n];
      ret = -a[m][n];
      return 1; }
    for(p=INF,i=0; i<m; i++) if(a[i][c]>EPS) {
      v = a[i][n]/a[i][c];
      if(v<p) p=v,r=i; }
    if(p==INF) return -1;
    pivot(m,n,a,B,N,r,c); } }

int main() {
	int ncase; cin >> ncase;
	for (int cs = 1; cs <= ncase; cs++) {
		int n; ld v, x;
		cin >> n >> v >> x;
		ld rates[n], temps[n];
		for (int i = 0; i < n; i++) {
			cin >> rates[i] >> temps[i];
		}

		ld mat[MAXM][MAXN];
		ld b[MAXM];
		memset(mat, 0, sizeof mat);
		memset(b, 0, sizeof b);
		for (int i = 0; i < n; i++) {
			if (rates[i] == 0) mat[i][i] = INF;
			else mat[i][i] = 1/rates[i];
			mat[i][n] = -1;
			// rhs
			mat[i][n+1] = 0;
		}
		for (int i = 0; i < n; i++) {
			mat[n][i] = temps[i];
			mat[n+1][i] = -temps[i];
			mat[n+2][i] = 1;
			mat[n+3][i] = -1;
		}
		// rhs
		mat[n][n+1] = v*x;
		mat[n+1][n+1] = -v*x;
		mat[n+2][n+1] = v;
		mat[n+3][n+1] = -v;

		mat[n+4][n] = -1;

		ld res;
		int res2 = simplex(n+4, n+1, mat, b, res);

		/*
		cerr << "Result: "<< endl;
			for (int i = 0; i <= n; i++) {
				cerr << b[i] << ' ';
			} cerr << endl;
			*/

		cout << "Case #" << cs << ": ";
		if (res2 == 1) {
			cout << setprecision(16) << fixed << -res;
		} else {
			cout << "IMPOSSIBLE";
		}
		cout << endl;
	}
}
