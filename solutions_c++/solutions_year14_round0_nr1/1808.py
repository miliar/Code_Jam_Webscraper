#include<cstdio>
#include<iostream>

int main(){
	int T;
	int r1, r2;
	scanf("%d", &T);
	int block[4][4];
	int check[20];
	for(int i = 1; i <= T;i++){
		memset(check, 0, sizeof(check));
		scanf("%d", &r1);
		int temp = 0;
		for(int j = 0;j < 4; j++){
			for(int k = 0; k < 4; k++){
				scanf("%d", &temp);
				if(j == r1-1){
					check[temp]++;
				}
			}
		}
		scanf("%d", &r2);
		for(int j = 0;j < 4; j++){
			for(int k = 0; k < 4; k++){
				scanf("%d", &temp);
				if(j == r2-1){
					check[temp]++;
				}
			}
		}
		int cnt = 0;
		int ans = 0;
		for(int j = 1;j < 17;j++){
			if(check[j] == 2){
				ans = j;
				cnt++;
			}
		}
		if(cnt == 0)
			printf("Case #%d: Volunteer cheated!\n", i);
		if(cnt > 1)
			printf("Case #%d: Bad magician!\n", i);
		if(cnt == 1)
			printf("Case #%d: %d\n", i, ans);
	}
	return 0;
} 
