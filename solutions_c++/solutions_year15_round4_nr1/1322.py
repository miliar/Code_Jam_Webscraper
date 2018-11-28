#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

const int mv[4][2] = {
	{0,1}, {0,-1}, {1,0}, {-1,0}
};
char a[110][110];
int task, r, c, ret;


bool canhit(int x, int y, int k){
	int fx =x+mv[k][0], fy=y+mv[k][1];
	while (1<=fx&&fx<=r && 1<=fy&&fy<=c){
		if (a[fx][fy] != '.')
			return true;

		fx += mv[k][0];
		fy += mv[k][1];
	}
	
	return false;
}

void doit(){
	ret = 0;
	for (int i=1; i<=r; i++)
	for (int j=1; j<=c; j++){
		int d = -1;

		if (a[i][j]=='^')
			d = 3;else
		if (a[i][j]=='v')
			d = 2;else
		if (a[i][j]=='<')
			d = 1;else
		if (a[i][j]=='>')
			d = 0;
	
		if (d!=-1 && !canhit(i, j, d)){
			int p=-1;
			for (int k=0; k<4; k++){
				if (canhit(i, j, k)){
					p = k;
					break;
				}
			}

			if (p==-1){
				ret = -1;
				return;
			}

			ret++;
		}
	}
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("b.out","w",stdout);

	scanf("%d", &task);
	for (int CASE = 1; CASE<=task; CASE++){
		memset(a, '.', sizeof(a));
		scanf("%d%d", &r, &c);
		for (int i=1; i<=r; i++)
		for (int j=1; j<=c; j++){
			int cc;
			do{
			scanf("%c", &cc);
			}while (!(cc=='.' || cc=='<' || cc=='>' || cc=='^' || cc=='v'));
			a[i][j] = cc;
		}
		doit();

		if (ret==-1)
			printf("Case #%d: IMPOSSIBLE\n", CASE);else
			printf("Case #%d: %d\n", CASE, ret);
	}

	return 0;
}
