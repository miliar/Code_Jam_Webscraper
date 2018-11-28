//GCJ - Problem A. Magic Trick
#include<stdio.h>
int main()
{
    FILE *C;
	int test;
	int array[4][4]={0};
	int res[4]={0};
	int i,j;
	int volans;
	int ans;
	int counter;
	int co;
	scanf("%d",&test);
	C=fopen("a.txt","w+");
	for(co=1;co<=test;co++)
	{
		counter=0;
		scanf("%d",&volans);
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		scanf(" %d",&array[i][j]);
		for(i=0;i<4;i++)
		{
		res[i]=array[volans-1][i];
		printf("%d ",res[i]);
		}
		scanf("%d",&volans);
		for(i=0;i<4;i++)
		for(j=0;j<4;j++)
		scanf("%d",&array[i][j]);
		for(i=0;i<4;i++)
		{
		    for(j=0;j<4;j++)
		    {
                if(res[i]==array[volans-1][j])
                {
                    counter++;
                    ans=res[i];
                }
		    }
		}
		if(counter==1)
		{
			fprintf(C,"Case #%d: %d\n",co,ans);
		}
		if(counter==0)
		{
			fprintf(C,"Case #%d: Volunteer cheated!\n",co);
		}
		if(counter>1)
		{
			fprintf(C,"Case #%d: Bad magician!\n",co);
		}

	}
}
