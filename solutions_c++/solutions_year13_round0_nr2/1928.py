#include <stdio.h>
#include <stdlib.h>
#define MIN(x,y) (((x)<(y))?(x):(y))
int n,m,arr[101][101];
int getres(){
	int rs1[101],rs2[101];
	for(int i=0;i<n;i++){
		int res=0;
		for(int j=0;j<m;j++)
			arr[i][j]>res?res=arr[i][j]:0;
		rs1[i]=res;
	}
	for(int j=0;j<m;j++){
		int res=0;
		for(int i=0;i<n;i++)
			arr[i][j]>res?res=arr[i][j]:0;
		rs2[j]=res;
	}
	for(int i=0;i<n;i++){
		for(int j=0;j<m;j++){
			if(arr[i][j]!=MIN(rs1[i],rs2[j]))
				return 0;
		}
	}
	return 1;
}
int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++){
				scanf("%d",&arr[i][j]);
			
			}
			printf("Case #%d: %s\n",t,getres()?"YES":"NO");
	}
}