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

vector<int> read_row() {
	int c, tmp;
	vector<int> ret(4);
	scanf("%d", &c);
	--c;
	for(int i = 0; i < 4; ++i) {
		for(int k = 0; k < 4; ++k) {
			scanf("%d", &tmp);
			if(i == c) 
				ret[k] = tmp;
		}
	}
	return ret;
}

bool solve(int P) {
	printf("Case #%d: ", P+1);
	vector<int> r1 = read_row();
	vector<int> r2 = read_row();

	F(it, r1)
		dprintf(" %d", *it);
	dprintf("\n");
	F(it, r2)
		dprintf(" %d", *it);
	dprintf("\n");

	int ans = -1;
	F(it, r1) {
		if(find(r2.begin(), r2.end(), *it) != r2.end()) {
			if(ans != -1) {
				ans = -2;
			} else {
				ans = *it;
			}
		}
	}
	if(ans == -1) {
		printf("Volunteer cheated!\n");
	} else if(ans == -2) {
		printf("Bad magician!\n");
	} else {
		printf("%d\n", ans);
	}
	return true;
}

int main() {
  init();
  int n = mode == SIMPLE ? 1 : 1<<30;
  if (mode == FOR) scanf("%d", &n);
  for (int i = 0; i < n && solve(i); ++i);
  return 0;
}
