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
#include <string>
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

using std::string;
std::map<string, int> _hash; int thash;

inline int hash(string x){
	int &t = _hash[x];
	if(!t) t = ++thash;
	return t;
}

char buf[23333];
std::set<int> S[233], s1, s2;
bool eng[233];

int main(){
	int T; scanf("%d", &T);
	f(_, 1, T){
		_hash.clear(); thash = 0;
		int n; scanf("%d", &n); gets(buf);
		f(i, 1, n){
			memset(buf, 0, sizeof(buf));
			gets(buf); buf[strlen(buf)] = ' ';
			char *cb = buf;
			S[i].clear();
			while(*cb){
				char *tb = cb;
				while(*tb != ' ') ++tb; *tb = 0;
				S[i].insert(hash(cb));
				cb = tb + 1;
			}
		}
		eng[1] = 1; eng[2] = 0;
		int ans = 123456;
		g(st, 0, (1 << (n - 2))){
			f(i, 3, n) eng[i] = (st >> (i - 3) & 1);
			s1.clear(); s2.clear();
			f(i, 1, n) if(eng[i]) s1.insert(S[i].begin(), S[i].end()); else s2.insert(S[i].begin(), S[i].end());
			int c = 0;
			foreach(it, s1) c += s2.count(*it);
			ans = std::min(ans, c);
		}
		printf("Case #%d: %d\n", _, ans);
	}
	return 0;
}










