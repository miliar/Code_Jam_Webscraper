#include <bits/stdc++.h>

int v[2551];

int main()
{
	int t=0,T;
	scanf("%d",&T);
	while(t++<T)
	{
		int n,i,x,cont=0;
		memset(v,0,sizeof(v));
		scanf("%d",&n);
		int a=2*n*n-n;
		for(i=1;i<=a;i++)
		{
			scanf("%d",&x);
			v[x]++;
		}
		printf("Case #%d: ",t);
		for(i=1;;i++)
		{
			if(v[i]%2) printf("%d ",i), cont++;
			if(cont==n) {break;}
		}
		printf("\n");
	}
	return 0;
}