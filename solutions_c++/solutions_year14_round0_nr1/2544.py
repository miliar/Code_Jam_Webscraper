#include <stdio.h>

int main()
{
	int n,i;
	int j,m,row,ans;
	FILE *fs = fopen("B-small-attempt0.in","rt");
	FILE *fp = fopen("output.out","wt");
	fscanf(fs,"%d",&n);

	for(i=0;i<n;i++)
	{
		int Arr[17]={0,};
		ans=0;
		for(j=0;j<2;j++)
		{
			fscanf(fs,"%d",&row);
			for(int t=0;t<16;t++)
			{
				fscanf(fs,"%d",&m);
				if((t/4)+1==row)
					Arr[m]++;
			}
		}
		for(j=1;j<=16;j++)
		{
			if(Arr[j]==2)
			{
				if(ans!=0)
				{
					ans=-1;
					break;
				}
				else
					ans=j;
			}
		}
		if(ans==0)
			fprintf(fp,"Case #%d: Volunteer cheated!\n",i+1);
		else if(ans==-1)
			fprintf(fp,"Case #%d: Bad magician!\n",i+1);
		else
			fprintf(fp,"Case #%d: %d\n",i+1,ans);
	}
	fclose(fs);
	fclose(fp);
	return 0;
}