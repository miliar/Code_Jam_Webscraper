#include<cstdio>
int seen(int num[])
{
	int i;
	for(i=0;i<10;i++)
	{
		if(num[i]==0)
			return 0;
	}
	return 1;
}
int main()
{
	unsigned long long int t,n,i,j,prev,t1,t2,next;
	scanf("%llu",&t);
	int num[10];
	for(i=0;i<t;i++)
	{
		for(j=0;j<10;j++)
			num[j]=0;
		scanf("%llu",&n);
		if(n==0)
		{
			printf("Case #%llu:\tINSOMNIA\n",i+1);
		}
		else{
		next=n;
		while(!seen(num))
		{
			prev=next;
			t1=prev;
			while(t1)
			{
				t2=t1%10;
				num[t2]=1;
				t1=t1/10;
			}
			next=prev+n;	
		}
		printf("Case #%llu:\t%llu\n",i+1,prev);
		}
	}
	return 0;
}
