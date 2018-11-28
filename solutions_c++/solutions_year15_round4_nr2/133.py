#include<bits/stdc++.h>

using namespace std;

typedef pair<int, int> pii;
typedef long long int LL;
typedef vector<int> VI;

#define sd(x) scanf("%d", &x)
#define MP make_pair
#define PB push_back
#define F first
#define S second
#define MOD 1000000007
#define LD long double

typedef long double D;
typedef vector<D> VD;
typedef vector<VD> VVD;

const D EPS = 1e-15;

struct LPSolver {
  int m, n;
  VI B, N;
  VVD D;

  LPSolver(const VVD &A, const VD &b, const VD &c) : 
    m(b.size()), n(c.size()), N(n+1), B(m), D(m+2, VD(n+2)) {
    for (int i = 0; i < m; i++) for (int j = 0; j < n; j++) D[i][j] = A[i][j];
    for (int i = 0; i < m; i++) { B[i] = n+i; D[i][n] = -1; D[i][n+1] = b[i]; }
    for (int j = 0; j < n; j++) { N[j] = j; D[m][j] = -c[j]; }
    N[n] = -1; D[m+1][n] = 1;
  }
	   
  void Pivot(int r, int s) {
    for (int i = 0; i < m+2; i++) if (i != r)
      for (int j = 0; j < n+2; j++) if (j != s)
	D[i][j] -= D[r][j] * D[i][s] / D[r][s];
    for (int j = 0; j < n+2; j++) if (j != s) D[r][j] /= D[r][s];
    for (int i = 0; i < m+2; i++) if (i != r) D[i][s] /= -D[r][s];
    D[r][s] = 1.0 / D[r][s];
    swap(B[r], N[s]);
  }

  bool Simplex(int phase) {
    int x = phase == 1 ? m+1 : m;
    while (true) {
      int s = -1;
      for (int j = 0; j <= n; j++) {
	if (phase == 2 && N[j] == -1) continue;
	if (s == -1 || D[x][j] < D[x][s] || D[x][j] == D[x][s] && N[j] < N[s]) s = j;
      }
      if (D[x][s] >= -EPS) return true;
      int r = -1;
      for (int i = 0; i < m; i++) {
	if (D[i][s] <= 0) continue;
	if (r == -1 || D[i][n+1] / D[i][s] < D[r][n+1] / D[r][s] ||
	    D[i][n+1] / D[i][s] == D[r][n+1] / D[r][s] && B[i] < B[r]) r = i;
      }
      if (r == -1) return false;
      Pivot(r, s);
    }
  }

  bool Solve() {
    int r = 0;
    for (int i = 1; i < m; i++) if (D[i][n+1] < D[r][n+1]) r = i;
    if (D[r][n+1] <= -EPS) {
      Pivot(r, n);
      if (!Simplex(1) || D[m+1][n+1] < -EPS) return false;
    }
    return true;
  }
};

#define N 1123

int n;
D v, x;
D r[N], c[N];

bool pos(double ti){
	VVD a;
	VD b, d;
	int i, j;
	b.resize(4 + n);
	d.resize(n, 0);
	a.resize(4 + n);
	for(i = 0; i < n; i++){
		a[0].PB(c[i]);
	}
	b[0] = v * x;
	for(i = 0; i < n; i++){
		a[1].PB(-c[i]);
	}
	b[1] = -v * x;
	for(i = 0; i < n; i++){
		a[2].PB(1);
	}
	b[2] = v;
	for(i = 0; i < n; i++){
		a[3].PB(-1);
	}
	b[3] = -v;
	for(i = 0; i < n; i++){
		d[i] = 1 / r[i];
		for(j = 0; j < n; j++){
			a[i + 4].PB((j == i ? 1 : 0));
		}
		b[i + 4] = r[i] * ti;
	}
	LPSolver solver(a, b, d);
	return solver.Solve();
}

int main(){
	freopen("B-small-attempt3.in", "r", stdin);
	freopen("bout.txt", "w", stdout);
	int t;
	sd(t);
	for(int cas = 0; cas < t; cas++){
		printf("Case #%d: ", cas + 1);
		cin>>n>>v>>x;
		double rg = 0, lf = 0, m;
		int i;
		for(i = 0; i < n; i++){
			cin>>r[i]>>c[i];
			rg = max(rg, double(v / r[i]));
		}
		if(pos(1123456789) == false){
			cout<<"IMPOSSIBLE"<<endl;
			continue;
		}
		D eps = 1e-9;
		while(rg - lf > eps){
			m = (rg + lf) / 2;
			if(pos(m) == true){
				rg = m;
			}
			else{
				lf = m;
			}
		}
		printf("%0.9f\n", rg);
	}
	return 0;
}

