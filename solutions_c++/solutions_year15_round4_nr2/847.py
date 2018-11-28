#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <numeric>
#define INF 1e9
#define EPS 1e-12
#define REP(i,n) for(int i = 0; i < n; ++i)
#define FOR(i,j,m) for (int i = j; i < m; ++i)
#define ALL(b) b.begin(), b.end()
#define ALLOF(b) b.begin(), b.end()

using namespace std;

typedef long double ld;
typedef vector<int> VI;
typedef vector<ld> VD;
typedef vector<VD> mat;
typedef VD vector_t;

void pivot(mat& A, VD& b, int n, int m, int bi, int nv) {
    ld pd = A[bi][nv];
    REP(j, n+m) A[bi][j] /= pd;
    b[bi] /= pd;
    REP(i, m+2) {
        if (i == bi) continue;
        ld pn = A[i][nv];
        REP(j, n+m) A[i][j] -= A[bi][j] * pn;
        b[i] -= b[bi] * pn;
    }
}

void reinvert(mat& A, VD& b, int n, int m, VI& bx) {
    REP(i,m) {
        int mxpivot=i;
        FOR(ii,i+1,m) if (fabsl(A[i][bx[ii]])>fabsl(A[i][bx[mxpivot]])) mxpivot=ii;
        swap(bx[i],bx[mxpivot]);
        pivot(A,b,n,m,i,bx[i]);
    }
}

// Minimizes $cx$, constraints $Ax=b$, $x>=0$
// Try to have rows in $A$ of norm 1
vector_t simplex(mat A, VD b, VD c) {
    const int n = c.size(), m = b.size(); // n vars, m eqs
    // modify b to non-negative
    REP(i, m) if (b[i] < 0) {
        REP(j, n) A[i][j] *= -1;
        b[i] *= -1;
    }
    // list of base/independent variable ids
    vector<int> bx(m), nx(n);
    REP(i, m) bx[i] = n + i; // aux in base
    REP(i, n) nx[i] = i; // real independent
    // extend A, b
    A.resize(m + 2);
    REP(i, m+2) A[i].resize(n + m, 0); // aux vars
    REP(i, m) A[i][n + i] = 1; // aux vars
    REP(i, m) REP(j, n) A[m][j] = A[m][j]+A[i][j]; // row m is phase 0 costs
    b.push_back(accumulate(ALL(b), ld(0))); // row m is phase 0 costs
    REP(j, n) A[m + 1][j] = -c[j]; // row m+1 is costs
    REP(i, m) A[m + 1][n + i] = -INF; // aux costs
    b.push_back(0);
    mat A_(A);
    VD b_(b);
    VI forbidden(n+m,false);
    // main optimization
    REP(phase, 2) {
        for (int nsteps=0;;++nsteps) {
            // select an independent variable to enter
            int ni = -1;
            REP(i, n) if (!forbidden[nx[i]] && A[m][nx[i]] > EPS && (ni < 0 || nx[i] < nx[ni])) ni = i;
            if (ni == -1) break;
            int nv = nx[ni];
            // select a base variable to leave
            vector_t bound(m);
            REP(i, m) bound[i] = (A[i][nv] < EPS ? INF : b[i] / A[i][nv]);
            if (!(*min_element(ALLOF(bound)) < INF)) return vector_t(n,INF); // unbounded
            int bi = 0;
            REP(i, m)
                if (bound[i] < bound[bi] - EPS ||
                    (bound[i] < bound[bi] + EPS && bx[i] < bx[bi])) bi = i;
            // update
            swap(nx[ni], bx[bi]);
            if (false && nsteps%100==0) {
                A=A_;
                b=b_;
                reinvert(A,b,n,m,bx);
            }
            else pivot(A,b,n,m,bi,nv);
        }
        if (phase == 0) {
            if (b[m]>EPS) return vector_t(); // no solution
            REP(i, n+m) if (i>=n || A[m][i] < -EPS) forbidden[i]=true;
            swap(A[m], A[m + 1]);
            swap(b[m], b[m + 1]);
            swap(A_[m], A_[m + 1]);
            swap(b_[m], b_[m + 1]);
        }
    }
    vector_t x(n + m, 0);
    REP(i, m) x[bx[i]] = b[i];
    x.resize(n);
    return x;
}

int t,N;
ld V,X;
VD r,ccc;
VD minu; mat req;

//Simplex :D
int main() {
  cin >> t;
  cout.precision(15);
  cout.setf(ios::fixed);
  for(int cass = 1; cass <= t; ++cass){
    cin >> N >> V >> X;
    r = VD(N);
    ccc = VD(N);
    for(int i = 0; i < N; ++i){
      cin >> r[i] >> ccc[i];
    }
//     for(int i = 0; i < N; ++i){
//       cout << r[i] << ' ' << ccc[i] << endl;
//     }
//     minu = VD(p);
//     req = mat(p,VD(t));
//     for(int i = 0; i < p; ++i){
// 	    cin >> minu[i];
// 	    for(int j = 0; j < t; ++j){
// 		    cin >> req[i][j];
// 	    }
//     }
    int n,m;
//     n = p*t+p; m = p+t;
    n = N+1+N;
    m = 2+N;
    mat A(m, VD(n,0));
    VD b(m,0);
    b[0] = V;
    b[1] = X*V;
    for(int i = 0; i < m; ++i) cerr << b[i] << ' ';
    cerr << endl;
    VD c(n,0); c[N] = 1.;
    for(int i = 0; i < N; ++i){
      A[0][i] = r[i];
      A[1][i] = r[i]*ccc[i];
      A[2+i][i] = -1.;
      A[2+i][i+N+1] = -1.;
    }
    for(int i = 2; i < m; ++i) A[i][N] = 1.;
    for(int j = 0; j < m; ++j){
      for(int i = 0; i < n; ++i){
	cerr << A[j][i] << ' ';
      }
      cerr << endl;
    }
    //Initialize for the simplex
//     for(int i = 0; i < t; ++i) b[i] = 1;
//     for(int i = t; i < p+t; ++i) b[i] = minu[i-t];
//     for(int i = 0; i < p; ++i){
// 	    for(int j = 0; j < t; ++j){
// 		    A[j][j*p+i] = 1./req[i][j];
// 		    A[i+t][j*p+i] = 1.;
// 		    c[j*p+i] = 1.;
// 	    }
// 	    A[i+t][t*p+i] = 1;
//     }

    
    //Calcule the result of the linear problem given by the simplex
    VD res = simplex(A,b,c);
    if(!res.size()) cout << "Case #" << cass << ": IMPOSSIBLE" << endl;
    else{
	    ld z = 0;
	    for(int i = 0; i < n; ++i){
		    z += res[i]*c[i];
	    }
	    cout << "Case #" << cass << ": " << z << endl;
// 	    cout << max(res[0],res[1]) << endl;
// 	    cout << res[0]*r[0] + res[1]*r[1] << ' ' << V << endl;
// 	    if(z < s+EPS) cout << "Test case #" << cass << ": RIGHT" << endl;
// 	    else cout << "Test case #" << cass << ": " << z-s << endl;
    }
  }
}