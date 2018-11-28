#include<iostream>
#include<cstdio>

using namespace std;

#define F(i,a,b) for(i=a;i<=b;++i)

char board[4][5];

bool won(char ch)
{
	int i,j;
	bool flag=false;

	F(i,0,3){
		flag = true;
		F(j,0,3){
			if(board[i][j]!=ch&&board[i][j]!='T'){
				flag = false;
				break;
			}
		}
		if(flag) return true;

		flag = true;
		F(j,0,3){
			if(board[j][i]!=ch&&board[j][i]!='T'){
				flag = false;
				break;
			}
		}
		if(flag) return true;
	}

	flag = true;
	F(i,0,3){
		if(board[i][i]!=ch&&board[i][i]!='T'){
				flag = false;
				break;
			}
	}
	if(flag) return true;

	flag = true;
	F(i,0,3){
		if(board[i][3-i]!=ch&&board[i][3-i]!='T'){
				flag = false;
				break;
			}
	}
	if(flag) return true;
}

bool rem()
{
	int i,j;

	F(i,0,3) F(j,0,3) if(board[i][j]=='.') return true;
	return false;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);

	int ks=0,t,i;

	scanf("%d",&t);

	while(t--){
		F(i,0,3) scanf("%s",&board[i][0]);

		printf("Case #%d: ",++ks);

		if(won('X')) printf("X won\n");
		else if(won('O')) printf("O won\n");
		else if(rem()) printf("Game has not completed\n");
		else printf("Draw\n");
	}

	return 0;
}