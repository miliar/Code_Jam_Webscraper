#include <iostream>
#include <cstdio>
using namespace std;

int N,M,ar[105][105];
bool Ans;
bool Col[105];
void CheckRow();
void CheckCol();

int main(){
	int T;
	scanf("%d",&T);
	for(int Case=1; Case<=T; Case++){
		Ans=true;
		scanf("%d%d",&N,&M);
		for(int i=0; i<N; i++)
			for(int j=0; j<M; j++)
				scanf("%d",&ar[i][j]);
		Ans=true;
		CheckRow();
		if(Ans){CheckCol();}
		printf("Case #%d: ",Case);
		Ans?printf("YES\n"):printf("NO\n");
	}
	return 0;
}

void CheckRow(){
	memset(Col,false,sizeof(Col));
	for(int i=0; i<N; i++){
		bool First=false;
		int n=-1;
		int Stand;
		while(!First){
			First=true;
			Stand=ar[i][++n];
			for(int j=0; j<M; j++){
				if(j==n)continue;
				if(ar[i][j]!=Stand){
					bool Same=true;
					if(ar[i][j]>Stand){First=false; break;}
					if(Col[j])continue;
					for(int k=1; k<N; k++) if(ar[k][j]!=ar[k-1][j]){Same=false; break;}
					if(Same) Col[j]=true;
					else {First=false; break;}
				}
			}
			if(n>=M)break;
		}
		if(!First){
			Ans=false; break;
		}
	}
}

void CheckCol(){
	bool Row[105]; memset(Row,false, sizeof(Row));
	for(int i=0; i<M; i++){
		if(!Col[i]){
			bool First=false;
			int Stand;
			int n=-1;
			while(!First){
				First=true;
				Stand=ar[++n][i];
				for(int j=1; j<N; j++) 
					if(ar[j][i]!=Stand){
						bool Same=true;
						if(ar[j][i]>Stand){First=false; break;}
						if(Row[j]) continue;
						for(int k=1; k<M; k++) if(ar[j][k]!=ar[j][k-1]){Same=false; break;}
						if(Same) Row[j]=true;
						else {First=false; break;}
					}
				if(n>=N)break;
			}
			if(!First){
				Ans=false; break;
			}
		}
	}
}
