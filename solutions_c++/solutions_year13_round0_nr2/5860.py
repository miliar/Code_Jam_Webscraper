#include<iostream>
#include<cstdio>

using namespace std;

#define F(i,a,b) for(i=a;i<=b;++i)

int board[101][101],row,col;

bool chk()
{
	int i,j,k;
	bool flag;

	F(i,1,row) board[i][0] = 0;
	F(j,1,col) board[0][j] = 0;

	// pass 1

	F(i,1,row){
		flag = true;
		F(j,2,col)
			if(board[i][1]!=board[i][j]){
				flag=false;
				break;
			}
		if(flag) board[i][0] = 1;
	}

	F(j,1,col){
		flag = true;
		F(i,2,row)
			if(board[1][j]!=board[i][j]){
				flag=false;
				break;
			}
		if(flag) board[0][j] = 1;
	}

	// pass 2

	F(i,1,row){
		if(board[i][0]) continue;

		//printf("row %d\n",i);
		
		F(k,1,col) if(board[0][k]==0) break;
		if(k>col) continue;

		//printf("k %d\n",k);

		F(j,1,col)
			if( (board[i][k]<board[i][j])||(board[i][k]!=board[i][j]&&board[0][j]==0) ) return false;
	}

	F(j,1,col){
		if(board[0][j]) continue;

		//printf("col %d\n",j);

		F(k,1,row) if(board[k][0]==0) break;
		if(k>row) continue;

		//printf("k %d\n",k);

		F(i,1,row)
			if( (board[k][j]<board[i][j])||board[k][j]!=board[i][j]&&board[i][0]==0) return false;
	}

	return true;
}


int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);

	int ks=0,t,i,j;

	scanf("%d",&t);

	while(t--){
		scanf("%d%d",&row,&col);
		F(i,1,row) F(j,1,col) scanf("%d",&board[i][j]);

		printf("Case #%d: %s\n",++ks,chk()?"YES":"NO");
	}

	return 0;
}