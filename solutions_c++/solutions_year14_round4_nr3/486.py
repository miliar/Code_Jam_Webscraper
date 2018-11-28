/*
 * $File: c.cpp
 * $Date: Sun Jun 01 00:14:02 2014 +0800
 * $Author: Xinyu Zhou <zxytim@gmail.com>
 */

#include <cstdio>
#include <cassert>
#include <cmath>
#include <cstdlib>
#include <ctype.h>
#include <cstring>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>

using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;

template<typename T> void updatemax(T &a, T b) { if (b > a) a = b; }
template<typename T> void updatemin(T &a, T b) { if (b < a) a = b; }

void solve(int case_id);

int main()
{
	int ncase;
	scanf("%d", &ncase);
	for (int id = 1; id <= ncase; id ++)
	{
		printf("Case #%d: ", id);
		solve(id);
	}
	return 0;
}

struct Rect {
	int x0, y0, x1, y1;
	void input() {
		cin >> x0 >> y0 >> x1 >> y1;
	}
};

#define CHECK_RANGE(x, up) assert(x >= 0 && x < up)

std::vector<std::vector<int>> get_field(int W, int H, std::vector<Rect> &rect) {
	std::vector<std::vector<int>> ret(W, std::vector<int>(H));
	for (auto &r: rect) {
		CHECK_RANGE(r.x0, W);
		CHECK_RANGE(r.x1, W);
		CHECK_RANGE(r.y0, H);
		CHECK_RANGE(r.y1, H);
		for (int i = r.x0; i <= r.x1; i ++)
			for (int j = r.y0; j <= r.y1; j ++)
				ret[i][j] = 1;
	}
	return ret;
}

void print_field(std::vector<std::vector<int>> &a) {
	return ;
	fprintf(stderr, "\n");
	int W = a.size(), H = a[0].size();
	for (int j = H - 1; j >= 0; j --) {
		for (int i = 0; i < W; i ++)
			fprintf(stderr, "%c", a[i][j] ? a[i][j] + '0': '.');
		fprintf(stderr, "\n");
	}
	fprintf(stderr, "\n");
}

const vector<pair<int, int>> DIRS = {
//    {-1, 0}, {0, 1}, {1, 0}, {0, -1}
	{0, 1}, {-1, 0}, {0, -1}, {1, 0}
};

int do_fill(vector<vector<int>> &a, int x, int y, int val) {
	int W = a.size(), H = a[0].size();
	if (a[x][y])
		return 0;
	a[x][y] = val;
	if (y == H - 1)
		return 1;
	for (auto &d: DIRS) {
		int nx = x + d.first,
			ny = y + d.second;
		if (!(nx >= 0 && nx < W && ny >= 0 && ny < H))
			continue;
		int v;
		if ((v = do_fill(a, nx, ny, val)) != 0)
			return v;
	}
	return 0;
}

int do_fill_dir(vector<vector<int>> &a, int x, int y, int dir, int val) {
	int W = a.size(), H = a[0].size();
	if (a[x][y])
		return 0;
	print_field(a);
	a[x][y] = val;
	if (y == H - 1)
		return 1;

	auto head = [&](int d) {
		int nx = x + DIRS[d].first,
			ny = y + DIRS[d].second;
		if (!(nx >= 0 && nx < W && ny >= 0 && ny < H))
			return 0;
		int v;
		if ((v = do_fill_dir(a, nx, ny, d, val)) != 0)
			return v;
	};

	for (int i = 1; i >= -2; i --) {
		int d = (dir + i + 4) % 4;
		int v = head(d);
		if (v)
			return v;
	}
	return 0;
}




int get_ans(std::vector<std::vector<int>> &a) {
	int ans = 0;
	int W = a.size(), H = a[0].size();
	print_field(a);
	for (int i = 0; i < W; i ++) {
//        ans += do_fill(a, i, 0, ans + 2);
		ans += do_fill_dir(a, i, 0, 0, ans + 2);
	print_field(a);
	}
	return ans;
}

void solve(int case_id)
{

	int W, H, B;
	cin >> W >> H >> B;
//    fprintf(stderr, "%d %d %d\n", case_id, W, H);
	vector<Rect> rect(B);
	for (int i = 0; i < B; i ++) {
		rect[i].input();
//        if (case_id == 6)
//            fprintf(stderr, "%d %d %d %d\n",
//                    rect[i].x0, rect[i].y0, rect[i].x1, rect[i].y1);
	}

	auto a = get_field(W, H, rect);
	int ans = get_ans(a);
//    if (case_id == 6)
//        fprintf(stderr, "%d\n", ans);

	printf("%d\n", ans);
}

