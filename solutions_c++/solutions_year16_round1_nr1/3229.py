#include<bits/stdc++.h>
using namespace std;

int main()
{
long long t,i,f,e,k;
string s,p;
cin>>t;
k=1;
while(t--)
{
	cin>>s;
	
	f=2002;
	e=f;
	p[f]=s[0];
	
	for(i=1;i<s.size();i++)
	{
		if(s[i]>=p[f])
		{
			p[--f]=s[i];
		}
		
		else
		{
			p[++e]=s[i];
		}
	}
	
	printf("Case #%lld: ",k++);
	for(i=f;i<=e;i++)
	cout<<p[i];
	
	cout<<endl;
}
}	
