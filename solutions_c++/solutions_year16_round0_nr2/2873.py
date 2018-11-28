#include<bits/stdc++.h>
using namespace std;

int n,i,j,k,l,p;
string s;
int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	
	scanf("%d",&n);
	for(;n;n--)
	{
		
		cin>>s;
		char c='+';
		int ans=0;
		for(int i=s.length()-1;i>=0;i--)
		if(s[i]!=c)
		{
			++ans;
			if(c=='-')c='+';else c='-';
		}
		printf("Case #%d: %d\n",++p,ans);
	}
	return 0;
}
