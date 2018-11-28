#include<iostream>
#include<cstdio>
#include<string>
using namespace std;
int ans,n;
string s;
int Doit()
{
	ans=0;
	char lt=s[0];
	for(int i=1;i<s.length();i++)
	{
		if(s[i]!=lt)
		{
			ans++;
			lt=s[i];
		}
	}
	if(lt=='-')
		ans++;
	return ans;
}
int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		cin>>s;
		printf("Case #%d: %d\n",i,Doit());
	}
	return 0;
}
