#include<cstdio>
#include<algorithm>
#include<iostream>
using namespace std;
int main()
	{
	int t, i, j, n, sn, ln, sk, lk, s;
	scanf("%d", &t);
	for(i=1;i<=t;i++)
		{
		scanf("%d", &n);
		float a[n], b[n];
		for(j=0;j<n;j++)
			scanf("%f", a+j);
		for(j=0;j<n;j++)
			scanf("%f", b+j);
		printf("Case #%d: ", i);
		sort(a, a+n);
		sort(b, b+n);
		//deceitful war
		sn=sk=0;
		ln=lk=n-1;
		s=0;
		for(j=0;j<n;j++)
			{
			if(a[sn]<b[sk])
				{
				//printf("%f %f\n", a[sn], b[lk]);
				sn++;
				lk--;
				}
			else
				{
				//printf("%f %f inc\n", a[sn], b[sk]);
				s++;
				sn++;
				sk++;
				}
			}
		printf("%d ", s);
		
		//war
		sn=sk=0;
		ln=lk=n-1;
		s=0;
		for(j=0;j<n;j++)
			{
			if(a[sn]>b[sk])
				{
				s++;
				sk++;
				}
			else
				{
				sn++;
				sk++;
				}
			}
		printf("%d\n", s);
		}
	return 0;
	}