#include<cstdio>

void test(int);

int main()
{
	int t,i=1;
	scanf("%d",&t);
	while(t--)
	{
		test(i);
		i++;
	}
	return 0;
}

void test(int c)
{
	int a,b,k,i,j,temp,ctr=0;
	scanf("%d%d%d",&a,&b,&k);
	for(i=0 ; i<a ; i++)
	{
		for(j=0 ; j<b ; j++)
		{
			temp=(i & j);
			//printf("%d\n",temp);
			if(temp < k)
				ctr++;
		}
	}
	printf("Case #%d: %d\n",c,ctr);
}
