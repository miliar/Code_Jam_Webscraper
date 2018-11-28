#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;

int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int TC, T, j, flag, i, a , b , k, m, n;
	scanf("%d", &TC);
	for(T=0;T<TC;T++)
	{
		flag = 0;
		scanf("%d",&a);
		scanf("%d",&b);
		scanf("%d",&k);
		for(m=0;m<a;m++)
			for(n=0;n<b;n++)
			{
				if((m&n) < k)
				{
					flag++;
					//printf ("%d,%d,%d\t",m,n,m&n);
				}
			}
		printf("Case #%d: %d\n",T+1,flag);
	}
	return 0;
}
