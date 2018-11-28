#include <cstdio>

using namespace std;

int main() {
	char map[4][4];
	int k;
	scanf("%d", &k);
	for (int t = 1; t <= k; ++t) {
		printf("Case #%d: ", t);
		scanf("\n");
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				scanf("%c", &map[i][j]);
			}scanf("\n");
		}
		
		int s = 0;
		for (int i = 0; i < 4; ++i) {
			s = 0;
			for (int j = 0; j < 4; ++j) s += map[i][j];
			if (s == 4*'X' || s==3*'X'+'T') goto Xwon;
			if (s == 4*'O' || s==3*'O'+'T') goto Owon;
			s = 0;
			for (int j = 0; j < 4; ++j) s += map[j][i];
			if (s == 4*'X' || s==3*'X'+'T') goto Xwon;
			if (s == 4*'O' || s==3*'O'+'T') goto Owon;
		}
		s = 0;
		for (int j = 0; j < 4; ++j) s += map[j][j];
		if (s == 4*'X' || s==3*'X'+'T') goto Xwon;
		if (s == 4*'O' || s==3*'O'+'T') goto Owon;
		s = 0;
		for (int j = 0; j < 4; ++j) s += map[3-j][j];
		if (s == 4*'X' || s==3*'X'+'T') goto Xwon;
		if (s == 4*'O' || s==3*'O'+'T') goto Owon;
		
		for (int t = 1; t <= k; ++t) {
			for (int i = 0; i < 4; ++i) {
				for (int j = 0; j < 4; ++j) {
					if (map[i][j] == '.') goto NotCompleted;
				}
			}
		}
		
		printf("Draw\n"); scanf("\n");continue;
		
		NotCompleted:
		printf("Game has not completed\n"); scanf("\n");continue;
		
		Xwon:
		printf("X won\n"); scanf("\n");continue;
		
		Owon:
		printf("O won\n"); scanf("\n");continue;
	}
	
	return 0;
}
