#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

const int MAXN=110;

int T,N,M;
int used[MAXN][MAXN];
int ar[MAXN][MAXN];

int f(int x,int y){
	
	int fl=0;
	
	for(int i=1;i<=M;i++)
		if(!used[x][i] && ar[x][i]!=ar[x][y])
			fl=1;
	
	if(!fl){
		for(int i=1;i<=M;i++)
			used[x][i]=1;
		return 0;
	}
	
	fl=0;
	
	for(int i=1;i<=N;i++)
		if(!used[i][y] && ar[i][y]!=ar[x][y])
			fl=1;
	
	if(!fl){
		for(int i=1;i<=N;i++)
			used[i][y]=1;
		return 0;
	}
	
	return 1;
}

int main(){
	
	scanf(" %d",&T);
	
	for(int t=1,fl;t<=T;t++){
		
		scanf("%d %d",&N,&M);
		
		for(int i=1;i<=N;i++)
			for(int j=1;j<=M;j++)
				scanf(" %d",&ar[i][j]);
		
		memset(used,0,sizeof used);
		fl=0;
		
		for(int i=1;i<=100;i++){
			for(int j=1;j<=N;j++){
				for(int k=1;k<=M;k++){
					if(ar[j][k]==i && !used[j][k])
						if(f(j,k)){
							fl=1;
							break;
						}
				}
				if(fl)	break;
			}
			if(fl)	break;
		}
		
		if(fl)	printf("Case #%d: NO\n",t);
		else printf("Case #%d: YES\n",t);
	}
	
	return 0;
}
