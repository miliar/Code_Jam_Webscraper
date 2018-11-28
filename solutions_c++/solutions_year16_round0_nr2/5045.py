#include <bits/stdc++.h>
#define ll long long
using namespace std;
string s;
int l;
bool ok()
{
	int i;
	bool flag=1;
	for(i=0;i<l;i++)
	{
		if(s.at(i)=='-')
		{
			flag=0;
			break;
		}
	}
	return flag;
}
void myperform()
{
	int i;
	for(i=(l-1);i>=0;i--)
	{
		if(s.at(i)=='-')
		{
			break;
		}
	}
	while(i>=0)
	{
		if(s.at(i)=='+')
		s.at(i)='-';
		else
		s.at(i)='+';
		i--;
	}
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int test,t;
	cin>>test;
	for(t=1;t<=test;t++)
	{

		cin>>s;
		int ans;
		l=s.length();ans=0;
		while(1)
		{
			if(ok())
			break;
			else
			{
				ans++;
				myperform();
			}
		}
		printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}
