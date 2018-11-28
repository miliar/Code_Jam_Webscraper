#include<cstdio>
#include<iostream>
#include<cstring>
using namespace std;

string s;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T;
	cin>>T;
	for(int i=1;i<=T;++i)
	{
		cin>>s;
		int ans=1;
		int l=s.size();
		for(int j=1;j<l;j++)
		{
			if(s[j]!=s[j-1]) ans++;		
		}
		if(s[l-1]=='+') ans--;
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
