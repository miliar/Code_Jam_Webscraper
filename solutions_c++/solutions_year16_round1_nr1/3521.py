#include<bits/stdc++.h>
using namespace std;
int main()
{
	FILE *fout = freopen("output6.txt", "w", stdout);
	long int t,l,b,e,i,j;
	char s[1001],p[2001];
	j=1;
	cin>>t;
	while(t--)
	{
		
		cin>>s;
		cout<<"Case #"<<j++<<": ";
		l=strlen(s);
		p[1000]=s[0];
		b=1000;e=1000;
		for(i=1;i<l;i++)
		{
			if(p[b]<=s[i])
			{
				b-=1;
				p[b]=s[i];
			}
			else
			{
				e+=1;
				p[e]=s[i];
			}
		}
		for(i=b;i<=e;i++)
		cout<<p[i];
		cout<<endl;
	}
	return 0;
}
