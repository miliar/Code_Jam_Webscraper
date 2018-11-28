// #pragma GCC optimize(3)
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <iostream>
#include <cmath>
#include <ctime>
#define f(x, y, z) for(int x = (y); x <= (z); ++x)
#define g(x, y, z) for(int x = (y); x < (z); ++x)
#define h(x, y, z) for(int x = (y); x >= (z); --x)
#define foreach(x, y) for(__typeof(y.begin()) x = y.begin(); x != y.end(); ++x)
#define rforeach(x, y) for(__typeof(y.rbegin()) x = y.rbegin(); x != y.rend(); ++x)
#define FILL(x, y) memset(x, y, sizeof(x))
#define COPY(x, y) memcpy(x, y, sizeof(x))
namespace orz{
	typedef long long LL;
	typedef unsigned long long ULL;
	typedef std::pair<int, int> PII;
	// typedef long double real;
	typedef std::vector<int> VI;
	inline void read(int &x){scanf("%d", &x);}
	inline void read(unsigned int &x){scanf("%u", &x);}
	inline void read(LL &x){scanf("%I64d", &x);}
	inline void read(ULL &x){scanf("%I64u", &x);}
	inline void read(double &x){scanf("%lf", &x);}
	inline void read(long double &x){
		double tmp; read(tmp); x = tmp;
	}
	inline void read(char &x){x = getchar();}
	inline void read(char *x){scanf("%s", x);}
	template <class T>
	inline void read(T *a, int n){
		g(i, 0, n) read(a[i]);
	}
	template <class T1, class T2>
	inline void read(T1 &a, T2 &b){
		read(a); read(b);
	}
	template <class T1, class T2, class T3>
	inline void read(T1 &a, T2 &b, T3 &c){
		read(a); read(b); read(c);
	}
	template <class T1, class T2, class T3, class T4>
	inline void read(T1 &a, T2 &b, T3 &c, T4 &d){
		read(a); read(b); read(c); read(d);
	}
	template <class T1, class T2, class T3, class T4, class T5>
	inline void read(T1 &a, T2 &b, T3 &c, T4 &d, T5 &e){
		read(a); read(b); read(c); read(d); read(e);
	}
	inline void write(int x){printf("%d", x);}
	inline void write(unsigned int x){printf("%u", x);}
	inline void write(LL x){printf("%I64d", x);}
	inline void write(ULL x){printf("%I64u", x);}
	inline void write(double x){printf("%.10lf", x);}
	inline void write(long double x){printf("%.10lf", (double) x);}
	inline void write(char x){putchar(x);}
	inline void write(char *x){printf("%s", x);}
	template <class T>
	inline void writes(T x){write(x); putchar(' ');}
	template <class T1, class T2>
	inline void writes(T1 a, T2 b){
		writes(a); writes(b);
	}
	template <class T1, class T2, class T3>
	inline void writes(T1 a, T2 b, T3 c){
		writes(a); writes(b); writes(c);
	}
	template <class T1, class T2, class T3, class T4>
	inline void writes(T1 a, T2 b, T3 c, T4 d){
		writes(a); writes(b); writes(c); writes(d);
	}
	template <class T1, class T2, class T3, class T4, class T5>
	inline void writes(T1 a, T2 b, T3 c, T4 d, T5 e){
		writes(a); writes(b); writes(c); writes(d); writes(e);
	}
	template <class T1, class T2>
	inline void writesln(T1 a, T2 b){
		writes(a); writes(b); putchar('\n');
	}
	template <class T1, class T2, class T3>
	inline void writesln(T1 a, T2 b, T3 c){
		writes(a); writes(b); writes(c); putchar('\n');
	}
	template <class T1, class T2, class T3, class T4>
	inline void writesln(T1 a, T2 b, T3 c, T4 d){
		writes(a); writes(b); writes(c); writes(d); putchar('\n');
	}
	template <class T1, class T2, class T3, class T4, class T5>
	inline void writesln(T1 a, T2 b, T3 c, T4 d, T5 e){
		writes(a); writes(b); writes(c); writes(d); writes(e); putchar('\n');
	}
	template <class T1, class T2>
	inline void writeln(T1 a, T2 b){
		write(a); write(b); putchar('\n');
	}
	template <class T1, class T2, class T3>
	inline void writeln(T1 a, T2 b, T3 c){
		write(a); write(b); write(c); putchar('\n');
	}
	template <class T1, class T2, class T3, class T4>
	inline void writeln(T1 a, T2 b, T3 c, T4 d){
		write(a); write(b); write(c); write(d); putchar('\n');
	}
	template <class T1, class T2, class T3, class T4, class T5>
	inline void writeln(T1 a, T2 b, T3 c, T4 d, T5 e){
		write(a); write(b); write(c); write(d); write(e); putchar('\n');
	}
	template <class T1, class T2>
	inline void write(T1 a, T2 b){
		write(a); write(b);
	}
	template <class T1, class T2, class T3>
	inline void write(T1 a, T2 b, T3 c){
		write(a); write(b); write(c);
	}
	template <class T1, class T2, class T3, class T4>
	inline void write(T1 a, T2 b, T3 c, T4 d){
		write(a); write(b); write(c); write(d);
	}
	template <class T1, class T2, class T3, class T4, class T5>
	inline void write(T1 a, T2 b, T3 c, T4 d, T5 e){
		write(a); write(b); write(c); write(d); write(e);
	}
	template <class T>
	inline void writeln(T x){write(x); putchar('\n');}
	template <class T>
	inline void writeln(T *a, int n){
		g(i, 0, n) write(a[i]); putchar('\n');
	}
	template <class T>
	inline void writesln(T *a, int n){
		g(i, 0, n) writes(a[i]); putchar('\n');
	}
	template <class T>
	inline void writelnln(T *a, int n){
		g(i, 0, n) writeln(a[i]);
	}
}
using namespace orz;

typedef double real;
// #define double long double

int n;
double R[1007], C[1007];
const double INF = 1e101;

inline double get(double V, double X, double R1, double C1, double R2, double C2){
	if(fabs(X - C1) <= 1e-8 && fabs(X - C2) <= 1e-8) return V / (R1 + R2);
	C1 = R1 * C1 / (V * X);
	C2 = R2 * C2 / (V * X);
	R1 /= V; R2 /= V;
	// printf("delta %.20lf\n", fabs(C2 * R1 - C1 * R2));
	// if(fabs(C2 * R1 - C1 * R2) <= 1e-16) return INF;
	double x1 = (C2 - R2) / (C2 * R1 - C1 * R2);
	double x2 = (C1 - R1) / (C1 * R2 - C2 * R1);
	// printf("x %.20lf %.20lf\n", x1, x2);
	// if(x1 < -1 || x2 < -1) return INF; else
	return std::max(x1, x2);
}

inline double get2(double V, double X, double R, double C){
	if(fabs(X - C) > 1e-8) return INF; else return V / R;
}

int main(){
	int T; scanf("%d", &T);
	f(_, 1, T){
		double V, X;
		read(n, V, X);
		// scanf("%d%lf%lf", &n, &V, &X);
		f(i, 1, n) read(R[i], C[i]);
		// f(i, 1, n) scanf("%lf%lf", R + i, C + i);
		double ans = 1e100;
		f(i, 1, n) f(j, i + 1, n) if((C[i] - X) * (C[j] - X) <= 1e-12) ans = std::min(ans, get(V, X, R[i], C[i], R[j], C[j]));
		f(i, 1, n) ans = std::min(ans, get2(V, X, R[i], C[i]));
		if(ans >= 1e99) printf("Case #%d: IMPOSSIBLE\n", _); else printf("Case #%d: %.20lf\n", _, (real) ans);
	}
	return 0;
}










