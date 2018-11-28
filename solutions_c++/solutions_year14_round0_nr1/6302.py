#include<stdio.h>
#include<stdlib.h>
int main(void)
{
	int test=0,count;
	FILE *fin=fopen("in.txt","r");
	FILE *fout=fopen("out.txt","w");
	fscanf(fin,"%d",&count);
	int a[5][5],b[5][5];
	while(count--)
	{
		test++;
		int n,m;
		fscanf(fin,"%d",&n);
		int i,j;
		for(i=0;i<4;++i)
		{
			for(j=0;j<4;++j)
			{
				fscanf(fin,"%d",&a[i][j]);
			}
		}
		fscanf(fin,"%d",&m);
		for(i=0;i<4;++i)
		{

			for(j=0;j<4;++j)
			{
				fscanf(fin,"%d",&b[i][j]);
			}
		}
		int flag=0,result=-1;
		for(i=0;i<4;++i)
		{

			for(j=0;j<4;++j)
			{
				if(a[n-1][i]==b[m-1][j])
				{
					flag++;
					result=a[n-1][i];
				}
			}
		}
		fprintf(fout,"Case #%d: ",test);
		if(flag==0)
		{
			fprintf(fout,"Volunteer cheated!\n");
		}
		else if(flag>1)
		{
			fprintf(fout,"Bad magician!\n");
		}
		else
		{

			fprintf(fout,"%d\n",result);
		}

	}
	fclose(fin);
	fclose(fout);
	return 0;
}