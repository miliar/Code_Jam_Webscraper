#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;
int main()
{
	int caseTest;
	scanf("%d",&caseTest);
	for (int _ = 1 ; _ <= caseTest ; _ ++)
	{
		int ans = 0;
		int Smax;
		scanf("%d",&Smax);
		getchar();
		int now = 0;
		for (int i = 0 ; i <= Smax ; i ++)
		{
			int a = getchar() - '0';
			if ( now < i ) 
			{
				ans += ( i - now );
				now = i;
			}
			now += a;
		}
		printf("Case #%d: %d\n",_,ans);
	}
}
