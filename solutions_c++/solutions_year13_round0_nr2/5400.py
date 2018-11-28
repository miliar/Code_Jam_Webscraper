#include<stdio.h>

int main(){
	
	int grama[105][105];
	int t, n, m, i, j, k;
	int linha[105];
	int coluna[105];
	
	
	scanf("%d", &t);
	for(k=1;k<=t;k++){
		
		scanf("%d %d", &n, &m);
		
		for(i=0;i<n;i++){
			linha[i]=0;
		}
		for(i=0;i<m;i++){
			coluna[i]=0;
		}
			
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				scanf("%d", &grama[i][j]);
				if(grama[i][j]>linha[i])linha[i]=grama[i][j];
				if(grama[i][j]>coluna[j])coluna[j]=grama[i][j];
			}
		}
		
		int no=0;
		for(i=0;i<n;i++){
			for(j=0;j<m;j++){
				if((grama[i][j]<linha[i])&&(grama[i][j]<coluna[j]))no=1;
			}
		}
		
		printf("Case #%d: ", k);
		if(no)printf("NO\n");
		else printf("YES\n");
	}
	
	return 0;
}