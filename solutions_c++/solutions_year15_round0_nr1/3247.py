#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,n;
	string s;
	scanf("%d",&T);
	for(int tt=1;tt<=T;++tt)
	{
		int cnt=0,tot=0;
		cin>>n>>s;
		for(int i=0;i<s.length();i++)
		{
			
			while(tot<i)
			{
				cnt++;
				tot++;
			}
			tot+=s[i]-'0';
		}
		printf("Case #%d: %d\n",tt,cnt);
	}
	return 0;
}
