#include <bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	scanf("%d",&t);

	for(int q=1;q<=t;q++)
	{
		string s;
		cin>>s;
		int n=s.size();
		int cnt=0;
		for(int i=0;i+1<n;++i)
		{
			
			if(s[i]!=s[i+1])
				cnt++;
		}

		if(s[n-1]=='-') cnt++;

		printf("Case #%d: %d\n",q,cnt);
		


	}


}