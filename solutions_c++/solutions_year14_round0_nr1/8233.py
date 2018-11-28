#include<stdio.h>
using namespace std;

int main(){
	int t,r1,r2;
	int a1[5][5],a2[5][5];
	int ans,count,i,j;
	scanf("%d",&t);
	int c=0;
	while(t--){
		c++;
		count=0;
		scanf("%d",&r1);
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				scanf("%d",&a1[i][j]);
			}
		}
		scanf("%d",&r2);
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				scanf("%d",&a2[i][j]);
			}
		}
		
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				if(a1[r1][i]==a2[r2][j]){
					count++;
					ans=a1[r1][i];
				}			
			}	
			if(count>1)
			break;
		}	
		if(!count)
		printf("Case #%d: Volunteer cheated!\n",c);
		else if(count==1)
		printf("Case #%d: %d\n",c,ans);
		else
		printf("Case #%d: Bad magician!\n",c);
	}
}
