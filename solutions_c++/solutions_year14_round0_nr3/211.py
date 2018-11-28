#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;
char map[55][55];
int main(){
	//freopen("C-large.in","r",stdin);
	//freopen("C-large.out","w",stdout);
	int i,j,m,n,T,x,s,vcase=0;
	scanf("%d",&T);
	while(T--){
		scanf("%d%d%d",&n,&m,&x);
		s=n*m-x;
		printf("Case #%d:\n",++vcase);
		for(i=1;i<=n;i++)
			for(j=1;j<=m;j++)
				map[i][j]='*';
		if(x==0){
			for(i=1;i<=n;i++)
				for(j=1;j<=m;j++)
					map[i][j]='.';
		}
		else if(s==1);
		else if(n==1){
			for(i=1;i<=s;i++)
				map[1][i]='.';
		}
		else if(n==2){
			if(s%2 || s==2){
				printf("Impossible\n");
				continue;
			}
			else{
				for(i=1;i<=s/2;i++){
					map[1][i]='.';
					map[2][i]='.';
				}
			}
		}
		else if(m==1){
			for(i=1;i<=s;i++)
				map[i][1]='.';
		}
		else if(m==2){
			if(s%2 || s==2){
				printf("Impossible\n");
				continue;
			}
			else{
				for(i=1;i<=s/2;i++){
					map[i][1]='.';
					map[i][2]='.';
				}
			}
		}
		else if(s<=2*m){
			if(s%2){
				if(s<8){
					printf("Impossible\n");
					continue;
				}
				else{
					for(i=1;i<=(s-3)/2;i++){
						map[1][i]='.';
						map[2][i]='.';
					}
					map[3][1]='.';
					map[3][2]='.';
					map[3][3]='.';
				}
			}
			else{
				if(s<3){
					printf("Impossible\n");
					continue;
				}
				else{
					for(i=1;i<=s/2;i++){
						map[1][i]='.';
						map[2][i]='.';
					}
				}
			}
		}
		else if(s==2*m+1){
			if(m>3){
				for(i=1;i<m;i++){
					map[1][i]='.';
					map[2][i]='.';
				}
				map[3][1]='.';
				map[3][2]='.';
				map[3][3]='.';
			}
			else{
				printf("Impossible\n");
				continue;
			}
		}
		else if(s%m==1){
			for(i=1;i<=s/m;i++)
				for(j=1;j<=m;j++)
					map[i][j]='.';
			map[s/m+1][1]='.';
			map[s/m+1][2]='.';
			map[s/m][m]='*';
		}
		else{
			for(i=1;i<=s/m;i++)
				for(j=1;j<=m;j++)
					map[i][j]='.';
			for(j=1;j<=s%m;j++)
				map[s/m+1][j]='.';
		}
		map[1][1]='c';
		for(i=1;i<=n;i++){
			for(j=1;j<=m;j++) printf("%c",map[i][j]);
			printf("\n");
		}
	}
	return 0;
}