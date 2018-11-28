#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <cmath>
#include <ctime>
#pragma comment (linker, "/STACK:256000000")

using namespace std;

void readData() {
}

// 0 - Paper
// 1 - Rock
// 2 - Scissors

int winner(int x, int y) {
	if (x == y) {
		return -1;
	}
	if (x > y) {
		swap(x, y);
	}
	if (x == 0 && y == 1) {
		return 0;
	}
	if (x == 0 && y == 2) {
		return 2;
	}
	if (x == 1 && y == 2) {
		return 1;
	}
	return -1;
}

vector < int > prepare(const vector < int > &a, int l, int r) {
	if (l + 1 == r) {
		return vector < int > (1, a[l]);
	}

	int m = (l + r) / 2;
	vector < int > L = prepare(a, l, m);
	vector < int > R = prepare(a, m, r);
	if (L > R) {
		swap(L, R);
	}
	vector < int > res = L;
	for (int i = 0; i < R.size(); ++i) {
		res.push_back(R[i]);
	}
	return res;
}

vector < int > gen(int start, int n) {
	vector < int > res(1, start);
	while (res.size() != (1 << n)) {
		vector < int > current;
		for (int i = 0; i < res.size(); ++i) {
			if (res[i] == 0) {
				current.push_back(0);
				current.push_back(1);
			} else if (res[i] == 1) {
				current.push_back(1);
				current.push_back(2);
			} else {
				current.push_back(0);
				current.push_back(2);
			}
		}
		res = current;
	}
	res = prepare(res, 0, res.size());
	return res;
}

bool check(vector < int > a, int r, int p, int s) {
	return r == count(a.begin(), a.end(), 1) && p == count(a.begin(), a.end(), 0) && s == count(a.begin(), a.end(), 2);
}

void solve2(int test) {
	int n, r, p, s;
	cin >> n >> r >> p >> s;
	vector < int > a = gen(0, n);
	vector < int > b = gen(1, n);
	vector < int > c = gen(2, n);

	vector < vector < int > > d;
	d.push_back(a);
	d.push_back(b);
	d.push_back(c);

	sort(d.begin(), d.end());
	for (int i = 0; i < d.size(); ++i) {
		if (check(d[i], r, p, s)) {
			printf("Case #%d: ", test);
			for (int j = 0; j < d[i].size(); ++j) {
				printf("%c", (d[i][j] == 0 ? 'P' : (d[i][j] == 1 ? 'R' : 'S')));
			}
			printf("\n");
			return;
		}
	}
	printf("Case #%d: IMPOSSIBLE\n", test);
}

void solve(int test) {
	int n, r, p, s;
	cin >> n >> r >> p >> s;
	vector < int > order(1 << n);
	for (int i = 0; i < p; ++i) {
		order[i] = 0;
	}
	for (int i = p; i < p + r; ++i) {
		order[i] = 1;
	}
	for (int i = p + r; i < (1 << n); ++i) {
		order[i] = 2;
	}

	do {
		vector < int > res = order;
		bool bad = false;
		while (res.size() > 1 && !bad) {
			vector < int > cur;
			for (int i = 0; i < res.size(); i += 2) {
				cur.push_back(winner(res[i], res[i + 1]));
				if (cur.back() == -1) {
					bad = true;
					break;
				}
			}
			res = cur;
		}
		if (bad) {
			continue;
		}
		printf("Case #%d: ", test);
		for (int i = 0; i < order.size(); ++i) {
			printf("%c", (order[i] == 0 ? 'P' : (order[i] == 1 ? 'R' : 'S')));
		}
		printf("\n");
		return;
	} while (next_permutation(order.begin(), order.end()));
	printf("Case #%d: IMPOSSIBLE\n", test);
}

int main(int argc, char* argv[]) {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int left_bound, right_bound;

	/*freopen(argv[3], "w", stdout);	
	sscanf(argv[1], "%d", &left_bound);
	sscanf(argv[2], "%d", &right_bound);*/

	int t;
	cin >> t;
	left_bound = 1, right_bound = t;
	for (int i = 1; i <= t; ++i) {
		if (i >= left_bound && i <= right_bound) {
			solve2(i);
		}
		cerr << i << ": " << clock() << endl;
	}

	return 0;
}
