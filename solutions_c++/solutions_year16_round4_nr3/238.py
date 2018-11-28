#include <stdio.h>
#include <vector>
#include <string.h>
#include <algorithm>
using namespace std;
int r, c, map[18][18],num[18][18];
pair<int, int>su[101];
bool flag;
pair<int, int> find_axis(int b){
	for (int i = 0; i <= r + 1; i++){
		for (int j = 0; j <= c + 1; j++){
			if (num[i][j] == b)
				return make_pair(i, j);
		}
	}
}
int go[4][2] = { 1, 0, 0, 1, -1, 0, 0, -1 }; 
bool valid() {
	int y, x, dir;
	for (int i = 0; i < r+c; i++){
		pair<int, int> s = find_axis(su[i].first);
		if (su[i].first <= c)
			dir = 0;
		else if (su[i].first <= c + r)
			dir = 3;
		else if (su[i].first <= c + r + c)
			dir = 2;
		else
			dir = 1;
		y = s.first; x = s.second;
		while (1){
			y += go[dir][0]; x += go[dir][1];
			if (!(y >= 1 && x >= 1 && y <= r && x <= c)) break;
			if (map[y][x] == 1){
				dir = 3 - dir;
			}
			else{
				if (dir <= 1)
					dir = 1 - dir;
				else
					dir = 5 - dir;
			}
		}
		if (num[y][x] != su[i].second)
			return false;
	}
	return true;
}
void fill_map(int i, int j){
	if (i == r+1){
		if (valid())
			flag = 1;
		return;
	}

	map[i][j] = 1;
	if (j == c)
		fill_map(i + 1, 1);
	else
		fill_map(i, j + 1);
	if (flag) return;
	map[i][j] = 2;
	if (j == c)
		fill_map(i + 1, 1);
	else
		fill_map(i, j + 1);
}
int main(){
	int testt;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &testt);
	for (int test = 1; test <= testt; test++){
		flag = 0;
		printf("Case #%d:\n", test);
		memset(num, 0, sizeof(num));
		memset(map, 0, sizeof(map));
		scanf("%d %d", &r, &c);
		for (int i = 0; i < (r+c); i++)
			scanf("%d %d", &su[i].first, &su[i].second);
		int cnt = 0;
		for (int i = 0; i < c; i++)
			num[0][i + 1] = ++cnt;
		for (int i = 0; i < r; i++)
			num[i + 1][c + 1] = ++cnt;

		for (int i = c - 1; i >= 0;i--)
			num[r+1][i + 1] = ++cnt;
		for (int i = r - 1; i >= 0;i--)
			num[i + 1][0] = ++cnt;

		fill_map(1, 1);
		if (!flag)
			printf("IMPOSSIBLE\n");
		else{
			for (int i = 1; i <= r; i++){
				for (int j = 1; j <= c; j++){
					if (map[i][j]==1)
						printf("/");
					else if (map[i][j]==2)
						printf("\\");
				}
				printf("\n");
			}
		}
	}
	return 0;
}
