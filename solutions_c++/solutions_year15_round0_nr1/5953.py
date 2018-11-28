#include<stdio.h>
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("zzz.in","w",stdout);
	int i,T,S,f,s,count=1;
	char arr[100000]={0};
	scanf("%d",&T);
	while(T--)
	{
		
		scanf("%d",&S);
		scanf("%s",arr);
		f=0;
		s=0;
		for(i=0;i<S+1;i++)
		{			
			arr[i]=arr[i]-48;
			if(s<i && arr[i]>0)
			{
				f=f+i-s;
				s=s+arr[i]+i-s;
			}
			else
			{
				s=s+arr[i];
			}
		}
		printf("Case #%d: %d\n",count++,f);
		
	}
	return 0;
}
