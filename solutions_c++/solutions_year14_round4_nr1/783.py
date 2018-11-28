#include <stdio.h>
#include <string.h>

const int PROB_NUM=2;

int num[701];

void pre_process()
{

}

void process()
{
	memset(num,0,sizeof(num));
	int s=0,a,n,x,i,j;
	scanf("%d%d",&n,&x);
	for(i=0;i<n;i++)
	{
		scanf("%d",&a);
		num[a]++;
	}
	for(i=1;i<=700;i++)
	{
		while(num[i])
		{
			s++;
			num[i]--;
			for(j=x-i;j>=i;j--)
			{
				if(num[j])
				{
					num[j]--;
					break;
				}
			}
		}
	}
	printf("%d\n",s);
}

int main()
{
	char in[10]="0.in";
	char out[10]="0.out";
	in[0]=PROB_NUM+'0';
	out[0]=PROB_NUM+'0';
	freopen(in,"r",stdin);
	freopen(out,"w",stdout);
	pre_process();
	int t,i;	
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		process();
	}
	return 0;
}