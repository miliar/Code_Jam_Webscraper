#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<vector>
#include<math.h>
#include<stdlib.h>
#include<set>
#include<ctype.h>
using namespace std;

#define X first
#define Y second
typedef long long ll;
typedef pair<int,int> Pi;

int is_swaped;
int chk[55][55];
int click[2];

void output(int R, int C)
{
	if(is_swaped)swap(R, C);
	for(int i=0;i<R;i++){
		for(int j=0;j<C;j++){
			int x=i, y=j;
			if(is_swaped)swap(x, y);
			if(click[0] == x && click[1] == y)printf("c");
			else if(chk[x][y])printf("*");
			else printf(".");
		}
		puts("");
	}
}

bool solve(int R, int C, int M)
{
	if(M==0){click[0] = 0, click[1] = 0;output(R, C);return true;}
	int rest = R*C - M;
	int i, j;
	if(rest >= 9){
		int cnt = 0;
		for(i=0;i<R-2;i++)for(j=0;j<C-2;j++){
			chk[i][j] = 1, cnt++;
			if(cnt == M){
				click[0] = R-1, click[1] = C-1;
				output(R, C);return true;
			}
		}
		for(i=0;i<R-3;i++){
			chk[R-3][C-3] = 0;
			chk[i][C-2] = chk[i][C-1] = 1;
			cnt++;
			if(cnt == M){
				click[0] = R-1, click[1] = C-1;
				output(R, C);return true;
			}
			chk[R-3][C-3] = 1;
			cnt++;
			if(cnt == M){
				click[0] = R-1, click[1] = C-1;
				output(R, C);return true;
			}
		}
		for(i=0;i<C-3;i++){
			chk[R-3][C-3] = 0;
			chk[R-2][i] = chk[R-1][i] = 1;
			cnt++;
			if(cnt == M){
				click[0] = R-1, click[1] = C-1;
				output(R, C);return true;
			}
			chk[R-3][C-3] = 1;
			cnt++;
			if(cnt == M){
				click[0] = R-1, click[1] = C-1;
				output(R, C);return true;
			}
		}
		printf("??");
		return true;
	}
	if(rest == 2 || rest == 3 || rest == 5 || rest == 7)return false;
	if(rest == 4){
		click[0] = click[1] = 0;
		for(i=0;i<R;i++)for(j=0;j<C;j++)if(i>1||j>1)chk[i][j] = 1;
		output(R, C);
		return true;
	}
	if(rest == 6){
		click[0] = click[1] = 0;
		for(i=0;i<R;i++)for(j=0;j<C;j++)if(i>2||j>1)chk[i][j] = 1;
		output(R, C);
		return true;
	}
	if(rest == 8){
		click[0] = click[1] = 0;
		for(i=0;i<R;i++)for(j=0;j<C;j++)if(i>2||j>2)chk[i][j] = 1;
		chk[2][2] = 1;
		output(R, C);
		return true;
	}
	printf("???");
	return true;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int Tc;
	scanf("%d",&Tc);
	for(int tt=1;tt<=Tc;tt++){
		memset(chk,0,sizeof chk);
		is_swaped = 0;
		printf("Case #%d:\n", tt);
		int R, C, M;
		scanf("%d%d%d",&R,&C,&M);
		if(M == R*C - 1){
			for(int i=0;i<R;i++){for(int j=0;j<C;j++)printf("%c",(!i&&!j)?'c':'*');puts("");}
			continue;
		}
		if(C<=2){
			is_swaped = 1;
			swap(R, C);
		}
		if(R == 1){
			for(int i=0;i<M;i++)chk[0][i] = 1;
			click[0] = 0, click[1] = C-1;
			output(R, C);
			continue;
		}
		if(R == 2){
			if(C==1 && M==0);
			else if((M&1) || R*C-M == 2){printf("Impossible\n");continue;}
			for(int i=0;i<M/2;i++)chk[0][i] = chk[1][i] = 1;
			click[0] = 0, click[1] = C-1;
			output(R, C);
			continue;
		}
		if(!solve(R, C, M))printf("Impossible\n");
	}
	return 0;
}
