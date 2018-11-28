#include <cstdio>

using namespace std;

int a[4][4], b[4][4];

int main() {
	int T, z = 0;
	scanf(" %d", &T);
	while(T --) {
		z ++;
		int a1, a2;
		scanf(" %d", &a1);
		a1 --;
		for(int i = 0; i < 4; i ++)
			for(int j = 0; j < 4; j ++)
				scanf(" %d", &a[i][j]);
		//printf("Row1: %d %d %d %d\n", a[a1][0], a[a1][1], a[a1][2], a[a1][3]);
		scanf(" %d", &a2);
		a2 --;
		for(int i = 0; i < 4; i ++)
			for(int j = 0; j < 4; j ++)
				scanf(" %d", &b[i][j]);
		//printf("Row2: %d %d %d %d\n", b[a2][0], b[a2][1], b[a2][2], b[a2][3]);
	 	int cnt = 0, ans;
		for(int i = 0; i < 4; i ++)
			for(int j = 0; j < 4; j ++)
				if(a[a1][i] == b[a2][j]) {
					cnt ++;
					ans = a[a1][i];
				}
		if(cnt == 1)
			printf("Case #%d: %d\n", z, ans);
		else if(cnt == 0)
			printf("Case #%d: Volunteer cheated!\n", z);
		else
			printf("Case #%d: Bad magician!\n", z);
	}
	return 0;
}
