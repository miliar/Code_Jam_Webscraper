#include <stdio.h>
#include <algorithm>
#include <set>
#include <string>
#include <vector>
#include <string.h>
#define mp make_pair
using namespace std;
int n, m;
char map[102][105];
bool check[105][105][4];
int go[4][2] = { 1, 0, 0, 1, -1, 0, 0, -1 };
char arrow[6] = "v>^<";
int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testt;
	scanf("%d", &testt);
	for (int test = 1; test <= testt; test++){
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; i++)
			scanf("%s", map[i]);

		memset(check, 0, sizeof(check));
		for (int i = 0; i < n; i++){
			for (int j = 0; j < m; j++){
				for (int a = 0; a < 4; a++){
					if (i + go[a][0] < 0 || j + go[a][1] < 0 || i + go[a][0] >= n || j + go[a][1] >= m){
						int i2 = i, j2 = j, a2=(a+2)%4;
						while (1){
							if (map[i2][j2] != '.'){
								check[i2][j2][a] = 1;
								break;
							}
							i2 += go[a2][0]; j2 += go[a2][1];
						}
					}
				}
			}
		}
		bool flag = 0;
		int print = 0;
		for (int i = 0; i < n; i++){
			for (int j = 0; j < m; j++){
				if (map[i][j] != '.'){
					if (check[i][j][0] + check[i][j][1] + check[i][j][2] + check[i][j][3] == 4)
						flag = 1;
					else{
						for (int a = 0; a < 4; a++){
							if (arrow[a] == map[i][j]){
								if (check[i][j][a])
									print++;
								break;
							}
						}
					}
				}
			}
		}
		printf("Case #%d: ", test);
		if (flag)
			printf("IMPOSSIBLE");
		else
			printf("%d", print);
		printf("\n");
	}
	return 0;
}