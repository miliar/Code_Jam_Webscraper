#include <stdio.h>
#include<algorithm>
using namespace std;
int palin(int a)
{
	int i,j,n[2][14]={0,};
	for(i=0;a>=1;i++)
	{
		n[1][i]=n[0][i]=a%10;
		a-=a%10;
		a/=10;
	}
	reverse(n[0],n[0]+i);
	a=i;
	for (j=0;j!=i;j++)
		if (n[0][j]==n[1][j])
			a-=1;
	if(a==0)
		return 1;
	else
		return 0;
}

int main()
{
	int cas,k=1;
	scanf("%d",&cas);
	while(cas--)
	{
		int i,j,l,cnt=0;
		scanf("%d %d",&i,&j);
		for(;i<=j;i++) 
		{
			for(l=1;l<=i;l++)
			{
				if(l*l==i)
					if(palin(l)&&palin(i)==1)
						cnt+=1;
			}
		}	
		printf("Case #%d: %d\n",k,cnt);
		k+=1;	
	}
}