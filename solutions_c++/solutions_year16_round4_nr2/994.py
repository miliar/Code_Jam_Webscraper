#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <complex>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>

using namespace std;
typedef unsigned int uint;
typedef long int lint;
typedef unsigned long int ulint;
typedef long long int llint;
typedef unsigned long long int ullint;
template<typename T, typename D> inline T coerce_ct(T dummy, D value) { return (T)value; }
template<typename T, typename D> inline T add_ct(T a, D b) { return (T)(a + (T)b); }
template<typename T, typename D> inline T sub_ct(T a, D b) { return (T)(a - (T)b); }
template<typename T, typename D> inline T max_ct(T a, D b) { return a > (T)b ? a : (T)b; }
template<typename T, typename D> inline T min_ct(T a, D b) { return a < (T)b ? a : (T)b; }
template<typename T> T gcd(T a, T b) { while(a) { T tmp = a; a = b % a; b = tmp; } return b; }
template<typename T> T lcm(T a, T b) { return a / gcd(a, b) * b; }
template<typename T> T rscanf(char const *fmt) { T tmp; scanf(fmt, &tmp); return tmp; }
template<typename T, typename D> inline void update(T f(T, D), T &a, D b) { a = f(a, b); }
template<typename T, typename D> T repeat(T a, D b) { T tmp = a; while(--b) tmp += a; return tmp; }
inline char const *reps(string a, int b) { return repeat(a, b).c_str(); }
#define for0(var, limit) for(auto var = coerce_ct(limit, 0); var < (limit); var++)
#define for0r(var, limit) for(auto var = sub_ct(limit, 1); var + 1; var--)
#define fors(var, start, limit) for(auto var = start; var < (limit); var++)
#define forsr(var, start, limit) for(auto var = sub_ct(limit, 1) ; var - (start) + 1; var--)
#define fori(var, obj) for(auto var = (obj).begin(); var != (obj).end(); var++)
#define forir(var, obj) for(auto var = (obj).rbegin(); var != (obj).rend(); var++)
#ifdef DBG
#define DEBUG(X) X
#define track_depth(var) static int var; var++; class depth_sentinel { public: ~depth_sentinel() {var--;} } var##_sentinel
#else
#define DEBUG(X) 0
#define track_depth(var) static int var;
#endif
#define debugf(...) DEBUG(fprintf(stderr,##__VA_ARGS__))
template<typename T, typename ...Ts> T tracef(char const *fmt, T x, Ts... rest) { debugf(fmt, x, &rest...); return x; }
template<typename T, typename D, typename... Ts> D tracef2(char const *fmt, T x, D y, Ts... rest) { debugf(fmt, x, y, &rest...); return y; }

void run_test();

int main(int argc, char *argv[])
{
	int T = rscanf<int>("%d");
	fors(test, 1, T + 1)
	{
		printf("Case #%d: ", test);
		run_test();
	}
}

double votes[200];
int pick[200];
int ipick = 0;

double maxprob(int N, int K, int i)
{
	if(!K)
	{
		double m = 0.0;
		for0(i, 1ULL << ipick)
		{
			double p = 1.0;
			int Z = 0;
			for0(b, ipick)
				if((i >> b) & 1)
				{
					p *= votes[pick[b]];
					Z++;
				}
				else
					p *= 1.0 - votes[pick[b]];
			if(Z * 2 == ipick)
				m += p;
		}
		return m;
	}
	if(i + K > N)
		return 0.0;
	double m = 0.0;
	pick[ipick++] = i;
	m = max(m, maxprob(N, K - 1, i + 1));
	ipick--;
	m = max(m, maxprob(N, K, i + 1));
	return m;
}

void run_test()
{
	int N, K;
	scanf("%d%d", &N, &K);
	for0(i, N)
		scanf("%lf", &votes[i]);
	printf("%.12lg\n", maxprob(N, K, 0));
}
