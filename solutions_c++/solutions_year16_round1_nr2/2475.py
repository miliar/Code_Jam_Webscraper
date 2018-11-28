#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <list>
#include <algorithm>
#include <string>
#include <deque>
#include <vector>
using namespace std;

FILE *fout;

vector<vector<int>> input(FILE *f, int n) {
	vector<vector<int>> list;
	list.resize(n * 2 - 1);
	int tmp;
	for (int i = 0; i != n * 2 - 1; ++i) {
		vector<int> v;
		v.reserve(n);
		for (int j = 0; j != n; ++j) {
			fscanf(f, "%d", &tmp);
			v.push_back(tmp);
		}
		list[i].swap(v);
	}
	return list;
}

vector<int> mkCurrent(vector<vector<int>> &list, vector<int> &rows, vector<int> &columns, int row, int column, int n) {
	auto &map = row != -1 ? columns : rows;
	int offset = row != -1 ? row : column;
	vector<int> current;
	current.reserve(n);
	for (int i = 0; i != n; ++i) {
		if (map[i] == -1) current.push_back(-1);
		else {
			auto &l = list[map[i]];
			current.push_back(l[offset]);
		}
	}
	return current;
}

void printMap(vector<vector<int>> &list, vector<int> rows, vector<int> columns) {
	printf("-------------------\n");
	for (int i = 0; i != rows.size(); ++i) {
		if (rows[i] != -1) {
			auto &l = list[rows[i]];
			printf("row %d: ", i);
			for (auto c : l) printf("%d ", c);
		}
		printf("\n");
	}
	for (int i = 0; i != columns.size(); ++i) {
		if (columns[i] != -1) {
			auto &l = list[columns[i]];
			printf("col %d: ", i);
			for (auto c : l) printf("%d ", c);
		}
		printf("\n");
	}
}

bool check(vector<vector<int>> &list, vector<int> &rows, vector<int> &columns, vector<vector<int>>::iterator currentItem, int cr, int cc, int n) {
	vector<int> current = mkCurrent(list, rows, columns, cr, cc, n);
	printf("curr %d %d: ", cr, cc);
	for (auto c : current) printf("%d ", c);
	printf("\n");
	for (int i = 0; i != n; ++i) {
		if (current[i] != -1 && current[i] != currentItem->at(i)) return false;
	}
	return true;
}

bool finish;
void doFinish(vector<vector<int>> &list, vector<int> &rows, vector<int> &columns, int n) {
	if (finish) return;
	vector<int> current;
	for (int i = 0; i != rows.size(); ++i) {
		if (rows[i] == -1) {
			printf("rows %d\n", i);
			current = mkCurrent(list, rows, columns, i, -1, n);
		}
	}
	for (int i = 0; i != columns.size(); ++i) {
		if (columns[i] == -1) {
			printf("rows %d\n", i);
			current = mkCurrent(list, rows, columns, -1, i, n);
		}
	}
	for (auto it : current) fprintf(fout, " %d", it);
	fprintf(fout, "\n");
	fflush(fout);
	finish = true;
}

void dfs(vector<vector<int>> &list, vector<int> &rows, vector<int> &columns, vector<vector<int>>::iterator li, int n, int cr, int cc, bool jmp) {
	//printMap(list, rows, columns);
	if (finish) return;
	if (li == list.end()) {
		printf("finished\n");
		doFinish(list, rows, columns, n);
		return;
	}

	if (cr < n && check(list, rows, columns, li, cr, -1, n)) {
		rows[cr] = li - list.begin();
		dfs(list, rows, columns, li + 1, n, cr + 1, cc, jmp);
		rows[cr] = -1;
	}

	if (cc < n && check(list, rows, columns, li, -1, cc, n)) {
		columns[cc] = li - list.begin();
		dfs(list, rows, columns, li + 1, n, cr, cc + 1, jmp);
		columns[cc] = -1;
	}

	if (!jmp) {
		dfs(list, rows, columns, li, n, cr + 1, cc, true);
		dfs(list, rows, columns, li, n, cr, cc + 1, true);
	}
}

bool cmp(vector<int> &l, vector<int> &r) {
	for (int i = 0; i != l.size(); ++i) {
		if (l[i] != r[i]) return l[i] < r[i];
	}
	return 0;
}

int main() {
	int T;
	FILE *f = fopen("input.txt", "r");
	fout = fopen("output.txt", "w");
	fscanf(f, "%d", &T);
	for (int i = 0; i != T; ++i) {
		finish = false;
		int n;
		fscanf(f, "%d", &n);
		vector<vector<int>> list = input(f, n);
		sort(list.begin(), list.end(), cmp);
		vector<int> rows, columns;
		rows.resize(n);
		columns.resize(n);
		fill(rows.begin(), rows.end(), -1);
		fill(columns.begin(), columns.end(), -1);
		fprintf(fout, "Case #%d:", i + 1);
		dfs(list, rows, columns, list.begin(), n, 0, 0, false);
	}
	system("pause");
	return 0;
}