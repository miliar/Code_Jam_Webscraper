#include <stdio.h>
#include <string.h>


int t;
int a,b;
int arr1[4][4];
int arr2[4][4];

int main(void)
{
	int i,j,k,total;
	int ck;
	int l=1;
	FILE *fp = fopen("A-small-attempt6.in","r");
	FILE *out = fopen("output.txt","w");
	fscanf(fp,"%d",&t);
	total=t;
	while(t--)
	{

		ck=0;
		fscanf(fp,"%d",&a);
		for(i=0; i<4; i++)
		{
			for(j=0; j<4; j++)
			{
				fscanf(fp,"%d",&arr1[i][j]);
			}
		}
		fscanf(fp,"%d",&b);
		for(i=0; i<4; i++)
		{
			for(j=0; j<4; j++)
			{
				fscanf(fp,"%d",&arr2[i][j]);
			}
		}
		for (i=0; i<4; i++)
		{
			for (j=0; j<4; j++){
				if(arr1[a-1][i] == arr2[b-1][j])
				{
					ck++;
					k=arr1[a-1][i];
				}
			}
		}
		if(ck ==1)
		{
			fprintf(out,"Case #%d: %d",l++,k);
		}	
		else if ( ck ==0)
		{
			fprintf(out,"Case #%d: Volunteer cheated!",l++);
		}
		else
		{
			fprintf(out,"Case #%d: Bad magician!",l++);
		}
		if(l -1 != total)
			fprintf(out,"\n");
	}
	fclose(fp);
	fclose(out);

	return 0;
}
