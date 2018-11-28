#include<cstring>
#include<cstdio>
#include<string>
#include<iostream>
using namespace std;
int main()
{
	int tc;
	string s;
	scanf("%d",&tc);
	int ans;
	for(int i=0;i<tc;i++)
	{
		ans=0;
		cin>>s;
		s+='+';
		int n=s.length();
		char last_char=s[0];
		for(int j=1;j<n;j++)
		{
			if(s[j]!=last_char)
			{
				ans++;
				last_char=s[j];
			}
		}
		printf("Case #%d: %d\n",i+1,ans);
	}
}