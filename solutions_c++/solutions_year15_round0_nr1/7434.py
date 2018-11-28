#include<stdio.h>

int main()
{
	int T, Smax;
	char S[10001];
	int temp,inv;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		scanf("%d %s",&Smax,S);
		temp=0;
		inv=0;
		for(int j=0;j<Smax+1;j++)
		{
			if(temp<=0)
			{
				if(S[j]-48>0)
					temp=S[j]-48;
				else
					inv++;
			}
			else
				temp+=S[j]-48;
			temp--;	
		}
		printf("Case #%d: %d\n",i+1,inv);
	}
}