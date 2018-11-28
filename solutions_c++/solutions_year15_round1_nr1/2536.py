#include<stdio.h>
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("outputxxx2.in","w",stdout);
	int i,j,decsum=0,decsum2,temp,maxdec,preentry=0,temp1,count=1,T,N,arr[10001];
	scanf("%d",&T);
	while(T--)
	{
		decsum=0;
		decsum2=0;
		maxdec=0;
		preentry=0;
		scanf("%d",&N);
		for(i=0;i<N;i++)
		{
			scanf("%d",&arr[i]);
			temp=arr[i]-preentry;
			if(temp<0)
			{
				decsum=decsum-temp;
			}
			preentry=arr[i];
			
			if((-temp)>maxdec)
			{
				maxdec=-temp;
			}
		
		}
		for(i=0;i<N-1;i++)
		{
			//temp=arr[i]-arr[i-1];
			if(arr[i]>=maxdec)
			{	
				decsum2=decsum2+maxdec;
				
			}
			else
			{
				decsum2=decsum2+arr[i];
				
			}
			
		}
	
		printf("Case #%d: %d %d\n",count++,decsum,decsum2);
			
	}
}
