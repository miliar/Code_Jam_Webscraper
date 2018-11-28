#include<stdio.h>
int main()
{
	FILE *op = fopen("Output1.TXT", "w");
	FILE *ip = fopen("A-small-attempt1.in", "r");
	int test_case=1, T, x, i=0, a[4][4], b[4][4],row1, row2, count=0, flag;
	fscanf(ip, "%d", &T);
	while(test_case<=T)
	{
		fscanf(ip, "%d", &row1);
		row1--;
		x=0;
		while(x<4)
		{
			fscanf(ip,"%d %d %d %d", &a[x][0], &a[x][1], &a[x][2], &a[x][3]);
			x++;		
		}
		
		fscanf(ip, "%d", &row2);
		row2--;
		x=0;
		while(x<4)
		{
				fscanf(ip,"%d %d %d %d", &b[x][0], &b[x][1], &b[x][2], &b[x][3]);
				x++;
		}
		count=0;		
		for(i=0; i<4; i++)
		{
			if(b[row2][i]==a[row1][0]||b[row2][i]==a[row1][1]||b[row2][i]==a[row1][2]||b[row2][i]==a[row1][3])
					{
						count++;
						flag = b[row2][i];
					}
		}
				
		
		if(count==1)
			fprintf(op,"Case #%d: %d\n",test_case, flag);
		else if(count>1)
			fprintf(op,"Case #%d: Bad magician!\n", test_case);
		else
			fprintf(op,"Case #%d: Volunteer cheated!\n", test_case);
	test_case++;
	}
	fclose(ip);
	fclose(op);
	return 0;
}
