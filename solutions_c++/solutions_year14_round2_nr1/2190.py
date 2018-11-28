#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <stdlib.h>
using namespace std;

int main()
{
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A-small-attempt2.out","w",stdout);
	int t;
	cin>>t;
	for (int tt=1;tt<=t;tt++)
	{
		int n;
		cin>>n;
		std::vector<string> s(n);
		bool win = true;
		char a[n][101];
		int b[n][101];
		int c[n];
		int ans = 0;
		memset(a,0,sizeof(a));
		for (int i=0;i<n;i++)
		{
			cin>>s[i];
			a[i][0] = s[i][0];
			b[i][0] = 1;
			c[i] = 1;
			for (int j=1;j<s[i].length();j++)
			{
				if (s[i][j]!=s[i][j-1])
				{
					
					a[i][c[i]] = s[i][j];
					b[i][c[i]] = 1;
					c[i]++;
				}
				else
				{
					b[i][c[i]-1] ++;
				}
			}
		}
		/*
		for (int i=0;i<n;i++)
		{
			for (int j=0;j<c[i];j++)
				cout<<a[i][j]<<b[i][j]<<" ";
			cout<<"\n";
		}
		*/
		for (int i=1;i<n;i++)
		{
			if (c[i]!=c[0]) 
			{
				win = false;
				break;
			}
			for (int j=0;j<c[0];j++)
			{
				if (a[i][j]!=a[0][j])
				{
					win = false;
					break;
				}
				
			}
		}
		if (win)
		{
			for (int i=0;i<c[0];i++)
			{
				int sum = 0;
				for (int j=0;j<n;j++)
					sum +=b[j][i];
				int avg = sum/n;
				for (int j=0;j<n;j++)
					ans += abs(b[j][i]-avg);
			}
				

		}
		/*
		for (int i=0;i<26;i++)
		{
			if (a[i][1]!=0 && a[i][0]!=0)
				ans+=abs(a[i][1]-a[i][0]);
			else
			{
				if (a[i][1]!=0 || a[i][0]!=0)
				{
					win = false;
					break;
				}
			}
		}
		*/
		/*
		for (int i=0;i<26;i++)
		{
			bool flag = true;
			int sum = 0;
			for (int j=0;j<n;j++)
			{
				if (a[i][j]==0) flag = false;
				sum +=a[i][j];
			}
			if (sum!=0)
				if (!flag) 
				{
					win = false;
					break;
				}
				else
				{
					if (sum!=0)
					{
						int avg = sum/n;
						int tmp = 0;
						for (int j=0;j<n;j++)
							tmp +=abs(a[i][j]-avg);
						avg --;
						int tmp1 = 0;
						for (int j=0;j<n;j++)
							tmp1 +=abs(a[i][j]-avg);
						if (tmp1<tmp) tmp = tmp1;
						avg+=2;
						tmp1 = 0;
						for (int j=0;j<n;j++)
							tmp1 +=abs(a[i][j]-avg);
						if (tmp1<tmp) tmp = tmp1;
						ans +=tmp;
					}
				}
		}
		*/
		cout<<"Case #"<<tt<<": ";
		if (win)
			cout<<ans<<"\n";
		else
			cout<<"Fegla Won\n";
	}
	return 0;
}