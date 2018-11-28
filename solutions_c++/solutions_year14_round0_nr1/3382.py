#include <stdio.h>
int main()
{
	FILE *fp,*fo;
	fp=fopen("A-small-attempt2.in","r");
	fo=fopen("outputmagicatt2.o","w");
	int t,r,i,test,num,a[5][5],cnt[17],j,cnt2;
	fscanf(fp,"%d",&t);
	for(test=1;test<=t;test++)
	{
		for(i=1;i<=16;i++)
		cnt[i]=0;
		fscanf(fp,"%d",&r);
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				fscanf(fp,"%d",&a[i][j]);
				if(i==r)
				cnt[a[i][j]]++;
			}
		}
		fscanf(fp,"%d",&r);
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				fscanf(fp,"%d",&a[i][j]);
				if(i==r)
				cnt[a[i][j]]++;
			}
		}
		cnt2=0;
		for(i=1;i<=16;i++)
		{
			if(cnt[i]==2)
			{
				cnt2++;
				num=i;
			}
		}
		//for(i=1;i<=16;i++)
		//printf("%d  ",cnt[i]);
		if(cnt2==1)
		fprintf(fo,"Case #%d: %d\n",test,num);
		else if(cnt2>1)
		fprintf(fo,"Case #%d: Bad magician!\n",test);
		else
		fprintf(fo,"Case #%d: Volunteer cheated!\n",test);
	}
	return 0;
}
