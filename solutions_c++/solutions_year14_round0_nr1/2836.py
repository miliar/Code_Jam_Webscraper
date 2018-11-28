#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
int main()
	{
	int t, i, j, x1, x2, x3, x4, n, c, m;
	bool num[17];
	scanf("%d", &t);
	for(i=1;i<=t;i++)
		{
		scanf("%d", &n);
		j=1;
		memset(num, false, sizeof(bool)*17);
		while(j<n)
			{
			scanf("%d%d%d%d", &x1, &x2, &x3, &x4);
			j++;
			}
		scanf("%d%d%d%d", &x1, &x2, &x3, &x4);
		j++;
		num[x1]=num[x2]=num[x3]=num[x4]=true;
		while(j<=4)
			{
			scanf("%d%d%d%d", &x1, &x2, &x3, &x4);
			j++;
			}
		
		scanf("%d", &n);
		j=1;
		while(j<n)
			{
			scanf("%d%d%d%d", &x1, &x2, &x3, &x4);
			j++;
			}
		scanf("%d%d%d%d", &x1, &x2, &x3, &x4);
		j++;
		c=0;
		if(num[x1]) {m=x1;c++;}
		if(num[x2]) {m=x2;c++;}
		if(num[x3]) {m=x3;c++;}
		if(num[x4]) {m=x4;c++;}
		printf("Case #%d: ", i);
		if(c==1)
			printf("%d\n", m);
		else if(c==0)
			printf("Volunteer cheated!\n");
		else
			printf("Bad magician!\n");
		while(j<=4)
			{
			scanf("%d%d%d%d", &x1, &x2, &x3, &x4);
			j++;
			}
		}
	return 0;
	}