#include <stdio.h>
#include <algorithm>

using namespace std;

int T, row[2],mat[2][4][4];

int main() {
	scanf("%d",&T);
	for (int c=1;c<=T;c++) {
		for (int x=0;x<=1;x++) {
			scanf("%d",row+x);
			--row[x];
			for (int i=0;i<4;i++)
				for (int j=0;j<4;j++)
					scanf("%d", &mat[x][i][j]);
		}
		int make[8]={mat[0][row[0]][0],mat[0][row[0]][1],mat[0][row[0]][2],mat[0][row[0]][3],mat[1][row[1]][0],mat[1][row[1]][1],mat[1][row[1]][2],mat[1][row[1]][3]};
		sort(make,make+8);
		int tot=0, arr[8];
		for (int x=0;x<7;x++)
			if (make[x]==make[x+1])
				arr[tot++]=make[x];
		printf("Case #%d: ", c);
		if (tot==1)
			printf("%d\n",arr[0]);
		else if (tot>1)
			puts("Bad magician!");
		else
			puts("Volunteer cheated!");
	}
}
