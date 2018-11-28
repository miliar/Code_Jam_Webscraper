//I hate this town, bacause it's too filled with memories I'd rather forget.
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

//kAc
const double pi = acos(-1.0), eps = 1e-9;
const int dx[8] = {1, -1, 0, 0, 1, 1, -1, -1};
const int dy[8] = {0, 0, 1, -1, 1, -1, -1, 1};
const int MO = (int)(1e9 + 7);

//Two becomes one,and it through all eternity.
#define ALL(x) x.begin(), x.end()
#define fr(x, E) for (__typeof(E.begin()) x = E.begin(); x != E.end(); x++)
#define MP make_pair
#define PB push_back
#define FR first
#define SC second
#define ERR cerr << "ERROR" << endl
#define LL long long
#define LD long double
#define PII pair<int, int>
#define PIII pair<PII, int>
#define PDI pair<double, int>
#define PID pair<int, double>
#define SZ(a) (int)((a).size())
#define VEC vector
#define STR string
#define ISS istringstream
#define OSS ostringstream
#define CLR(a, b) memset(a, b, sizeof(a))
#define gmin(a, b) { if (b < a) a = b; }
#define gmax(a, b) { if (b > a) a = b; }
const int INF = 0x3f3f3f3f;
using namespace std;
struct Tflow{
	int tot, e[1000001], v[1000001], next[1000001], c[1000001], d[1000001], q[1000001], l, r, s, t, n;
	Tflow() { tot = 1; }
	void init()
	{
		for (int i = 1; i <= n; i++) e[i] = 0;
	}
	void addedge(int A, int B, int C)
	{
		//cerr << A << " " << B << " " << C << endl;
		++tot; next[tot] = e[A]; e[A] = tot; v[tot] = B; c[tot] = C;
		++tot; next[tot] = e[B]; e[B] = tot; v[tot] = A; c[tot] = 0;
	}
	bool relabel()
	{
		for (int i = 1; i <= n; i++) d[i] = -1;
		q[l = r = 1] = s; d[s] = 0;
		while(l <= r){
			int x = q[l++];
			for (int i = e[x]; i; i = next[i]) if (d[v[i]] == -1 && c[i] > 0){
				d[v[i]] = d[x] + 1; q[++r] = v[i];
			}
		}
		return d[t] != -1;
	}
	int find(int x, int f = 0x3f3f3f3f)
	{
		if (x == t) return f; int augc = f;
		for (int i = e[x]; i; i = next[i]) if (c[i] > 0 && d[v[i]] == d[x] + 1){
			int t = find(v[i], min(f, c[i]));
			c[i] -= t; c[i ^ 1] += t; f -= t; if (f == 0) return augc;
		}
		if (f != 0) d[x] = -1;
		return augc - f;
	}
	int run()
	{
		int ret = 0, t = 0;
		while(relabel())
			while(t = find(s)) ret += t;
		return ret;
	}
} flow;
int left(int x) { return 2 * x + 1; }
int right(int x) { return 2 * x + 2; }
int main()
{
#ifndef ONLINE_JUDGE
	freopen("temp.in", "r", stdin); freopen("temp.out", "w", stdout);
#endif
int TestCase; cin >> TestCase;
for (int ti = 1; ti <= TestCase; ti++){
	cerr << "New" << endl;
	printf("Case #%d: ", ti);
	map<string, int> dict; dict.clear(); 
	int dictnum = 0;
	int n; cin >> n;
	flow.init();
	flow.s = 1; flow.t = 2;
	while(true){
		string s; cin >> s;
		if (dict.count(s) == 0){
			dict[s] = ++dictnum;
		}
		flow.addedge(flow.s, left(dict[s]), INF);
		char c = getchar();
		if (c == '\n') break;
	}
	while(true){
		string s; cin >> s;
		if (dict.count(s) == 0){
			dict[s] = ++dictnum;
		}
		flow.addedge(right(dict[s]), flow.t, INF);
		char c = getchar();
		if (c == '\n') break;
	}
	while(n > 2){
		--n;
		vector<int> a;
		while(true){
			string s; cin >> s;
			if (dict.count(s) == 0){
				dict[s] = ++dictnum;
			}
			a.push_back(dict[s]);
			char c = getchar();
			if (c == '\n') break;
		}
		for (int i = 0; i < a.size(); i++)
			for (int j = 0; j < a.size(); j++) if (i != j)
				flow.addedge(right(a[i]), left(a[j]), INF);
	}
	for (int i = 1; i <= dictnum; i++)
		flow.addedge(left(i), right(i), 1);

	flow.n = dictnum * 2 + 2;
	printf("%d\n", flow.run());
}    

}
