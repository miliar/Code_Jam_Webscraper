/*
 * codejam_R1C_A.cpp
 *
 *  Created on: May 12, 2013
 *      Author: leo
 */

#include <iostream>
#include <queue>
using namespace std;

#define BLACK 1
#define WHITE 0
#define nNodes 100

bool v[2*nNodes+1][2*nNodes+1];
char p[2*nNodes+1][2*nNodes+1]; // carries the parent of each node / to construct the path
int n; // # nodes in current graph
int w, h; //height and width

int dx[] = { 0, 0, -1, 1 };
int dy[] = { -1, 1, 0, 0 };
char dc[] = { 'S', 'N', 'W', 'E' };

void print_path(int j, int i, int step) {
	if (i == 0+n && j == 0+n) {
	} else {
		switch (p[i][j]) {
		case 'S':
			print_path(j, i+step, step-1);
			break;
		case 'E':
			print_path(j-step, i, step-1);
			break;
		case 'N':
			print_path(j, i-step, step-1);
			break;
		case 'W':
			print_path(j+step, i, step-1);
			break;
		default:
			break;
		}
		cout<<p[i][j];
	}

}

void BFS_matrix(int tx, int ty) {
	for (int i = 0; i < 2*n+1; i++) {
		for (int j = 0; j < 2*n+1; ++j) {
			v[i][j] = WHITE;
			p[i][j] = ' ';
		}
	}
	queue<int> q;
	q.push(0+n);
	q.push(0+n);
	q.push(1);
	v[0+n][0+n] = BLACK;

	int cx, cy, x, y, step;

	while (!q.empty()) {
		cx = q.front();		q.pop();
		cy = q.front();		q.pop();
		step = q.front();	q.pop();

		// visiting operation
		for (int k = 0; k < 4; ++k) {
			x = cx + dx[k] * step;
			y = cy + dy[k] * step;
			if (x < 0 || x > 2*n || y < 0 || y > 2*n || v[y][x])
				continue;
			v[y][x] = true;
			p[y][x] = dc[k];
			if (x == tx && y == ty) {
				print_path(x, y, step);
				return;
			}
			q.push(x);
			q.push(y);
			q.push(step + 1);
		}
	}

}

int main() {
	int tc,x,y;
	cin >> tc;
	n = nNodes;
	for (int t = 1; t <= tc; ++t) {
		cin>>x>>y;
		cout<<"Case #"<<t<<": ";
		BFS_matrix(x+n,y+n);
		cout<<endl;
	}
	return 0;
}

