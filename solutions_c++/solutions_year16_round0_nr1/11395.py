#include<cstdio>

int main()
{
	int T,N,count,numn,i,j,NCP,temp,time;
	scanf("%d",&T);
//	FILE *fp;
//	fp = fopen("data4.txt","w");
	for(count=1;count<=T;count++)
	{
		int number[10]={0};
		scanf("%d",&N);
		if(N==0)
		{
			printf("Case #%d: INSOMNIA\n",count);
//			fprintf(fp,"Case #%d: INSOMNIA\n",count);
			continue;
		}
		else
		{
			for(time=1;number[0]==0||number[1]==0||number[2]==0||number[3]==0||number[4]==0||number[5]==0||number[6]==0||number[7]==0||number[8]==0||number[9]==0;time++)
			{
				NCP=N*time;
			//	printf("%d\n",NCP);
				
				numn=1;
				while(NCP>=10)
				{
					NCP/=10;
					numn++;
				}
				NCP=N*time;
				for(j=0;j<numn;j++)
				{
					temp=NCP%10;
					number[temp]=1;
					NCP/=10;
				}
				NCP=N*time;
			//	printf("%d %d %d %d %d %d %d %d %d %d\n",number[0],number[1],number[2],number[3],number[4],number[5],number[6],number[7],number[8],number[9]);
			}
			printf("Case #%d: %d\n",count,NCP);
//			fprintf(fp,"Case #%d: %d\n",count,NCP);
		}
	}
	return 0;
} 
