#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <cstring>
#include <numeric>
#include <algorithm>
#include <functional>
#include <array>
#include <map>
#include <queue>
#include <limits.h>
#include <set>
#include <stack>
#include <random>
#include <complex>
#include <unordered_map>
#include <unordered_set>
#define rep(i,s,n) for(int i = (s); (n) > i; i++)
#define REP(i,n) rep(i,0,n)
#define RANGE(x,a,b) ((a) <= (x) && (x) <= (b))
#define DUPLE(a,b,c,d) (RANGE(a,c,d) || RANGE(b,c,d) || RANGE(c,a,b) || RANGE(d,a,b))
#define INCLU(a,b,c,d) (RANGE(a,c,d) && (b,c,d))
#define PW(x) ((x)*(x))
#define ALL(x) (x).begin(), (x).end()
#define RALL(x) (x).rbegin(), (x).rend()
#define MODU 1000000007
#define bitcheck(a,b)   ((a >> b) & 1)
#define bitset(a,b)      ( a |= (1 << b))
#define bitunset(a,b)    (a &= ~(1 << b))
#define MP(a,b) make_pair((a),(b))
#define Manh(a,b) (abs((a).first-(b).first) + abs((a).second - ((b).second))
#define pritnf printf
#define scnaf scanf
#define itn int
#define PI 3.141592653589


#define izryt bool

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
template<typename A, size_t N, typename T>
void Fill(A(&array)[N], const T &val) {
	std::fill((T*)array, (T*)(array + N), val);
}
struct UnionFind {
	vector<int> data;
	UnionFind(int size) : data(size, -1) { }
	bool unionSet(int x, int y) { //‚˜‚Ì“ü‚Á‚Ä‚éW‡‚Æ y‚Ì“ü‚Á‚Ä‚éW‡‚ğ•¹‡
		x = root(x); y = root(y);
		if (x != y) {
			if (data[y] < data[x]) swap(x, y);
			data[x] += data[y]; data[y] = x;
		}
		return x != y;
	}
	bool findSet(int x, int y) { //x‚Æy‚ª“¯‚¶W‡‚É“ü‚Á‚Ä‚¢‚é‚©‚Ç‚¤‚©‚ğ”»’è
		return root(x) == root(y);
	}
	int root(int x) {
		return data[x] < 0 ? x : data[x] = root(data[x]);
	}
	bool isroot(int x) {
		return data[x] < 0;
	}
	int size(int x) {
		return -data[root(x)];
	}
};

signed main() {
	int n;

	scanf("%d", &n);

	REP(cc, n) {
		char s[2001];
		int m;
		scanf("%s %d", s, &m);
		string str(s);
		vector<int> imo(strlen(s) + 2000);
		int st = 0, ans = 0;
		bool f = 0;
		REP(i, str.length()) {
			int cur = str[i] == '+';
			st += imo[i];
			cur += st;
			cur %= 2;

			if (!cur) {
				if (i <= (str.length() - m)) {
					st += 1;
					imo[i + m] += 1;
					ans++;
				}
				else {
					f = 1;
					break;
				}
			}
		}
		if (f)
			printf("Case #%d: IMPOSSIBLE\n",cc+1);
		else
			printf("Case #%d: %d\n", cc+1, ans);
	}

	return 0;
}