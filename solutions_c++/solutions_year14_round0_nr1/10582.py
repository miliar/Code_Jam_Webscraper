#include<stdio.h>

int main()
{
	int t,i,j,k,found;
	int ans,ans1,ans2;
	int mat1[4][4],mat2[4][4];
	scanf("%d",&t);
	for(i = 1;i <= t;i++) {
		found = 0;
		scanf("%d",&ans1);
		ans1--;
		for(j = 0;j < 4;j++) {
			for(k = 0;k < 4;k++) {
				scanf("%d",&mat1[j][k]);
			}
		}
		scanf("%d",&ans2);
		ans2--;
		for(j = 0;j < 4;j++) {
			for(k = 0;k < 4;k++) {
				scanf("%d",&mat2[j][k]);
			}
		}
		for(j = 0;j < 4;j++) {
			for(k = 0;k < 4;k++) {
				if(mat1[ans1][j] == mat2[ans2][k]) {
					if(found == 0) {
						found = 1;
						ans = mat1[ans1][j];
					} else found = 2;					
				}
			}
		}
		if(found == 1) printf("Case #%d: %d\n",i,ans); 
		else if(found == 2) printf("Case #%d: Bad magician!\n",i);
		else printf("Case #%d: Volunteer cheated!\n",i);
	}
	return 0;
}
