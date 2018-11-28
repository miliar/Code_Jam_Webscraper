#include <iostream>
#include <fstream>
#include <queue>
#include <cstdio>
using namespace std;

int n, m, total;
char a[10][10];
bool ans = false;
int start_x, start_y;
typedef pair<int, int> P;  
int dir[8][2] = {{-1, -1}, {-1, 0}, {-1, 1}, {0, -1}, {0, 1}, {1, -1}, {1, 0}, {1, 1}};

int count(int i, int j) {
	int ans = 0;
	for (int k = 0; k < 8; k++) {
		int x = i + dir[k][0], y = j + dir[k][1];
		if (0 <= x && x < n && 0 <= y && y < m && a[x][y] == '*') {
			ans++;
		}	
	}	
	return ans;
}

bool find() {
	//找起始点
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (a[i][j] == '.' && count(i, j) == 0) {
				start_x = i;
				start_y = j;
				return true;
			}
		}
	}
	return false;
}

void bfs() {
	bool visit[6][6];
	memset(visit, false, sizeof(visit));
	if(!find()) return;
	visit[start_x][start_y] = true;
	queue<P> Q;
	Q.push(P(start_x, start_y));
	int sum = 1;
	while(!Q.empty()) {
		P now = Q.front(); Q.pop();
		for (int k = 0; k < 8; k++) {
			int x = now.first + dir[k][0], y = now.second + dir[k][1];
			if (0 <= x && x < n && 0 <= y && y < m && a[x][y] == '.' && !visit[x][y]) {
				sum++;
				visit[x][y] = true;
				if (count(x, y) == 0)
					Q.push(P(x, y));
			}
		}
	}
	//cout << "sum = " << sum << endl;
	if (sum == n * m - total) {
		a[start_x][start_y] = 'c';
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				printf("%c", a[i][j]);
			}
			printf("\n");
		}
		ans = true;
	}
}


void dfs(int x, int y, int num) {
	if (num == total) {
		//cout << "num = " << num << endl;
		bfs();
		return;
	}
	if (x == n || ans) return;
	a[x][y] = '*';
	if (y == m - 1) dfs(x + 1, 0, num + 1);
	else dfs(x, y + 1, num + 1);
	a[x][y] = '.';
	if (y == m - 1) dfs(x + 1, 0, num);
	else dfs(x, y + 1, num);
}

int main() {
    //ifstream cin("D:\\C-small-attempt2.in");  
    //freopen("D:\\C-small-attempt2.out","w",stdout);  
	int t;
	cin >> t;
	for (int times = 1; times <= t; times++) {
		cin >> n >> m >> total;
        printf("Case #%d:\n", times);
		if (n * m - total == 1) { // 特判只有一个空的情况
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					a[i][j] = '*';
				}
			}
			a[n - 1][m - 1] = 'c';	
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					printf("%c", a[i][j]);
				}
				printf("\n");
			}
            continue;		
		}
		//	初始化
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				a[i][j] = '.';
			}
		}
		ans = false;
		

		dfs(0, 0, 0);
		if (ans == false) {
			printf("Impossible\n");
		}
	}
}
