#include<stdio.h>

int main()
{
	int tcase = 0;
	FILE *rfp = fopen("test.txt","r");
	FILE *wfp = fopen("output.txt","w");
	if(fscanf(rfp,"%d",&tcase)<=0){}
	else for(int i=0;i<tcase;i++)
	{
		int fAns,sAns;

	        fscanf(rfp,"%d",&fAns);

		int fArray[4],k = 0,j =0,tmp;

		for(j=0;j<4;j++)
		{
			if(j == (fAns-1))
			for(k=0;k<4;k++)
			{
				fscanf(rfp,"%d",&fArray[k]);
				printf("%d\t",fArray[k]);
			}
			else for(k=0;k<4;k++)fscanf(rfp,"%d",&tmp);		
		}


	        fscanf(rfp,"%d",&sAns);

		int sArray[4];

		for(j=0;j<4;j++)
		{
			if(j == (sAns-1))
			for(k=0;k<4;k++)
			{
				fscanf(rfp,"%d",&sArray[k]);
				printf("%d\t",sArray[k]);
			}
			else for(k=0;k<4;k++)fscanf(rfp,"%d",&tmp);		
		}

		int count = 0,flg=1,var;
		for(j=0;j<4;j++)
		{
			
			for(k=0;k<4;k++)
			{
				if(fArray[j] == sArray[k])
				{
					if((++count)>1)
					{
						fprintf(wfp,"%s%d%s\n","Case #",i+1,": Bad magician!");
						break;

					}
					var = sArray[k];
				}
			}
			if(count>1){flg=0;break;}
		}

		if(!count)fprintf(wfp,"%s%d%s\n","Case #",i+1,": Volunteer cheated!");
		else if(flg) fprintf(wfp,"%s%d%s%d\n","Case #",i+1,": ",var); 
	}
	return 0;
}
							

