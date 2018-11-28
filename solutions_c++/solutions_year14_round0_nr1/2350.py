#include<stdio.h>
int x[4][4],y[4][4];
int main(){
	int t,c=1;
	scanf("%d",&t);
	while(t--){
		int a,b;
		scanf("%d",&a);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&x[i][j]);
		scanf("%d",&b);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&y[i][j]);
		int ans = -2;
			for(int i=0;i<4;i++)
				for(int j=0;j<4;j++){
					if(x[a-1][i]==y[b-1][j]){
						if(ans!=-2){
							ans=-1;
						}else{
							ans = x[a-1][i];
						}
					}
				}
		printf("Case #%d: ",c);		
		if(ans ==-2){
			printf("Volunteer cheated!\n");
		}else  if(ans ==-1){
			printf("Bad magician!\n");
		}else {
			printf("%d\n",ans);
		}
		c++;
	}
	return 0;
}
