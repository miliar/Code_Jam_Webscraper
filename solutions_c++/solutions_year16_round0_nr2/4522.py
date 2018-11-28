#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for (int k = 1; k <= t; ++k)
	{
		printf("Case #%d: ",k);
		string s;
		cin>>s;
		int n=s.size();
		int count=0;
		for (int i = 0; i < n-1; ++i)
		{
			if(s[i]!=s[i+1])
				count++;
		}
		if(s[n-1]=='-')
			count++;
		printf("%d\n",count);
	}
}