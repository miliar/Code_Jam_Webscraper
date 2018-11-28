#include <bits/stdc++.h>

int main()
{
	int t=0,T;
	scanf("%d",&T);
	while(t++<T)
	{
		int n,i,x,cont=0,v[2550];
		scanf("%d",&n);
		memset(v,0,sizeof(v));
		int k=2*n*n-n;
		for(i=1;i<=k;i++) scanf("%d",&x), v[x]++;
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