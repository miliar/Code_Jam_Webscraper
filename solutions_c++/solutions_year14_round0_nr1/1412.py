#include <cstdio>

int T;
int pos[22];
int grid[2][4][4];
int r[2];
int num;

int main()
{
	scanf("%d", &T);

	for(int q=1; q<=T; q++) {
		for(int k=0; k<2; k++) {
			scanf("%d", &r[k]);
			r[k]--;
			for(int i=0; i<4; i++) {
				for(int j=0; j<4; j++) {
					scanf("%d", &grid[k][i][j]);
				}
			}
		}
		for(int i=1; i<=16; i++) pos[i]=0;
		for(int i=0; i<4; i++) pos[grid[0][r[0]][i]]|=1;
		for(int i=0; i<4; i++) pos[grid[1][r[1]][i]]|=2;
		num=-1;
		for(int i=1; i<=16; i++) {
			if(pos[i]==3) {
				if(num==-1) num=i;
				else {
					num=-2;
					break;
				}
			}
		}
		if(num==-1) printf("Case #%d: Volunteer cheated!\n", q);
		else if(num==-2) printf("Case #%d: Bad magician!\n", q);
		else printf("Case #%d: %d\n", q, num);
	}

	return 0;
}
