#include<stdio.h>
int main(){
	//freopen("input.txt", "r", stdin);
	//freopen("out.txt","w",stdout);
	int t,arr1[4][4],pos,arr2[4][4],x,y,i=0,j=0,c=0,count=0;
	scanf("%d",&t);
	while(t--){
		c++; count = 0;
		scanf("%d",&x);
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
			scanf("%d",&arr1[i][j]);
		}
		scanf("%d",&y);
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
			scanf("%d",&arr2[i][j]);
		}
		for(i=0;i<4;i++){
			for(j=0;j<4;j++)
			if(arr1[x-1][i]==arr2[y-1][j]){
					count++;
					pos=i;
			}
		}
		if(count==0)printf("Case #%d: Volunteer cheated!\n",c);
		else if(count==1)printf("Case #%d: %d\n",c,arr1[x-1][pos]);
		else printf("Case #%d: Bad magician!\n",c);
	}
	return 0;
}
