#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<queue>
using namespace std;
int n;
int flag[17];
int main(){
	int T,Case = 1;
	scanf("%d",&T);
	while(T--){
		memset(flag,0,sizeof(flag));
		scanf("%d",&n);
		int a[5][5];
		for(int i = 1;i <= 4;i ++){
			for(int j = 1;j <= 4;j ++){
				scanf("%d",&a[i][j]);
				if(i == n)
					flag[a[i][j]]++;
			}
		}
		scanf("%d",&n);
		for(int i = 1;i <= 4;i ++){
			for(int j = 1;j <= 4;j ++){
				scanf("%d",&a[i][j]);
				if(i == n)
					flag[a[i][j]]++;
			}
		}
		int ans = 0,mark = -1;
		for(int i = 1;i <= 16;i ++){
			if(flag[i] == 2)
				ans++,mark = i;
		}
		printf("Case #%d: ",Case++);
		if(ans == 1)
			printf("%d\n",mark);
		else if(ans > 1)
			printf("Bad magician!\n");
		else
			printf("Volunteer cheated!\n");
	}
	return 0;
}
