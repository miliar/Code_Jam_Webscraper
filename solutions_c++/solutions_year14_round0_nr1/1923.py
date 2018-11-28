#include <stdio.h>

int main(){
	int T;
	int a[5][5], b[5][5];
	int rec[17];
	int ans_a, ans_b;
	scanf("%d", &T);
	for(int t=1; t<=T; ++t){
		scanf("%d", &ans_a);
		for(int i=1; i<=4; ++i){
			for(int j=1; j<=4; ++j) scanf("%d", &a[i][j]);
		}
		scanf("%d", &ans_b);
		for(int i=1; i<=4; ++i){
			for(int j=1; j<=4; ++j) scanf("%d", &b[i][j]);
		}
		for(int i=1; i<=16; ++i) rec[i] = 0;
		for(int j=1; j<=4; ++j) rec[a[ans_a][j]]++;
		for(int j=1; j<=4; ++j) rec[b[ans_b][j]]++;
		int cnt = 0, ans;
		for(int i=1; i<=16; ++i){
			if(rec[i] == 2){
				cnt++;
				ans = i;
			}
		}
		printf("Case #%d: ", t);
		if(cnt == 0) printf("Volunteer cheated!\n");
		else if(cnt == 1) printf("%d\n", ans);
		else printf("Bad magician!\n");
	}
	
	return 0;
}

