#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <queue>
#include <vector>
#include <utility>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long llg;

const int N = 101;

struct node {
	int x, y, key;
	node() {}
	node(int _x, int _y, int _key) {
		x = _x; y = _y; key = _key;
	}
};
struct comp {
	bool operator()(const node &a, const node &b) {
		return  a.key > b.key;
	}
};
int T, n, m, h[N][N];
bool visit[N][N];
priority_queue <node, vector<node>, comp> q;

bool judgeRow(int x, int key) {
	for(int i = 0; i < m; i++) {
		if(h[x][i] > key)  return  false;
	}
	return  true;
}

bool judgeCol(int x, int key) {
	for(int i = 0; i < n; i++) {
		if(h[i][x] > key)  return  false;
	}
	return  true;
}

void coverRow(int x, int key) {
	for(int i = 0; i < m; i++)  visit[x][i] = true;
}

void coverCol(int x, int key) {
	for(int i = 0; i < n; i++)  visit[i][x] = true;
}

void run() {
	node tmp;
	scanf("%d", &T);
	for(int Case = 1; Case <= T; Case++) {
		scanf("%d%d", &n, &m);
		while(!q.empty())  q.pop();
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				scanf("%d", &h[i][j]);
				q.push(node(i, j, h[i][j]));
			}
		}
		memset(visit, false, sizeof(visit));
		bool flag = true;
		while(!q.empty()) {
			tmp = q.top(); q.pop();
			if(visit[tmp.x][tmp.y])  continue;
			flag = false;
			if(judgeRow(tmp.x, tmp.key)) {
				coverRow(tmp.x, tmp.key);
				flag = true;
			}
			if(judgeCol(tmp.y, tmp.key)) {
				coverCol(tmp.y, tmp.key);
				flag = true;
			}
			if(!flag)  break;
		}
		for(int i = 0; i<n && flag; i++){
			for(int j = 0; j<m && flag; j++) {
				if(!visit[i][j])  flag = false;
			}
		}
		printf("Case #%d: ", Case);
		if(flag)  printf("YES\n");
		else  printf("NO\n");
	}
}

int main() {
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	run();
	return  0;
}













