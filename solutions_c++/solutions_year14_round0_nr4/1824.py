#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <set>

using namespace std;
#define dprintf debug && printf
#define F(x,y) for(typeof((y).begin()) x = (y).begin(); x != (y).end(); ++x) 
#define CHECKREAD(x, ...) if(scanf(__VA_ARGS__) != x) { fprintf(stderr, "Failed to read on %s, %d\n", __FILE__, __LINE__); exit(1); }


const enum {SIMPLE, FOR, WHILE} mode = FOR;
bool debug = false;

void init() {
}

int find_ken(const double w, const vector<double> &ken, const vector<char> &used) {
	int ret = -1;
	for(int i = (int) ken.size() - 1; i >= 0; --i) {
		if(!used[i] && ken[i] > w)
			ret = i;
	}

	if(ret != -1)
		return ret;

	for(int i = 0; i < (int) ken.size(); ++i) {
		if(!used[i])
			return i;
	}
	assert(!"Unreachable");
}

bool solve(int P) {
	printf("Case #%d: ", P+1);
	int n;
	if( scanf("%d", &n) != 1) assert(!"Failed to read n");
	vector <double> naomi(n), ken(n);
	for(int i = 0; i < n; ++i) {
		if(scanf("%lf", &naomi[i]) != 1) assert(!"Failed to read naomi number");
	}
	for(int i = 0; i < n; ++i) {
		if(scanf("%lf", &ken[i]) != 1) assert(!"Failed to read ken number");
	}
	sort(naomi.begin(), naomi.end());
	sort(ken.begin(), ken.end());

	dprintf("naomi:");
	F(it, naomi) {
		dprintf(" %lf ", *it);
	}
	dprintf("\n");
	dprintf("ken:");
	F(it, ken) {
		dprintf(" %lf ", *it);
	}
	dprintf("\n");

	int kbig = 0, dans = 0;
	for(int i = 0; i < n; ++i) {
		if(naomi[i] > ken[i - kbig]) {
			++dans;
		} else {
			++kbig;
		}
	}

	vector<char> used(n);
	int hans = 0;
	for(int i = 0; i < n; ++i) {
		int k = find_ken(naomi[i], ken, used);
		dprintf("Playing %lf, responded with %lf\n", naomi[i], ken[k]);
		used[k] = 1;
		if(ken[k] < naomi[i])
			++hans;
	}

	printf("%d %d\n", dans, hans);
	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
