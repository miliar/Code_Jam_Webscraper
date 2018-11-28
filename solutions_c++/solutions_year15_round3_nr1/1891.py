#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

vector<int> cost;
vector<int> chck;

int check(int C, int W) {
	if(chck[C] != 0)
		return chck[C];
	if(C < W * 2) {
		return chck[C] = 1;
	}
	assert(C >= W*2);
	return chck[C] = C / W;
}


int solve(int C, int W) {
	if(cost[C] != 0)
		return cost[C];
	if(W == 1)
		return cost[C] = C;
	if(C < W * 2) {
		if(C == W)
			return cost[C] = W;
		assert(C > W);
		return cost[C] = W + 1;
	}
	assert(C >= 2 * W);
	if(C == W * 2) {
		return cost[C] = W + 1;
	}
	assert(C > 2 * W);
	int mc = C;
	int ms = 0;
	for(int i = W + 1; i <= C - W; ++i) {
		int ok = W + 1;
		int sep = 1 + min(
				max(check(i-1,W)+solve(C-i,W), solve(i-1,W)),
				max(check(C-i,W)+solve(i-1,W), solve(C-i,W))
				);
		if(max(ok, sep) < mc) {
			mc = max(ok, sep);
			ms = i;
		}
	}
	cerr << "C = " << C << "; minc = " << mc << "; at = " << ms << endl;
	return cost[C] = mc;
}

void oneTest(int caseid) {
	int R, C, W;
	cin >> R >> C >> W;
	cost.clear();
	cost.resize(C + 1);
	chck.clear();
	chck.resize(C + 1);

/*
 * 4 3
 * 5 4
 * 6 4
 * 7 5
 * 8 5
 *
 * 
 *
 *  2:
 *  .. 2
 *  ... 3
 *  ..#. 3
 *  ..#.. 4
 *  ..#.#. 4
 *  .#.#.#. 5
 *  ..#.#.#. 5
 *
 *  3:
 *  ... 3
 *  .... 4
 *  ..#.. 4
 *  ...#.. 4
 *  ...#... 4
 *  ...#..#. 5
 *  ...#..#.. 5
 *  ..#..#..#. 6
 *
 */
	int ans = (C + W + 1) / W;

	cout << "Case #" << caseid << ": " << R * solve(C,W) << endl;
}

int main() {
	ios_base::sync_with_stdio(0);
	int T;
	cin >> T;
	for(int i = 0; i < T; ++i)
		oneTest(i + 1);
	return 0;
}
