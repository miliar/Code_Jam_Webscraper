#include "stdafx.h"

int main(int argc, char* argv[])
{
	int n;	//case ­Ó¼Æ
	int card[4][4];
    int ch_row;
	int temp[4];
	int ch_num;
	int count;
	int i,j,k,l;
	FILE *IN1, *OUT1;

	IN1 = fopen ("A-small-attempt3.in" , "rb");
    OUT1 = fopen ("A-small-attempt3.out" , "wb");
    fscanf(IN1,"%d",&n);

	for(i=0;i<n;i++)
	{
		count = 0;
		fscanf(IN1,"%d",&ch_row);
		for(j=0;j<4;j++)
			for(k=0;k<4;k++)
				fscanf(IN1,"%d",&card[j][k]);
		for(j=0;j<4;j++)
			temp[j] = card[ch_row - 1][j];
		
		fscanf(IN1,"%d",&ch_row);
		for(j=0;j<4;j++)
			for(k=0;k<4;k++)
				fscanf(IN1,"%d",&card[j][k]);
	
		for(j=0;j<4;j++)
			for(k=0;k<4;k++)
			{
				if(temp[j] == card[ch_row - 1][k])
				{	
					count++;
					ch_num = card[ch_row - 1][k];
				}
			}
		if(count == 0)
			fprintf(OUT1,"Case #%d: Volunteer cheated!\r\n",i+1);
		else if(count == 1)
			fprintf(OUT1,"Case #%d: %d\r\n",i+1,ch_num);
		else
			fprintf(OUT1,"Case #%d: Bad magician!\r\n",i+1);
	}
	return 0;
}

