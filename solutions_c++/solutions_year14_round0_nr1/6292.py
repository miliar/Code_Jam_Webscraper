#include <cstdio>

int main(){
	int T;
	scanf("%d",&T);
	for(int m = 1; m <= T; ++m){
		int a[9][9]={0};
		int b[9][9]={0};
		int cnt = 0;
		int res = 0;
		int s1,s2;		//answer1, answer2
		scanf("%d",&s1);
		for(int i = 1; i <= 4; ++i){
			for(int j = 1; j <= 4; ++j){
				scanf("%d",&a[i][j]);
			}
		}
		scanf("%d",&s2);
		for(int i = 1; i <= 4; ++i){
			for(int j = 1; j <= 4; ++j){
				scanf("%d",&b[i][j]);
			}
		}
		for(int i = 1; i <= 4; ++i){
			for(int j = 1; j <= 4; ++j){
				if ( a[s1][i] == b[s2][j] ){
					cnt++;
					res = a[s1][i];
				}
			}
		}
		printf("Case #%d: ", m);
		if ( cnt == 0 )
			printf("Volunteer cheated!\n");
		if ( cnt == 1 )
			printf("%d\n", res);
		if ( cnt > 1 )
			printf("Bad magician!\n");
	}
}