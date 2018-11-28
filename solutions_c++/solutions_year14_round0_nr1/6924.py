#include<stdio.h>
#include<stdlib.h>

int main()
{
	int chose1[4],chose2[4],com[4]={0};
	int t,i,j,temp,k,count=0;
	int sel,tcase=1;
	FILE *fp1,*fp2;

	fp1 = fopen("prob1.txt","r");
	fp2 = fopen("output.txt","w");
	fscanf(fp1,"%d",&t);
	//printf("%d",t);
	while(tcase<=t)
	{
		fscanf(fp1,"%d",&sel);
		for(i=0;i<4;i++)
		{
			if(i != (sel-1))
			{
				for(j=0;j<4;j++)
				{
					fscanf(fp1,"%d",&temp);
				//printf("%d ",mat[i][j]);
				}
			}
			else
			{
				for(j=0;j<4;j++)
				{
					fscanf(fp1,"%d",&chose1[j]);
				}
			}
		}

		fscanf(fp1,"%d",&sel);
		for(i=0;i<4;i++)
		{
			if(i != (sel-1))
			{
				for(j=0;j<4;j++)
				{
					fscanf(fp1,"%d",&temp);
					//printf("%d ",mat[i][j]);
				}
			}
			else
			{
				for(j=0;j<4;j++)
				{
					fscanf(fp1,"%d",&chose2[j]);
					for(k=0;k<4;k++)
					{
						if(chose2[j] == chose1[k])
						{
							com[count] = chose2[j];
							count ++;
						}
					}
				}
			}
		}



		fprintf(fp2,"Case #%d: ",tcase);
		if(count == 0)
		{
			fprintf(fp2,"Volunteer cheated!");
			fprintf(fp2,"\n");
		}
		if(count == 1)
		{
			fprintf(fp2,"%d",com[0]);
			fprintf(fp2,"\n");
		}
		if(count > 1)
		{
			fprintf(fp2,"Bad magician!");
			fprintf(fp2,"\n");
		}

		count = 0;
		tcase++;
	}
	fclose(fp2);
	fclose(fp1);
	return 0 ;
}
