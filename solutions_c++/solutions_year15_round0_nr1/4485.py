#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	for(int k=1;k<=t;k++)
	{
		int n,cur=0,answer=0;
		string s;
		cin>>n>>s;
		cur=s[0]-'0';
		for(int i=1;i<=n;i++)
		{
			if(s[i]>'0'&&cur<i)
			{
				answer+=(i-cur);
				cur=i+s[i]-'0';
			}
			else
				cur+=s[i]-'0';
			if(cur>=n)break;
		}
		cout<<"Case #"<<k<<": "<<answer<<endl;
	}
	return 0;
}
