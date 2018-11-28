#include<stdio.h>
int main(){
	int n, tanque[5][5],lleno[5][5],cont=1,uno,dos,ans=0,ots;
	
	scanf("%d",&n);
	while(cont<=n){
	ans=0;
	scanf("%d",&uno);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&tanque[i][j]);
				
	scanf("%d",&dos);
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				scanf("%d",&lleno[i][j]);
				
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++){	
				if(tanque[uno-1][i]==lleno[dos-1][j]){
					ans++;
					ots=tanque[uno-1][i];
			}
		}
		if(ans==1)
			printf("Case #%d: %d\n",cont,ots);
		else
			if(ans>1)
				printf("Case #%d: Bad magician!\n",cont);
			else
				printf("Case #%d: Volunteer cheated!\n",cont);
		cont++;
	}
}	
