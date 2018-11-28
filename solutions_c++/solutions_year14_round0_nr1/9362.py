#include<cstdio>
#include<set>
using namespace std;

int mat[10][10];
int mat2[10][10];

int main()
{
	freopen("D:\\A-small-attempt0.in", "r", stdin);
	freopen("D:\\A-small-attempt0.out", "w", stdout);
	int T, TT;
	scanf("%d", &T);
	TT = T;
	while (T--) {
		int a;
		scanf("%d", &a);
		a--;
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				scanf("%d", &mat[i][j]);
			}
		}
		int b;
		scanf("%d", &b);
		b--;
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				scanf("%d", &mat2[i][j]);
			}
		}
		set<int> s;
		for (int i = 0; i < 4; i++){
			s.insert(mat[a][i]);
		}
		int chongfu = 0;
		int ans = 0;
		for (int i = 0; i < 4; i++){
			if (s.count(mat2[b][i])){
				ans = mat2[b][i];
				chongfu++;
			}
		}
		printf("Case #%d: ", TT - T);
		if (chongfu == 1){
			printf("%d\n", ans);
		}
		else if (chongfu == 0) {
			printf("Volunteer cheated!\n");
		}
		else {
			printf("Bad magician!\n");
		}
	}
	return 0;
}