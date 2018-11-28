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

bool solve(int P) {
	printf("Case #%d: ", P+1);
	double C, F, X;
	if(scanf("%lf%lf%lf", &C, &F, &X) != 3) assert(!"Failed to read C F X");

	double rate = 2, t = 0;
	while( X  * rate < (X - C) * (rate + F)) {
		t += C / rate;
		rate += F;
		dprintf("Bought at time %lf to get to rate %lf\n", t, rate);
	}

	t += X / rate;
	printf("%.7lf\n", t);
	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
