#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
using namespace std;

int x[20];
void doit(){
	int row, a;
	scanf("%d", &row);
	for(int i = 0; i < 4; i++)
		for(int j = 0; j < 4; j++){
			scanf("%d", &a);
			if(i + 1 == row)
				x[a]++;
		}
}
int main(){
	int t, cas=0;
//	freopen("A-small-attempt2.in", "r", stdin);
//	freopen("A-small-attempt2.out", "w", stdout);
	scanf("%d", &t);
	while(t--){
		memset(x, 0, sizeof(x));
		doit();
		doit();
		int cnt = 0, ans = -1;
		for(int i = 1; i <= 16; i++)
			if(x[i] == 2){
				cnt++;
				ans = i;
			}
		printf("Case #%d: ", ++cas);
		if(cnt > 1){
			puts("Bad magician!");
		} else if(cnt == 1){
			printf("%d\n", ans);
		} else {
			puts("Volunteer cheated!");
		}
	}
	return 0;
}
