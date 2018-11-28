# include <bits/stdc++.h>
using namespace std;
int main()
{
freopen("input.txt","r", stdin);
freopen("out.txt", "w", stdout);
int t,i,j,n,c;
cin>>t;string s;
for(j=1;j<=t;j++)
{
	cin>>s;c=0;
	for(i=1;i<s.length();i++)
	{
		if(s[i]!=s[i-1])
			c++;
	}
if(s[s.length()-1]=='-')
	c++;
printf("Case #%d: %d\n",j,c);
	}
return 0;
}