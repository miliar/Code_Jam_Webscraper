#include <cstdio>
#include <cstring>

void solve(int nT){
	int x[20],row,num;
	memset(x,0,sizeof(x));
	scanf("%d", &row);
	for (int i=1; i<=4; i++){
		for (int j=1; j<=4; j++){
			scanf("%d", &num);
			if (i == row)
				x[num]++;
		}
	}
	scanf("%d", &row);
	for (int i=1; i<=4; i++){
		for (int j=1; j<=4; j++){
			scanf("%d", &num);
			if (i == row)
				x[num]++;
		}
	}
	int ans=-1;
	for (int i=1; i<=16; i++){
		if (x[i] > 1){
			if (ans == -1)
				ans = i;
			else
				ans = -2;
		}
	}
	printf("Case #%d: ", nT);
	if (ans == -1){
		puts("Volunteer cheated!");
	} else if (ans == -2){
		puts("Bad magician!");
	} else {
		printf("%d\n", ans);
	}
}
int main(){
	int nT;
	scanf("%d", &nT);
	for (int i=1; i<=nT; i++)
		solve(i);
	return 0;
}