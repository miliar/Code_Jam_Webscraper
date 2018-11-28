#include<cstdlib>
#include<cstdio>
using namespace std;

int mat[4][4], arr[4];
int main(){
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int cnt = 1; cnt <= T; cnt++){
		printf("Case #%d: ", cnt);
		int fst, scd;
		scanf("%d", &fst);
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				scanf("%d", &mat[i][j]);
				if(i + 1 == fst) arr[j] = mat[i][j];
			}
		}
		scanf("%d", &scd);
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++) scanf("%d", &mat[i][j]);
		}
		int ans = -1;
		bool bad = false;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				if(arr[i] == mat[scd - 1][j]){
					if(ans != -1) bad = true;
					else ans = arr[i];
				}
			}
		}
		if(ans == -1) puts("Volunteer cheated!");
		else if(bad) puts("Bad magician!");
		else printf("%d\n", ans);
	}
	return 0;
}
