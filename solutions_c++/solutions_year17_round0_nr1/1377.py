/*
+--+-+---+ 2
*/
#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n;
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		cout<<"Case #"<<i<<": ";
		string s;int k;
		cin>>s>>k;
		bool b=1;
		int count1=0;
		for(int j=0;j<s.size();j++)
		{
			if(s[j]=='-')
			{
				count1++;
				if(j+k>s.size())
				{
					b=0;
					break;
				}
				else
				{
					for(int l=j;l<j+k;l++)
					{
						if(s[l]=='-')
							s[l]='+';
						else
							s[l]='-';
					}
				}
				//cout<<s<<"\n";
			}
		}
		if(b==1)
		{
			cout<<count1<<"\n";
		}
		else
		{
			cout<<"IMPOSSIBLE\n";
		}
	}
	return 0;
}