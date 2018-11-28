#include <iostream>
#include <iomanip>
#include <cstdio>
#include <bitset>
#include <memory>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <list>
#include <string>
#include <cstring>
#include <fstream>
#include <functional>
#include <stack>
#include <complex>
#include <wchar.h>
#include <wctype.h>
#include <cmath>
#include <queue>
#include <ctime>
#include <numeric>
#include <unordered_map>
#include <unordered_set>

using namespace std;

template<typename T> T mabs(const T &a) { return a<0 ? -a : a; }
#define rep(x,y,z) for(int x=(y),e##x=(z);x<e##x;x++)
#define SQR(x) ((x)*(x))
#define all(c) (c).begin(), (c).end()

typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef short int si;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<ll, int> pli;
typedef pair<int, ll> pil;
typedef pair<double, double> pdd;

const double EPS = 1e-8;

void init() {

}

char buf[100500];

map<string, int> strs;

vector<int> parseString(const string &str) {
	stringstream ss(str);
	vector<int> res;
	set<int> curSent;
	while (!ss.eof()) {
		string cur;
		ss >> cur;
		if (cur.size() == 0)
			break;
		if (strs.find(cur) == strs.end()) {
			strs[cur] = strs.size();
		}
		int id = strs[cur];
		if (curSent.find(id) == curSent.end()) {
			res.push_back(strs[cur]);
			curSent.insert(id);
		}
	}
	return res;
}

vector<int> count0, countA;
vector<vector<int> > sents;

void fillCount0() {
	count0.clear();
	count0.resize(strs.size(), 0);
	countA.clear();
	countA.resize(strs.size(), 0);
	int n = sents.size();
	rep(i, 0, sents[0].size()) {
		count0[sents[0][i]]++;
		countA[sents[0][i]]++;
	}
	rep(j, 1, n) {
		rep(i, 0, sents[j].size()) {
			countA[sents[j][i]]++;
		}
	}
}

int calcTrue() {
	int n = sents.size();
	int res = 1e9;
	rep(mask, 0, 1 << (n - 2)) {
		fillCount0();
		rep(j, 2, n) {
			if ((mask >> (j - 2)) & 1) {
				rep(i, 0, sents[j].size()) {
					count0[sents[j][i]]++;
				}
			}
		}
		int cr = 0;
		rep(i, 0, count0.size()) {
			if (count0[i] != 0 && count0[i] != countA[i])
				cr++;
		}
		res = min(res, cr);
	}
	return res;
}

void test() {
	int n;
	sents.clear();
	strs.clear();
	scanf("%d", &n);
	rep(i, 0, n) {
		scanf(" ");
		fgets(buf, 100499, stdin);
		vector<int> curSent = parseString(buf);
		sents.push_back(curSent);
	}
	int ans = calcTrue();
	printf("%d\n", ans);
}

void run()
{
	init();
	int tc;
	scanf("%d", &tc);
	rep(i, 0, tc) {
		printf("Case #%d: ", i + 1);
		test();
		cerr << i << endl;
	}
}

//#define prob "fence"

int main()
{
#ifdef LOCAL_DEBUG
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	time_t st = clock();
#else 
#ifdef prob
	freopen(prob".in", "r", stdin);
	freopen(prob".out", "w", stdout);
#endif
#endif

	run();

#ifdef LOCAL_DEBUG
	fprintf(stderr, "\n=============\n");
	fprintf(stderr, "Time: %.2lf sec\n", (clock() - st) / double(CLOCKS_PER_SEC));
#endif

	return 0;
}