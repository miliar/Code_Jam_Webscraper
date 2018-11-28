#include <bits/stdc++.h>

using namespace std;
int main()
{
	int t,x;
	cin>>t;
	for(int x=1;x<=t;x++)
	{
		string a;
		cin>>a;
		int count=0;
		int flag=0;
		while(flag!=a.length())
		{
			flag=0;
			for(int i=1;i<a.length();i++)
			{
				if(a[i]!=a[i-1])
				{
					string b;
					for(int j=i-1;j>=0;j--)
					{
						if(a[j]=='+')
						b.push_back('-');
						else
							b.push_back('+');
					}
					for(int j=i;j<a.length();j++)
						b.push_back(a[j]);
					a=b;
					count++;
					break;
				}
			}

			for(int i=0;i<a.length();i++)
			{
				if(a[i]=='+')
					flag++;
			}
			if(flag==0)
			{
				flag=a.length();
				count++;
			}
		}
		cout<<"Case #"<<x<<": "<<count<<endl;
	}

		

	
	return 0;
}