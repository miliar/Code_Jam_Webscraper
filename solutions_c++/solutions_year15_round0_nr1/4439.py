#include <bits/stdc++.h>
using namespace std;
int main()
{
	string s;
	int t,len;
	long long cnt, pre;
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++)
	{
		scanf("%d",&len);
		cin >> s;
		pre=cnt=0;
		pre+=s[0]-'0';
		for(int i=1;i<=len;i++)
		{	
			if(pre<i && (s[i]-'0')>0)
			{
				cnt+=(i-pre);
				pre=i;
			}
			pre+=s[i]-'0';
		}
		printf("Case #%d: %lld\n",tt,cnt);
	}
	return 0;
}
