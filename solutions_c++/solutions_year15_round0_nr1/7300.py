#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.out","w",stdout);
	int t,smax,l,ans,curr; scanf("%d",&t);
	string s;
	for(int j = 1; j<=t; ++j)
	{
		scanf("%d",&smax);
		cin >> s;
		l = s.length(), ans = 0, curr = (int)(s[0] - '0');
		for (int i = 1; i < l; ++i)
			if(s[i] >= '1')
			{
				while(curr < i)
					++ans,++curr;
				curr += (int)(s[i] - '0');
			}
		printf("Case #%d: %d\n",j,ans);
	}
	return 0;
}