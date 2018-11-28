#include<stdio.h>
#include<stdlib.h>

main()
{
	int t, row1,row2,a[4][4],b[4][4],count,l,i,j,ans;
	FILE *in, *out;
	in=fopen("input.txt","r");
	out=fopen("output.txt","w");
	fscanf(in,"%d",&t);
	
	for(l=1;l<=t;l++)
	{	count=0;
		fscanf(in,"%d",&row1);
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		fscanf(in,"%d",&a[i][j]);
		
		fscanf(in,"%d",&row2);
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		fscanf(in,"%d",&b[i][j]);
		
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		{
			if(a[row1-1][i]==b[row2-1][j])
			{
			ans=a[row1-1][i];
			count++;}
		
		}
		
		if(count==0)
		fprintf(out,"Case #%d: Volunteer cheated!\n",l);
		else if(count==1)
		{
		fprintf(out,"Case #%d: %d\n",l,ans);
		}	
		else
		fprintf(out,"Case #%d: Bad magician!\n",l);
	}
	fclose(in);
	fclose(out);
	
	return 0;
}
