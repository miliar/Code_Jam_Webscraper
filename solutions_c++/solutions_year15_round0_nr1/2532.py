#include<iostream>
#include<vector>
#include<cstring>

using namespace std;

int main()
{
	int T;
	scanf("%d",&T);
	for(int ix = 0;ix < T;ix++)
	{
		int l;
		char s[2000];
		scanf("%d %s",&l,s);
		//printf("%s\n",s);
		int cum = 0,ans = 0;
		for(int i=0;i<=l;i++)
		{
			if(i > cum)
			{
				ans += i-cum;
				cum = i;
			}
			cum += s[i] - '0';
		}
		printf("Case #%d: %d\n",ix+1,ans);

	}
	return 0;
}