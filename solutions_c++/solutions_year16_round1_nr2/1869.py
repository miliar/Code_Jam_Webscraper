#include<cstdio>
int count[2501];
//int temp[50];
int main(void)
{
    int T;
    int N;
    int temp;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        scanf("%d",&N);
	for(int j=0;j<2501;j++)
	    count[j]=0;
        for(int j=0;j<(2*N-1);j++)
	{
	    for(int k=0;k<N;k++)
	    {
	        scanf("%d",&temp);
		count[temp]++;
	    }
	}
	printf("Case #%d:",i);
        for(int j=1;j<2501;j++)
            if(count[j]%2)
		printf(" %d",j);
	printf("\n");
    }
    return 0;
}
