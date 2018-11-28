#include<iostream>
using namespace std;

int a[5][5], b[5][5];
int used[18];

int main(){
	freopen("A-small-attempt3.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int cas= 1; cas <= t; cas++){
		memset(used, 0, sizeof(used));
		int ra, rb;
		scanf("%d", &ra);
		for(int i= 1; i <= 4; i++)
			for(int j= 1; j <= 4; j++){
				scanf("%d", &a[i][j]);
				if(i == ra) used[a[i][j]]++;
			}
		scanf("%d", &rb);
		for(int i= 1; i <= 4; i++)
			for(int j= 1; j <= 4; j++){
				scanf("%d", &b[i][j]);
				if(i == rb) used[b[i][j]]++;
			}
		int cnt= 0;
		int ind= 0;
		for(int i= 1; i <= 16; i++){
			if(used[i] == 2){
				cnt++;
				ind= i;
			}
		}
		if(cnt == 1){
			printf("Case #%d: %d\n", cas, ind);
		}
		else if(cnt > 1){
			printf("Case #%d: Bad magician!\n", cas);
		}
		else if(cnt < 1){
			printf("Case #%d: Volunteer cheated!\n", cas);
		}
	}
	return 0;
}