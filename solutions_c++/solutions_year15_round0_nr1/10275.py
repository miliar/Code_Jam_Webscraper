#include <bits/stdc++.h>
using namespace std;
#define ll long long int

int main() {
	int t,n,p,c,x;
	char s[10000];
	cin>>t;
	for(int j=1;j<=t;j++)
	{
		c=0;
		p=0;
		cin>>n;
		scanf("%s",s);
		p=(int)s[0] - '0';
		for(int i=1;i<=n;i++)
		{
			x=(int)s[i] - '0';
			if(p>=i)
			p=p+x;
			else if(x!=0)
			{
				c=c+i-p;
				p=p+x+c;
			}
			
		}
		cout<<"Case #"<<j<<": "<<c<<"\n";
		
	}
	return 0;
}