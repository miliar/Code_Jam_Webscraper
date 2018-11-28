#include <stdio.h>

void main() 
{
	FILE *in = fopen("A-small-attempt0.in", "r");
	FILE *out = fopen("A-small-attempt0.out", "w");
	int n, N, select1, select2, cards1[4][4], cards2[4][4], check[16];
	int i,j, flag, ans;

	fscanf(in,"%d",&N);

	n=0;
	while(n<N) {

		fscanf(in,"%d",&select1);
		for(i=0;i<4;i++)
			fscanf(in,"%d %d %d %d",&cards1[i][0],&cards1[i][1],&cards1[i][2],&cards1[i][3]);
		
		fscanf(in,"%d",&select2);
		for(i=0;i<4;i++)
			fscanf(in,"%d %d %d %d",&cards2[i][0],&cards2[i][1],&cards2[i][2],&cards2[i][3]);
		
		for(i=0;i<16;i++)
			check[i]=0;

		for(i=0;i<4;i++)
		{
			check[ cards1[select1-1][i]-1 ]++;
			check[ cards2[select2-1][i]-1 ]++;
		}

		flag = 0;
		ans = 0;
		for(i=0;i<16;i++)
		{
			if( check[i] >= 2 )
			{
				flag++;
				ans = i+1;
			}
		}

		if(flag == 0 )
			fprintf(out,"Case #%d: Volunteer cheated!\n",n+1);		
		else if(flag == 1 )
			fprintf(out,"Case #%d: %d\n",n+1,ans);		
		else 
			fprintf(out,"Case #%d: Bad magician!\n",n+1);
		++n;
	}

}