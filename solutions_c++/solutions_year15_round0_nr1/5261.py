#include <cstdio>
#include <algorithm>
using namespace std;

char buffer[2000];

int main()
{
	int t;
	scanf("%d",&t);

	for(int casenum=1; casenum<=t; casenum++)
	{
		int smax;
		scanf("%d",&smax);

		int total = 0;
		int ans = 0;
		scanf("%s",buffer);
		for(int i=0; i<=smax; i++)
		{
			ans = max(ans,i-total);
			total += buffer[i]-'0';
		}

		printf("Case #%d: %d\n",casenum,ans);
	}
}