#include <fstream>
#include <iostream>
#include <sstream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <numeric>
#include <string>
#include <map>
#include <ctime>
#include <bitset>
#include <queue>
#include <unordered_set>

using namespace std;

#ifdef __GNUC__
#define ffs32(x) __builtin_ffs(x) // 1 + index of least 1-bit, 0 for 0
#define clz32(x) ((x) ? __builtin_clz(x) : 32) // leading 0s, undef for 0
#define ctz32(x) ((x) ? __builtin_ctz(x) : 32) // trailing 0s, undef for 0
#define pop32(x) __builtin_popcount(x) // number of 1s`
#define ffs64(x) __builtin_ffsll(x)
#define clz64(x) ((x) ? __builtin_clzll(x) : 64)
#define ctz64(x) ((x) ? __builtin_ctzll(x) : 64)
#define pop64(x) __builtin_popcountll(x)
#elif defined(_WIN32)
#include <intrin.h>
static int __inline clz32(unsigned int x) { unsigned long r = 0; return _BitScanReverse(&r, x) ? 31-r : 32; }
static int __inline ctz32(unsigned int x) { unsigned long r = 0; return _BitScanForward(&r, x) ? r : 32; }
static int __inline ffs32(unsigned int x) { unsigned long r = 0; return _BitScanForward(&r, x) ? r+1 : 0; }
#define pop32(x) ((int)__popcnt(x))
# ifdef _WIN64
static int __inline clz64(unsigned long long x) { unsigned long r = 0; return _BitScanReverse64(&r, x) ? 63-r : 64; }
static int __inline ctz64(unsigned long long x) { unsigned long r = 0; return _BitScanForward64(&r, x) ? r : 64; }
static int __inline ffs64(unsigned long long x) { unsigned long r = 0; return _BitScanForward64(&r, x) ? r+1 : 0; }
# define pop64(x) ((int)__popcnt64(x))
# else
static int __inline clz64(unsigned long long x) {
	int r = clz32(x >> 32);
	return (r == 32) ? 32 + clz32(x & 0xffffffff) : r;
}
static int __inline ctz64(unsigned long long x) {
	int r = ctz32(x & 0xffffffff);
	return (r == 32) ? 32 + ctz32(x >> 32) : r;
}
static int __inline ffs64(unsigned long long x) { int r = ctz64(x); return r == 64 ? 0 : r+1; }
static int __inline pop64(unsigned long long x) { return pop32(x & 0xffffffff) + pop32(x >> 32); }
# endif
#endif

#define countof(_Array) int((sizeof(_Array) / sizeof(_Array[0])))
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef long long i64;
typedef pair<i64, i64> pi64;
typedef vector<i64> vi64;
typedef vector<vi64> vvi64;
typedef vector<pi64> vpi64;
typedef double D;

#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()
#define sortall(x) sort(all(x))
#define sqr(x) ((x) * (x))
#define memfill(x,y) memset(x,y,sizeof(x))

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define foreach(i, x) for (auto i = begin(x); i != end(x); ++i)

#define MOD 1000000007

template<class T>
vector<T> splitstr(const string &s)
{
	istringstream in(s);
	vector<T> out;
	copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(out));
	return out;
}

template<class T>
string joinstr(const vector<T> &v)
{
	ostringstream out;
	copy(v.begin(), v.end(), ostream_iterator<T>(out, " "));
	return out.str();
}

template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template<class T> T abs(T x) { return x > 0 ? x : -x; }

static void redirect(int argc, const char **argv)
{
	if (argc > 1) {
		if (freopen(argv[1], "r", stdin) == NULL) throw "failed to open input file";
	}
	if (argc > 2) {
		if (freopen(argv[2], "w", stdout) == NULL) throw "failed to open output file";
	}
}

void scanline(string & s, int limit)
{
	char buf[limit];
restart:
	if (fgets(buf, limit, stdin) == NULL) throw "read string";
	size_t l = strlen(buf);
	while (l > 0 && isspace(buf[l-1])) --l;
	if (l == 0) goto restart;
	s.assign(buf, l);
}


///////////////////////////////////////////////////////////////////////////////

int M, N;
vector<vector<i64>> hh;
vvi servers;
int maxCount;
int nCount;

void shash(string & s, vector<i64> & v)
{
	i64 h = 0;
	int size = sz(s);
	v.pb(h);
	forn (i, size) {
		h = h * 27 + (s[i]-'A'+1);
		v.pb(h);
	}
	sort(all(v));
}

int count_server(vi & hi)
{
	int nj = sz(hi);
	unordered_set<i64> us;
	forn (j, nj) {
		int jj = hi[j];
		foreach (it, hh[jj]) {
			us.insert(*it);
		}
	}
	return us.size();
}

int count()
{
	int cnt = 0;
	forn (i, N) {
		cnt += count_server(servers[i]);
	}
	return cnt;
}

void rec(int depth)
{
	if (depth == M) {
		int cnt = count();
		if (maxCount < cnt) {
			maxCount = cnt;
			nCount = 1;
		} else if (maxCount == cnt) {
			++nCount;
		}
		return;
	}
	forn (i, N) {
		servers[i].pb(depth);
		rec(depth+1);
		servers[i].pop_back();
	}
}

int main(int argc, const char **argv)
{
	try {
		redirect(argc, argv);
		int nCases;
		if (scanf("%d", &nCases) != 1) throw "read nCases";
		forn (iCase, nCases) {
			if (scanf("%d %d", &M, &N) != 2) throw "read M N";
			hh.clear();
			hh.resize(M);
			forn (i, M) {
				string s;
				scanline(s, 200);
				shash(s, hh[i]);
			}
			servers.clear();
			servers.resize(N);
			maxCount = 0;
			nCount = 0;
			rec(0);
			printf("Case #%d: ", iCase+1);
			printf("%d %d\n", maxCount, nCount);
			fflush(stdout);
			fprintf(stderr, "Time elapsed: %d/%d: %.6f sec\n", iCase+1, nCases, (double)clock () / CLOCKS_PER_SEC);
		}
	} catch (exception& e) {
		fprintf(stderr, "exception: %s\n", e.what());
	} catch (const char* s) {
		fprintf(stderr, "exception: %s\n", s);
	}
	fprintf(stderr, "Time elapsed: %.6f sec\n", (double)clock () / CLOCKS_PER_SEC);
}

/* vim: set ts=4 sw=4 noet: */
