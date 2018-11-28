#include <stdio.h>
int main()
{
	int table[1000][1000];
	for(int a=0;a<1000;a++)
		for(int b=0;b<1000;b++)
			table[a][b]=a&b;

	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int A,B,K,ans=0;
		scanf("%d %d %d",&A,&B,&K);
		for(int a=0;a<A;a++)
			for(int b=0;b<B;b++)
				if(table[a][b]<K)
					ans++;
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
