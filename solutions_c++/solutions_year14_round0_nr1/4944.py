#include <stdio.h>
#include<conio.h>
int main(){

		freopen("A-small-attempt3.in","r",stdin);
	freopen("code.out","w",stdout);
	int t=0,i=0,j=0,k=0,h=0;
	int y=0,a=0,b=0,c[4][4],d[4][4],e[4],f[4],g[100],l[100];
	scanf("%d",&t);
	for(k=1;k<=t;k++){
		scanf("%d",&a);
		for(i=0;i<=3;i++){
			for(j=0;j<=2;j++){
				scanf("%d ",&c[i][j]);
			}		scanf("%d",&c[i][3]);
		}
		for(i=0;i<=3;i++){
			e[i]=c[a-1][i];
		}
		scanf("%d",&b);
			for(i=0;i<=3;i++){
			for(j=0;j<=2;j++){
				scanf("%d ",&d[i][j]);
			}	scanf("%d",&d[i][3]);
		}
			for(i=0;i<=3;i++){
			f[i]=d[b-1][i];
		}
		h=0;
		y=0;
		for(i=0;i<=3;i++){
			for(j=0;j<=3;j++){
				if(e[i]==f[j]){
		y=e[i];
					h++;
					
				}
			}
		}
		
		if(h==1){
			l[k]=y;
			g[k]=2;
		}
		if(h==0){
		
		g[k]=0;
			
		}
		if(h>1){
				g[k]=1;
	}}
	for(i=1;i<=t;i++){
		printf("Case #%d: ",i);
		if(g[i]==2){
			printf("%d\n",l[i]);
		}
		else if(g[i]==1){
				printf("Bad Magician!\n");
		}
		else{
				printf("Volunteer cheated!\n");
		}
	
}
	
	return 0;
}
