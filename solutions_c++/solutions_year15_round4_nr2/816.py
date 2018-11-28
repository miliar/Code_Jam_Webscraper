#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <bitset>
#include <numeric>
#include <utility>
#include <iomanip>
#include <algorithm>
#include <functional>
using namespace std;

typedef long long ll;
typedef vector<int> vint;
typedef vector<long long> vll;
typedef pair<int,int> pint;
typedef pair<long long, long long> pll;

#define MP make_pair
#define PB push_back
#define ALL(s) (s).begin(),(s).end()
#define EACH(i, s) for (__typeof__((s).begin()) i = (s).begin(); i != (s).end(); ++i)
#define COUT(x) cout << #x << " = " << (x) << " (L" << __LINE__ << ")" << endl

template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return 1; } return 0; }
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return 1; } return 0; }
template<class T> ostream& operator << (ostream &s, vector<T> P) 
{ for (int i = 0; i < P.size(); ++i) { if (i > 0) { s << " "; } s << P[i]; } return s; }
template<class T> ostream& operator << (ostream &s, vector<vector<T> > P) 
{ for (int i = 0; i < P.size(); ++i) { s << endl << P[i]; } return s << endl; }
template<class T1, class T2> ostream& operator << (ostream &s, map<T1,T2> P) 
{ EACH(it, P) { s << "<" << it->first << "->" << it->second << "> "; } return s; }
template<class T1, class T2> ostream& operator << (ostream &s, pair<T1,T2> P) 
{ return s << '<' << P.first << ", " << P.second << '>'; }

#define MAX 210

int N;
long double V, X;
long double R[MAX], C[MAX];



// 単体法（最小添字規則によるナイーブな2段階単体法）, 有理数ライブラリにも適用可能
// A : n×m行列, n <= mでないと止まらない
// min cx s.t. Ax = b, x >= 0
template<class T> struct Matrix {
    vector<vector<T> > val;
    Matrix(int n = 1, int m = 1) {val.clear(); val.resize(n, vector<T>(m));}
    Matrix(int n, int m, T x) {val.clear(); val.resize(n, vector<T>(m, x));}
    void init(int n, int m, T x = 0) {val.clear(); val.resize(n, vector<T>(m, x));}
    void resize(int n, int m, T x = 0) {val.resize(n); for (int i = 0; i < n; ++i) val[i].resize(m, x);}
    int size() {return val.size();}
    inline vector<T>& operator [] (int i) {return val[i];}
    friend ostream& operator << (ostream& s, Matrix<T> M) {s << endl; 
        for (int i = 0; i < M.val.size(); ++i) s << M[i] << endl; return s;}
};

const long double INF = 1LL<<30;
const long double EPS = 1e-9;
//const frac INF = 1LL<<29;
//const frac EPS = 0;

bool OPT, NON, UNB;
template<class T> pair<T,vector<T> > Simplex(Matrix<T> A, vector<T> b, vector<T> c) {
    OPT = false; NON = false; UNB = false;
	vector<T> kara;
    int n = A.size(), m = A[0].size();
    for (int i = 0; i < n; ++i) if (b[i] < 0) {b[i] *= -1; for (int j = 0; j < m; ++j) A[i][j] *= -1; }
    
    vector<int> base(n), non(m);
    for (int i = 0; i < n; ++i) base[i] = m+i;
    for (int j = 0; j < m; ++j) non[j] = j;
    
    A.resize(n+2, n+m+1);
    for (int i = 0; i < n; ++i) A[i][m+i] = 1, A[i][n+m] = b[i];
    for (int i = 0; i < n; ++i) { A[n][n+m] += A[i][n+m]; for (int j = 0; j < m; ++j) A[n][j] += A[i][j]; }
    for (int j = 0; j < m; ++j) A[n+1][j] = -c[j];
    
    for (int phase = 0; phase < 2; ++phase) {
        while (true) {
            int nn = -1, nb = -1;
			T FMax = -1;
			bool ok = true;
			for (int i = 0; i < non.size(); ++i) {
				if (non[i] >= m) continue;							// We cannot let slack value move to the base
				if (A[n][non[i]] > EPS) { 
					if (nn == -1) nn = i;
					else if (non[i] < non[nn]) nn = i;				// Bland's smallest subscript rule
					//if (chmax(FMax, A[n][non[i]])) nn = i;					// max coefficient rule
				}
			}
            if (nn == -1) {													
				if (phase == 1) break;                              // All done!
                if (A[n][A[0].size()-1] > EPS) {                    // No feasible solution!
                    NON = true; 
                    return make_pair(-1,kara);
                }	
				for (int i = 0; i < base.size(); ++i) {
					if (base[i] >= m) { 
						ok = false; nb = i; break;                  // If base doesn't contain slack, okay
					}
				}
				if (ok) break;									
				for (int i = 0; i < non.size(); ++i) {
					if (non[i] < m && abs(A[nb][non[i]]) > EPS) {
						nn = i; break;								// Continue... (put out slack from base)
					}
				}
				if (nn == -1) break;								// Slack base will be erased (,so okay)
            }   
            int col = non[nn];
            
            if (nb == -1) {
                T min_ratio = INF;
                for (int i = 0; i < base.size(); ++i) if (A[i][col] > EPS) {
                    T tmp = A[i][A[0].size()-1] / A[i][col];
                    if (min_ratio > tmp + EPS) { min_ratio = tmp, nb = i; }
                    else if (min_ratio >= tmp - EPS) {
                        if (nb == -1) nb = i;
                        else if (base[i] < base[nb]) nb = i;        // Bland's smallest subscript rule
                    }
                }
                if (nb == -1) {                                     // It cannot happen at the 1st stage
                    UNB = true; 
                    return make_pair(-1,kara);
                }	
            }
            int row = nb;
            
            T piv = A[row][col];									
            for (int j = 0; j < A[0].size(); ++j) A[row][j] = A[row][j] / piv;
            for (int i = 0; i < A.size(); ++i) {
                if (i == row) continue;
                T pn = A[i][col];
                for (int j = 0; j < A[0].size(); ++j) A[i][j] = A[i][j] - A[row][j] * pn;
            }
            swap(base[nb], non[nn]);
            
            //COUT(phase); COUT(A[n][A[0].size()-1]); 
            //COUT(base); COUT(non); COUT(A); cout << endl;
        }
        
        if (phase == 0) {
            swap(A[n], A[n+1]);
            
			for (int i = 0; i < n; ++i) 
				for (int j = 0; j < A.size(); ++j) 
					A[j].erase(A[j].begin() + m);
			for (int i = 0; i < base.size(); ++i) {                 // base slack can be removed
				if (base[i] >= m) {
					A.val.erase(A.val.begin() + i);
					base.erase(base.begin() + i);
					--i; --n;
				}
			}
			A.val.erase(A.val.end()-1);
            
			for (int i = 0; i < non.size(); ++i) 
				if (non[i] >= m) 
					non.erase(non.begin() + i--);
        }
    }
	
	OPT = true;
    vector<T> res(A[0].size(), 0);
    for (int i = 0; i < base.size(); ++i) res[base[i]] = A[i][A[0].size()-1];
    res.resize(m);                                                 
    
    return make_pair(A[n][A[0].size()-1],res);
}






void solve() {
    cin >> N;
    cin >> V >> X;
    for (int i = 0; i < N; ++i) cin >> R[i] >> C[i];
    
    bool loExist = false, upExist = false;
    for (int i = 0; i < N; ++i) {
        if (C[i] <= X + EPS) loExist = true;
        if (C[i] >= X - EPS) upExist = true;
    }
    if (!loExist || !upExist) {
        puts("IMPOSSIBLE");
        return;
    }
    
    if (N == 1) {
        if ( abs(C[0] - X) < EPS ) {
            long double res = V / R[0];
            cout << fixed << setprecision(9) << res << endl;
            return;
        }
        else {
            puts("IMPOSSIBLE");
            return;
        }
    }
    else if (N == 2) {
        if ( abs(C[0] - C[1]) < EPS ) {
            long double t = V / (R[0] + R[1]);
            cout << fixed << setprecision(9) << t << endl;
            return;
        }
        else {
            long double t1 = V * (X - C[1]) / R[0] / (C[0] - C[1]);
            long double t2 = V * (X - C[0]) / R[1] / (C[1] - C[0]);
            cout << fixed << setprecision(9) << max(t1, t2) << endl;
            return;
        }
    }
    
    //cout << fixed << setprecision(9) << hi << endl;
}

int main() {
    freopen( "/Users/macuser/Dropbox/Contest/B-small-attempt2.in", "r", stdin );
    freopen( "/Users/macuser/Dropbox/Contest/B-small.out", "w", stdout );
    

    int TTT;
    scanf("%d", &TTT);
    for (int XXX = 0; XXX < TTT; ++XXX) {
        printf("Case #%d: ", XXX+1);
        solve();
    }
    
    return 0;
}



