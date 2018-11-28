#include<bits/stdc++.h>

using namespace std;

int main()
{
	freopen("output.txt", "w", stdout);
	ifstream fin;
	fin.open ("input.txt");
	char str[1005];
	int k;
	int t;
	fin>>t;
	int l=1;
	while(l<=t)
	{
		fin>>str>>k;
		int len = strlen(str);
		int ans = 0;
		
		for(int i=0;i<=len-k;i++)
		{
			if(str[i]=='-')
			{
				for(int j = i; j < i+k; j++)
				{
					if(str[j]=='-')
						str[j] = '+';
					else str[j] = '-';
				}
				ans++;
			}
		}
		
		for(int i=len-k;i<len;i++)
		{
			if(str[i]=='-')
			{
				ans = -1;
				break;
			}
		}
		
		cout<<"Case #"<<l<<": ";
		if(ans == -1)
			cout<<"IMPOSSIBLE";
		else cout<<ans;
		cout<<endl;
		l++;
	}
}
