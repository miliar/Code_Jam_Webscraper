#include<bits/stdc++.h>
bool digit[12];
main()
{
	int T,t,count,N;
	long long i,n,tmp;
    scanf("%d",&T);
    //freopen("A.txt","w",stdout);
    for(t=1;t<=T;t++)
    {
    	scanf("%d",&N);
    	if(N==0)
    	{
    		printf("Case #%d: INSOMNIA\n",t);
    		continue;
		}
		for(i=0;i<10;i++)
    		digit[i]=0;
		count=0;
		for(i=1;count<10;i++)
		{
			n=N*i;
			tmp=n;
			while(tmp>0)
			{
				if(digit[tmp%10]==0)
				{
					digit[tmp%10]=1;
					count++;
				}
				tmp/=10;
			}
			//printf("%d ",N);
		}
		printf("Case #%d: %d\n",t,n);
	}
    scanf(" ");
}

