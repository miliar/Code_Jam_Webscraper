#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.txt","w",stdout);
	int a,b,c,d;
	char s[120];
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cin>>a;
	for(b=0;b<a;b++)
	{
		cin>>s;
		for(c=strlen(s)-1,d=0;c>=0;c--)
		{
			if((s[c]=='-'&&d%2==0)||(s[c]=='+'&&d%2==1))d++;
		}
		cout<<"Case #"<<b+1<<": "<<d<<"\n"; 
	}
}
