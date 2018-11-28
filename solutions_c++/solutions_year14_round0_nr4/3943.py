#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t,n,i,j,k,w=0,dw=0;
	scanf("%d", &t);
	for(int ii=1; ii<=t; ii++)
	{
		scanf("%d", &n);
		double nao[n], ken[n];
		for(i=0; i<n; i++)
			scanf("%lf", &nao[i]);
		for(i=0; i<n; i++)
			scanf("%lf", &ken[i]);

		sort(nao, nao+n);
		sort(ken, ken+n);
		w = 0;
		dw = 0;
		int s=0, e=n-1;i=0;
		j = n-1;
		e = n-1;
		while (e>=0)
		{
			while(nao[j] < ken[e] && e>=0)
			{
				e--;
			}
			if(e>=0)
				dw++;
			j--;e--;
		}
		//strategy for WAR
		bool *st = (bool *)calloc(n, sizeof(bool));
		while (s<n)
		{
			while(ken[s] < nao[i] && s<n)
			{
				s++;
			}
			while(st[s]==true && s<n)
				s++;

			if(s<n)
			{
				st[s] = true;
			}
			i++;s++;
		}
		for(i=0; i<n; i++)
			if(!st[i])
				w++;

		printf("Case #%d: %d %d\n",ii,dw, w);
		free(st);
	}
	return 0;
}