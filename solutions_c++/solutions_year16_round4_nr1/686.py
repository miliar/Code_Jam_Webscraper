#include<bits/stdc++.h>
using namespace std;
int T;
int N,R,P,S;
//P:0,R:1,S:2
int WinP[13][1<<13];
int WinR[13][1<<13];
int WinS[13][1<<13];
int main()
{
	scanf("%d",&T);
	WinP[0][0]=0;
	for(int i=1;i<=12;i++){
		for(int j=0;j<(1<<i);j++){
			if(WinP[i-1][j/2]==0){
				WinP[i][j]=0;j++;
				WinP[i][j]=1;
			}
			else if(WinP[i-1][j/2]==1){
				WinP[i][j]=1;j++;
				WinP[i][j]=2;
			}
			else{
				WinP[i][j]=0;j++;
				WinP[i][j]=2;
			}
		}
	}
	for(int i=1;i<=12;i++){
		for(int j=(i-1);j>=0;j--){
			for(int l=0;(l*(1<<(j+1))+(1<<j)+(1<<j)-1)<(1<<i);l++){
				bool F=false;
				for(int k=0;k<(1<<j);k++){
					if(WinP[i][l*(1<<(j+1))+(1<<j)+k]<WinP[i][l*(1<<(j+1))+k]){
						F=true;break;
					}
					else if(WinP[i][l*(1<<(j+1))+(1<<j)+k]>WinP[i][l*(1<<(j+1))+k]){
						F=false;break;
					}
				}
				if(F){
					for(int k=0;k<(1<<j);k++){
						swap(WinP[i][l*(1<<(j+1))+(1<<j)+k],WinP[i][l*(1<<(j+1))+k]);
					}
				}
			}
		}
	}
	WinR[0][0]=1;
	for(int i=1;i<=12;i++){
		for(int j=0;j<(1<<i);j++){
			if(WinR[i-1][j/2]==0){
				WinR[i][j]=0;j++;
				WinR[i][j]=1;
			}
			else if(WinR[i-1][j/2]==1){
				WinR[i][j]=1;j++;
				WinR[i][j]=2;
			}
			else{
				WinR[i][j]=0;j++;
				WinR[i][j]=2;
			}
		}
	}
	for(int i=1;i<=12;i++){
		for(int j=(i-1);j>=0;j--){
			for(int l=0;(l*(1<<(j+1))+(1<<j)+(1<<j)-1)<(1<<i);l++){
				bool F=false;
				for(int k=0;k<(1<<j);k++){
					if(WinR[i][l*(1<<(j+1))+(1<<j)+k]<WinR[i][l*(1<<(j+1))+k]){
						F=true;break;
					}
					else if(WinR[i][l*(1<<(j+1))+(1<<j)+k]>WinR[i][l*(1<<(j+1))+k]){
						F=false;break;
					}
				}
				if(F){
					for(int k=0;k<(1<<j);k++){
						swap(WinR[i][l*(1<<(j+1))+(1<<j)+k],WinR[i][l*(1<<(j+1))+k]);
					}
				}
			}
		}
	}
	WinS[0][0]=2;
	for(int i=1;i<=12;i++){
		for(int j=0;j<(1<<i);j++){
			if(WinS[i-1][j/2]==0){
				WinS[i][j]=0;j++;
				WinS[i][j]=1;
			}
			else if(WinS[i-1][j/2]==1){
				WinS[i][j]=1;j++;
				WinS[i][j]=2;
			}
			else{
				WinS[i][j]=0;j++;
				WinS[i][j]=2;
			}
		}
	}
	for(int i=1;i<=12;i++){
		for(int j=(i-1);j>=0;j--){
			for(int l=0;(l*(1<<(j+1))+(1<<j)+(1<<j)-1)<(1<<i);l++){
				bool F=false;
				for(int k=0;k<(1<<j);k++){
					if(WinS[i][l*(1<<(j+1))+(1<<j)+k]<WinS[i][l*(1<<(j+1))+k]){
						F=true;break;
					}
					else if(WinS[i][l*(1<<(j+1))+(1<<j)+k]>WinS[i][l*(1<<(j+1))+k]){
						F=false;break;
					}
				}
				if(F){
					for(int k=0;k<(1<<j);k++){
						swap(WinS[i][l*(1<<(j+1))+(1<<j)+k],WinS[i][l*(1<<(j+1))+k]);
					}
				}
			}
		}
	}
	/*
	for(int i=0;i<3;i++){
		for(int j=0;j<(1<<i);j++){
			printf("%d ",WinS[i][j]);
		}
		printf("\n");
	}*/
	for(int cas=1;cas<=T;cas++){
		scanf("%d%d%d%d",&N,&R,&P,&S);
		printf("Case #%d: ",cas);
		int cou0=0,cou1=0,cou2=0;
		bool F=false;
		for(int i=0;i<(1<<N);i++){
			if(WinP[N][i]==0)cou0++;
			else if(WinP[N][i]==1)cou1++;
			else cou2++;
		}
		//printf("%d %d %d\n",cou0,cou1,cou2);
		if((cou0==P&&cou1==R)&&cou2==S)F=true;
		if(F){
			for(int i=0;i<(1<<N);i++){
				if(WinP[N][i]==0)printf("P");
				else if(WinP[N][i]==1)printf("R");
				else printf("S");
			}
			printf("\n");
			continue;
		}
		cou0=0,cou1=0,cou2=0;
		F=false;
		for(int i=0;i<(1<<N);i++){
			if(WinR[N][i]==0)cou0++;
			else if(WinR[N][i]==1)cou1++;
			else cou2++;
		}
		
		if((cou0==P&&cou1==R)&&cou2==S)F=true;
		if(F){
			for(int i=0;i<(1<<N);i++){
				if(WinR[N][i]==0)printf("P");
				else if(WinR[N][i]==1)printf("R");
				else printf("S");
			}
			printf("\n");
			continue;
		}
		cou0=0,cou1=0,cou2=0;
		F=false;
		for(int i=0;i<(1<<N);i++){
			if(WinS[N][i]==0)cou0++;
			else if(WinS[N][i]==1)cou1++;
			else cou2++;
		}
		if((cou0==P&&cou1==R)&&cou2==S)F=true;
		if(F){
			for(int i=0;i<(1<<N);i++){
				if(WinS[N][i]==0)printf("P");
				else if(WinS[N][i]==1)printf("R");
				else printf("S");
			}
			printf("\n");
			continue;
		}
		printf("IMPOSSIBLE\n");
	}
	return 0;
}
