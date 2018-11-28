#include<stdio.h>

int a[7][7],b[7][7];
int chk[20];

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,x,y;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int ans = -1;
		scanf("%d",&x);
		for(int i=1;i<=4;i++)for(int j=1;j<=4;j++)scanf("%d",a[i]+j);
		scanf("%d",&y);
		for(int i=1;i<=4;i++)for(int j=1;j<=4;j++)scanf("%d",b[i]+j);
		for(int i=1;i<=4;i++)chk[a[x][i]]++, chk[b[y][i]]++;
		for(int i=1;i<=16;i++){
			if(chk[i] == 2 && ans == -1)ans = i;
			else if(chk[i] == 2)ans = -2;
		}
		printf("Case #%d: ",t);
		if(ans == -1)printf("Volunteer cheated!\n");
		else if(ans == -2)printf("Bad magician!\n");
		else printf("%d\n",ans);
		for(int i=1;i<=16;i++)chk[i]=0;
	}
	return 0;
}
