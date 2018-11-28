#include <bits/stdc++.h>
using namespace std;

int main()
{
	int n,K,cnt=1;
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	scanf("%d%d%d",&n,&n,&K); // 11 .. 11 .. 11 .. 11 .. 11

	printf("Case #1: \n");
	for (int i=0;i<=n-10;i++)
		for (int j=0;j<=n-10-i;j++)
			for (int k=0;k<=n-10-i-j;k++)
				{
					int l=n-10-i-j-k;
					printf("11");
					for (int x=0;x<i;x++) printf("0");
					printf("11");
					for (int x=0;x<j;x++) printf("0");
					printf("11");
					for (int x=0;x<k;x++) printf("0");
					printf("11");
					for (int x=0;x<l;x++) printf("0");
					printf("11 ");
					for (int x=2;x<=10;x++)	printf("%d ",x+1);
					printf("\n");
					cnt++;
					if (cnt > K) return 0;
				}
	return 0;
}
/*
a+b+c = 6
0 0 6
0 1 5
0 2 4
0 3 3



*/