#include <stdio.h>
int T,t,S;
char temp[1100];

int solve(int x)
{
	int i,j,k;
	int d;
	int first[10];
	int res = 0;
	for(i=0;i<10;i++) first[i]=0;
	d=10;
	for(i=0;i<1000;i++)
	{
		k=i*x;
		while(k)
		{
			j = k%10;
			k = k / 10;
			if(first[j]==0) 
			{
				first[j] = i;
				d--;
			}
		}
		if(d <= 0)
			break;
	}
	
	return i;
}


int main()
{
	int i,j,k;
	int x;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		scanf("%d",&x);
		k = solve(x);
		if(k>=1000)
			printf("Case #%d: INSOMNIA\n",t);
		else
			printf("Case #%d: %d\n",t,k*x);
		//printf("%d %s\n",S,temp);
		//printf("Case #%d: %d\n",i,solve());

	}

	//gets(temp);
	return 0;
}
