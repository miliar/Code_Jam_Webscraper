//  Created by Sengxian on 5/8/16.
//  Copyright (c) 2016年 Sengxian. All rights reserved.
//  
#include <algorithm>
#include <iostream>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <vector>
#include <queue>
using namespace std;

inline int ReadInt() {
	static int n, ch;
	n = 0, ch = getchar();
	while (!isdigit(ch)) ch = getchar();
	while (isdigit(ch)) n = (n << 3) + (n << 1) + ch - '0', ch = getchar();
	return n;
}
typedef long long ll;
const int maxn = 3 + 1, maxp = 9 + 1;
int n, t[maxn];


struct state {
	int left, t[maxn];
	inline bool valid() const {
		for (int i = 0; i < n; ++i)
			if (t[i] * 2 > left || t[i] < 0) return false;
		return true;
	}
}st;

int oper[maxn * maxp][2];

void print(int k) {
	for (int i = 0; i < k; ++i) {
		putchar(' ');
		for (int j = 0; j < 2; ++j)
			if (oper[i][j] != -1) putchar(oper[i][j] + 'A');
	}
	
	putchar('\n');
}

bool dfs(int k) {
	if (st.left == 0) {
		print(k);
		return true;
	}
	state ori = st;
	for (int i = 0; i < n; ++i) {
		st.left--;
		st.t[i]--;
		if (st.valid()) {
			oper[k][0] = i, oper[k][1] = -1;
			if (dfs(k + 1)) return true;
		}
		st = ori;
	}
	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j) {
			st.left -= 2;
			st.t[i]--, st.t[j]--;
			if (st.valid()) {
				oper[k][0] = i, oper[k][1] = j;
				if (dfs(k + 1)) return true;
			}
			st = ori;
		}
	return false;
}

int main() {
	int caseNum = ReadInt();
	for (int t = 1; t <= caseNum; ++t) {
		n = ReadInt();
		st.left = 0;
		printf("Case #%d:", t);
		for (int i = 0; i < n; ++i) st.left += st.t[i] = ReadInt();
		dfs(0);
	}
	return 0;
}
