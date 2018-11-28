#include<stdio.h>
#include<stdlib.h>
#include<iostream>

using namespace std;

main()
{
	FILE *fid=fopen("A-small-attempt1.in","r");
	FILE *fop=fopen("A-small-attempt1.op","w");
	
	int n,sn,sr1,sr2,t,i,j;
	int conf1[4][4],conf2[4][4];

	int count;
	fscanf(fid,"%d",&n);
	for(t=0;t<n;t++)
	{
		fscanf(fid,"%d",&sr1);
		sr1--;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				fscanf(fid,"%d",&conf1[i][j]);
				
		fscanf(fid,"%d",&sr2);
		sr2--;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				fscanf(fid,"%d",&conf2[i][j]);
		
		sn=-1;
		count=0;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(conf1[sr1][i]==conf2[sr2][j])
				{
					sn=conf1[sr1][i];
					count++;
				}
			}
		}
				
		switch(count)
		{
			case 1:	fprintf(fop,"Case #%d: %d\n",t+1,sn);	break;
			case 0: fprintf(fop,"Case #%d: Volunteer Cheated!\n",t+1);	break;
			default: fprintf(fop,"Case #%d: Bad Magician!\n",t+1);
		}
	}
}
