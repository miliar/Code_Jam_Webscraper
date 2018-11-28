#include<iostream>
#include<cstring>
#include<deque>
#include<cstdio>
using namespace std;
int main()
{	freopen("A-large(1).in","r",stdin);
	freopen("largea.txt","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		string s,a="";
		deque<char> ans;
		cin>>s;
		a+=s[0];
		ans.push_back(s[0]);
		char ch=s[0];
		for(int j=1;j<s.size();j++)
		{
			if(s[j]>=ch)
			{
				ans.push_front(s[j]);
				ch=s[j];
			}
			else ans.push_back(s[j]);
		}
		printf("Case #%d: ",i);
		for(int k=0;k<ans.size();k++)
		cout<<ans[k];
		cout<<"\n";
	}
}