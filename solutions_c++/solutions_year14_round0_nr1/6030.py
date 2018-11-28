#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int val[2][4][4];

int main(){
	int t, icase = 0;
	scanf("%d", &t);
	while(t--){
		int r[2];
		for(int i = 0; i < 2; i++){
			scanf("%d", &r[i]);
			r[i]--;
			for(int j = 0; j < 4; j++){
				for(int k = 0; k < 4; k++){
					scanf("%d", &val[i][j][k]);
				}
			}
		}
		int num = 0, ans = 0;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				if(val[0][r[0]][i] == val[1][r[1]][j]){
					num++;
					ans = val[0][r[0]][i];
				}
			}
		}
		printf("Case #%d: ", ++icase);
		if(num == 1){
			printf("%d\n", ans);
		}
		else if(num == 0){
			puts("Volunteer cheated!");
		}
		else{
			puts("Bad magician!");
		}
	}
	return 0;
}
