#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define DEBUG 0
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<pair<int, int> > VPII;

int N, M;
VI rows, cols;
VVI table;
VPII min_heap;

void readin()
{
	int i, j, cnt;
	rows.clear();
	cols.clear();
	table.clear();
	min_heap.clear();
	scanf("%d%d\n", &N, &M);
#if DEBUG
	cout << "N: " << N << " M: " << M << endl;
#endif
	cnt = 0;
	for (i = 0; i < N; ++i) {
		VI line;
		int h;
		for (j = 0; j < M; ++j) {
			scanf("%d", &h);
			line.push_back(h);
			min_heap.push_back(PII(h, cnt++));
		}
		table.push_back(line);
	}
	rows.assign(N, 1);
	cols.assign(M, 1);
	make_heap(min_heap.begin(), min_heap.end(), greater<PII>());
}

bool check_row(int row_idx, int col_idx)
{
	int h = table[row_idx][col_idx];
	int i;
	for (i = 0; i < M; ++i) {
		if (cols[i] == 0)
			continue;
		if (table[row_idx][i] > h)
			return false;
	}
	return true;
}

bool check_col(int row_idx, int col_idx)
{
	int h = table[row_idx][col_idx];
	int i;
	for (i = 0; i < N; ++i) {
		if (rows[i] == 0)
			continue;
		if (table[i][col_idx] > h)
			return false;
	}
	return true;
}

bool solve()
{
	int rows_left = N, cols_left = M;
	int row_idx, col_idx;
	PII cur;
	while (rows_left > 1 && cols_left > 1) {
		pop_heap(min_heap.begin(), min_heap.end(), greater<PII>());
		cur = min_heap.back();
		min_heap.pop_back();
#if DEBUG
		cout << "cur.first: " << cur.first << " cur.second: " << cur.second << endl;
#endif
		row_idx = cur.second / M;
		col_idx = cur.second % M;
#if DEBUG
		cout << "row_idx: " << row_idx << " col_idx: " << col_idx << endl;
#endif
		if (rows[row_idx] == 0 || cols[col_idx] == 0)
			continue;
		if (check_row(row_idx, col_idx)) {
			rows[row_idx] = 0;
			--rows_left;
		} else if (check_col(row_idx, col_idx)) {
			cols[col_idx] = 0;
			--cols_left;
		} else {
			return false;
		}
	}
	return true;
}

int main(int argc, char *argv[])
{
	int case_num = 0;

	scanf("%d\n", &case_num);

	for (int case_id = 1; case_id <= case_num; ++case_id) {
		readin();
		cout << "Case #" << case_id << ": ";
		bool ret = solve();
		cout << (ret ? "YES" : "NO") << endl;
		cout.flush();
	}

	return 0;
}

