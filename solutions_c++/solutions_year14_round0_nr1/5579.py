#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc,char **argv)
{
	int t,T;
	scanf("%d\n",&T);
	for (t=1;t<=T;t++){
		int q1,q2;
		int row,col;
		int b1[4][4],b2[4][4];
		int c1,c2;
		int ans=0;
		scanf("%d\n",&q1);
		for (row=0;row<4;row++){
			for (col=0;col<4;col++){
				scanf("%d ",&b1[row][col]);
			}
		}
		scanf("%d\n",&q2);
		for (row=0;row<4;row++){
			for (col=0;col<4;col++){
				scanf("%d ",&b2[row][col]);
			}
		}
		for (c1=0;c1<4;c1++){
			for (c2=0;c2<4;c2++){
				if (b1[q1-1][c1]==b2[q2-1][c2]){
					if (ans>0){
						ans=-1;// multiple answers, bad magician!
					}
					else if (ans==0)ans=b2[q2-1][c2];
				}
			}
		}
		if (ans>0){
			printf("Case #%d: %d\n",t,ans);
		}
		else if (ans==0){
			printf("Case #%d: Volunteer cheated!\n",t);
		}
		else{
			printf("Case #%d: Bad magician!\n",t);
		}
	}
	return 0;
}
