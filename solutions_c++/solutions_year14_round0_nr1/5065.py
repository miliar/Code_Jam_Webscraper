#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	FILE *fp,*fp1;
	fp=fopen("A-small-attempt3.in","r+");
	fp1=fopen("output1","w+");
	int T;
	fscanf(fp,"%d",&T);
	for(int n=1;n<=T;n++)
	{
		int row1,row2,card1[16],card2[16],sum=0,num;
		fscanf(fp,"%d",&row1);
		for(int i=0;i<16;i++)
				fscanf(fp,"%d",&card1[i]);
		fscanf(fp,"%d",&row2);
		for(i=0;i<16;i++)
			fscanf(fp,"%d",&card2[i]);
		for(i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(card1[4*(row1-1)+i]==card2[4*(row2-1)+j])
				{
					num=card1[4*(row1-1)+i];
					sum++;
				}
		switch(sum)
		{
		case 0:fprintf(fp1,"Case #%d: Volunteer cheated!\n",n);break;
		case 1:fprintf(fp1,"Case #%d: %d\n",n,num);break;
		default:fprintf(fp1,"Case #%d: Bad magician!\n",n);break;
		}
	}
	return 0;
}