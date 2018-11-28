#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	for(int j=1;j<=t;j++)
	{
		int n,i;
		long long res=0,min;
		string s;
		scanf("%d",&n);
		cin>>s;
		min=s[0]-48;
		for(i=1;i<=n;i++)
		{
			if(s[i]=='0')
				continue;
			if(i>min)
			{
				res+=i-min;
				min+=s[i]-'0'+i-min;
			}
			else
				min+=s[i]-'0';
		}
		printf("Case #%d: %lld\n",j,res);
	}
	return 0;
}

