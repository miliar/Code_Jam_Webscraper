#include<stdio.h>
int T;
int a,b;
int x[16];
int y[16];
int main(){
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		printf("Case #%d: ",i+1);
		scanf("%d",&a);
		for(int j=0;j<16;j++) scanf("%d",&y[j]);
		for(int j=0;j<4;j++) x[y[4*(a-1)+j]-1]=1;
		scanf("%d",&a);
		for(int j=0;j<16;j++) scanf("%d",&y[j]);
		for(int j=0;j<4;j++) if(x[y[4*(a-1)+j]-1]==1)x[y[4*(a-1)+j]-1]=2;
		int cnt=0;
		int ans=0;
		for(int j=0;j<16;j++){
			if(x[j]==2){
				cnt++;
				ans=j+1;
			}
		}
		if(cnt==0) puts("Volunteer cheated!");
		else if(cnt>1) puts("Bad magician!");
		else printf("%d\n",ans);
		for(int j=0;j<16;j++) x[j]=y[j]=0;
	}
	return 0;
}