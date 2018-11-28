#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

int N,M;
int map[105][105];
int MR[105],MC[105];

void init(){
	scanf("%d%d",&N,&M);
	for(int i=1;i<=N;i++){
		for(int j=1;j<=M;j++){
			scanf("%d",&map[i][j]);
		}
	}
	for(int i=1;i<=N;i++){
		MR[i]=0;
		for(int j=1;j<=M;j++) MR[i]=max(MR[i],map[i][j]);
	}
	for(int j=1;j<=M;j++){
		MC[j]=0;
		for(int i=1;i<=N;i++) MC[j]=max(MC[j],map[i][j]);
	}
}

bool work(){
	for(int i=1;i<=N;i++){
		for(int j=1;j<=M;j++) if(MR[i]>map[i][j] && MC[j]>map[i][j]) return 0;
	}
	return 1;
}

int main(){
	int T,T2=0; scanf("%d",&T);
	while(T--){
		printf("Case #%d: ",++T2);
		init();
		if(work()) printf("YES\n"); else printf("NO\n");
	}
	return 0;
}