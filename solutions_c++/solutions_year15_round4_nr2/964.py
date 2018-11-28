// #includes {{{
#include <algorithm>
#include <functional>
#include <numeric>
#include <limits>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <list>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <cmath>
using namespace std;
// }}}
// pre-written code {{{
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define RREP(i,a,b) for(int i=(int)(a);i<(int)(b);++i)
#define FOR(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();++i)
#define LET(x,a) __typeof(a) x(a)
//#define IFOR(i,it,c) for(__typeof((c).begin())it=(c).begin();it!=(c).end();++it,++i)
#define ALL(c) (c).begin(), (c).end()
#define MP make_pair

#define EXIST(e,s) ((s).find(e)!=(s).end())

#define RESET(a) memset((a),0,sizeof(a))
#define SET(a) memset((a),-1,sizeof(a))
#define PB push_back
#define DEC(it,command) __typeof(command) it=command

//const int INF=0x3f3f3f3f;

typedef long long Int;
typedef unsigned long long uInt;
#ifdef __MINGW32__
typedef double rn;
#else
typedef double rn;
#endif

typedef pair<int,int> pii;

/*
#ifdef MYDEBUG
#include"debug.h"
#include"print.h"
#endif
*/
// }}}

const double EPS = 1.0e-10;
const double INF = numeric_limits<double>::infinity();

typedef vector<double> vector_t;
typedef vector<vector_t> matrix_t;

vector_t simplex(matrix_t A, vector_t b, vector_t c) {

	const int n = c.size(), m = b.size();

	// modify b to non-negative
	REP(i, m) if (b[i] < 0) {
		REP(j, n)
			A[i][j] *= -1;
		b[i] *= -1;
	}

	// list of base/independent variable ids
	vector<int> bx(m), nx(n);
	REP(i, m)
		bx[i] = n+i;
	REP(i, n)
		nx[i] = i;

	// extend A, b
	A.resize(m+2);
	REP(i, m+2)
		A[i].resize(n+m, 0);
	REP(i, m)
		A[i][n+i] = 1;
	REP(i, m) REP(j, n)
		A[m][j] += A[i][j];
	b.push_back(accumulate(ALL(b), (double)0.0));
	REP(j, n)
		A[m+1][j] = -c[j];
	REP(i, m)
		A[m+1][n+i] = -INF;
	b.push_back(0);

	// main optimization
	REP(phase, 2) {

		for(;;) {

			// select an independent variable
			int ni = -1;
			REP(i, n)
				if (A[m][nx[i]] > EPS && (ni < 0 || nx[i] < nx[ni]))
					ni = i;
			if (ni < 0)
				break;

			int nv = nx[ni];

			// select a base variable
			vector_t bound(m);
			REP(i, m)
				bound[i] = (A[i][nv] < EPS ? INF : b[i] / A[i][nv]);
			if (!(*min_element(ALL(bound)) < INF))
				return vector_t(); // -infinity

			int bi = 0;
			REP(i, m)
				if (bound[i] < bound[bi]-EPS || (bound[i] < bound[bi]+EPS && bx[i] < bx[bi]))
					bi = i;

			// pivot
			double pd = A[bi][nv];
			REP(j, n+m)
				A[bi][j] /= pd;
			b[bi] /= pd;

			REP(i, m+2) if (i != bi) {
				double pn = A[i][nv];
				REP(j, n+m)
					A[i][j] -= A[bi][j] * pn;
				b[i] -= b[bi] * pn;
			}

			swap(nx[ni], bx[bi]);
		}

		if (phase == 0 && abs(b[m]) > EPS)
			return vector_t(); // no solution

		A[m].swap(A[m+1]);
		swap(b[m], b[m+1]);
	}

	vector_t x(n+m, 0);
	REP(i, m)
		x[bx[i]] = b[i];
	x.resize(n);

	return x;
}

/*
   int main() {
   for (int n, m; cin >> n >> m; ) {
   array c(n+m), b(m);
   for (int i = 0; i < n; ++i)
   cin >> c[i], c[i] *= -1;
   matrix A(m, array(n+m));
   for (int i = 0; i < m; ++i) {
   for (int j = 0; j < n; ++j)
   cin >> A[i][j];
   A[i][n+i] = 1;
   cin >> b[i];
   }
   two_stage_simplex tss(A, b, c);
   rn ans = -tss.solution() * m;
   printf("Nasa can spend %.0f taka.\n", ans + 0.5 - EPS);
   }
   }
   */

int N;
rn V,X;
rn R[110], C[110];

//matrix A;
//array b,c;

void main2(){
	cin>>N>>V>>X;
	REP(i,N)cin>>R[i]>>C[i];
	rn cmax = -numeric_limits<double>::infinity();
	rn cmin = numeric_limits<double>::infinity();
	REP(i,N){
		cmax = max(cmax,C[i]);
		cmin = min(cmin,C[i]);
	}
	if(X<cmin-EPS or cmax+EPS<X){
		cout<<"IMPOSSIBLE"<<endl;
		return;
	}
	if(abs(X-cmin)<EPS){
		rn v0 = 0.0L;
		REP(i,N)if(abs(C[i]-cmin)<EPS)v0+=R[i];
		printf("%.10lf\n",V/v0);
		return;
	}
	if(abs(X-cmax)<EPS){
		rn v0 = 0.0L;
		REP(i,N)if(abs(C[i]-cmax)<EPS)v0+=R[i];
		printf("%.10lf\n",V/v0);
		return;
	}

	matrix_t A(N+1,vector_t(N*2));
	vector_t b(N+1),c(N*2);
	REP(i,N)A[0][i]=R[i]*C[i]-R[i]*X;
	REP(i,N)A[i+1][i]=A[i+1][N+i]=1.0L;
	b[0]=0.0L;
	REP(i,N)b[i+1]=1.0L;
	REP(i,N)c[i]=-R[i]*C[i];
	vector<rn> x = simplex(A,b,c);
	if(x.size()==0){
		cout<<"IMPOSSIBLE"<<endl;
	}

	rn ps = 0.0L;
	REP(i,N){
		ps += x[i]*R[i];
//		cout<<x[i]<<" ";
	}
//	cout<<endl;
	printf("%.10lf\n",V/ps);
}

// main function {{{
int main() {
	int T;cin>>T;
	REP(ct, T){
		cout<<"Case #"<<ct+1<<": ";
		main2();
	}
	return 0;
}
//}}}
