#include<stdio.h>

int n,t;
int data[101][101];
bool check[101][101];

int main(){
	freopen("INPUT.TXT","r",stdin);
	freopen("OUTPUT.TXT","w",stdout);
	scanf("%d",&t);
	while(n++<t){
		int x,y;
		scanf("%d %d",&x,&y);
		for(int i=1;i<=x;i++){
			for(int j=1;j<=y;j++){
				scanf("%d", &data[i][j]);
				check[i][j] = false;
			}
		}
		for(int i=1;i<=x;i++){
			int max1 = 0;
			for(int j=1;j<=y;j++){
				if(data[i][j]>max1) max1 = data[i][j];
			}
			for(int j=1;j<=y;j++){
				if(data[i][j]==max1) check[i][j] = true;
			}
		}
		for(int i=1;i<=y;i++){
			int max1 = 0;
			for(int j=1;j<=x;j++){
				if(data[j][i]>max1) max1 = data[j][i];
			}
			for(int j=1;j<=x;j++){
				if(data[j][i]==max1) check[j][i] = true;
			}
		}
		int i,j;
		for(i=1;i<=x;i++){
			for(j=1;j<=y;j++){
				if(check[i][j]==false){
					printf("Case #%d: NO\n",n);
						break;
				}
			}
			if(j!=y+1) break; 
		}
		if(i!=x+1) continue;
		printf("Case #%d: YES\n",n);
	}
	return 0;
}