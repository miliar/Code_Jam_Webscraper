#include <bits/stdc++.h>
using namespace std;

int arr[1005];

int main()
{
	int t;
	cin >> t;

	for(int cn=1; cn<=t; cn++)
	{
		string str;
		int k;
		cin >> str >> k;

		int n = str.size();
		for(int i=0; i<n; i++)
			arr[i] = str[i]=='+'?1:0;

		int ans = 0;

		for(int i=0; i<=n-k; i++)
			if(arr[i]==0)
			{
				ans++;
				for(int j=0; j<k; j++)
					arr[i+j] ^= 1;
			}
		for(int i=n-k+1; i<n; i++)
			if(arr[i]==0)
			{
				ans = -1;
				break;
			}

		printf("Case #%d: ",cn);
		if(ans==-1)
			puts("IMPOSSIBLE");
		else
			printf("%d\n",ans);
	}

	return 0;
}