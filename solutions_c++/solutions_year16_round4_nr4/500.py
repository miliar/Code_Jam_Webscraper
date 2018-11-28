#include<bits/stdc++.h>
using namespace std;
int T;
int N;
string S[4];
int SS[4][4];
int main()
{
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++){
		scanf("%d",&N);
		for(int i=0;i<N;i++){
			cin >> S[i];
		}
		for(int i=0;i<N;i++){
			for(int j=0;j<N;j++){
				SS[i][j]=S[i][j]-'0';
			}
		}
		int ans=2000;
		int X[4][4];int Xnum[4];
		for(int i=0;i<N;i++)Xnum[i]=0;
		for(int i=0;i<1<<(N*N);i++){
			for(int j=0;j<N;j++)Xnum[j]=0;
			for(int j=0;j<N*N;j++){
				if((i>>j)&1){
					X[j/N][j%N]=1;
					Xnum[j/N]*=2;Xnum[j/N]++;
				}
				else {
					X[j/N][j%N]=0;
					Xnum[j/N]*=2;
				}
			}
			bool F=true;
			for(int j=0;j<N;j++){
				for(int k=0;k<N;k++){
					if(SS[j][k]==1&&X[j][k]==0)F=false;
				}
			}
			if(!F)continue;
			/*
			printf("%d\n",i);
			for(int j=0;j<N;j++){
				printf("%d:%d\n",j,Xnum[j]);
			}*/
			for(int j=0;j<N;j++){
				for(int k=0;k<N;k++){
					if((Xnum[j]&Xnum[k])!=0&&Xnum[j]!=Xnum[k])F=false;
				}
			}
			if(!F)continue;
			
			for(int j=0;j<N;j++){
				bool FF=false;
				for(int k=0;k<N;k++){
					if(X[j][k]==1)FF=true;
				}
				if(!FF)F=false;
			}
			if(!F)continue;
			int cou11[4];int cou12[4];
			for(int j=0;j<N;j++){
				cou11[j]=0;
				for(int k=0;k<N;k++){
					if(X[j][k]==1)cou11[j]++;
				}
			}
			for(int j=0;j<N;j++){
				cou12[j]=0;
				for(int k=0;k<N;k++){
					if(X[k][j]==1)cou12[j]++;
				}
			}
			for(int j=0;j<N;j++){
				for(int k=0;k<N;k++){
					if(X[j][k]==1&&cou11[j]!=cou12[k]){
						F=false;
					}
				}
			}
			if(!F)continue;
			int cou=0;
			for(int j=0;j<N;j++){
				for(int k=0;k<N;k++){
					if(SS[j][k]==0&&X[j][k]==1)cou++;
				}
			}
			/*
			if(cou==3){
				for(int j=0;j<N;j++){
					for(int k=0;k<N;k++){
						printf("%d ",X[j][k]);
					}
					printf("\n");
				}
			}*/
			ans=min(ans,cou);
		}
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}
