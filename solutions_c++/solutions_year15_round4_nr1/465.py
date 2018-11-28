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
// #include <cmath>
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
	typedef long double real;
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
int n, m; 
char a[1007][1007];
int dx[256], dy[256];

inline bool chk(int i, int j, int dx, int dy){
	for(int x = i + dx, y = j + dy; x >= 1 && x <= n && y >= 1 && y <= m; x += dx, y += dy) if(a[x][y] != '.') return true;
	return false;
}

int main(){
	dx['^'] = -1; dx['v'] = 1;
	dy['<'] = -1; dy['>'] = 1;
	int T; scanf("%d", &T);
	f(_, 1, T){
		scanf("%d%d", &n, &m);
		f(i, 1, n) scanf("%s", a[i] + 1);
		int ans = 0; bool can = true;
		f(i, 1, n) f(j, 1, m) if(a[i][j] != '.'){
			int x = i, y = j, cdx = dx[a[i][j]], cdy = dy[a[i][j]];
			x += cdx; y += cdy;
			while(x >= 1 && x <= n && y >= 1 && y <= m){
				if(a[x][y] != '.') break; x += cdx; y += cdy;
			}
			// printf("i %d j %d x %d y %d\n", i, j, x, y);
			if(!(x >= 1 && x <= n && y >= 1 && y <= m)){
				++ans;
				if(!(chk(i, j, -1, 0) || chk(i, j, 1, 0) || chk(i, j, 0, 1) || chk(i, j, 0, -1))) can = false;
			}
		}
		// if(n == 1 && m == 1 && a[n][m] != '.') can = false;
		if(can) printf("Case #%d: %d\n", _, ans);
		else printf("Case #%d: IMPOSSIBLE\n", _);
	}
	return 0;
}










