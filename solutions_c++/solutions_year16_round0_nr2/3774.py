#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
int t;
cin>>t;
int c=1;
while(c<=t)
{
	string s;
	cin>>s;
	int ans=0;
	int l=s.length();
	int i=0;
	while(i<l)	
	{	int flag=0;
		while(s[i]=='-' && i<l)
		{	
			i++;
			flag=1;
		}
		if(i==l) { ans+=1;	break; }
		if(flag) { ans+=1; flag=0;}
		while(s[i]=='+' && i<l)
		{
			i++;
			flag=1;
		}
		if(i==l) break;
		if(flag) { ans+=1; flag=0;}
}
cout<<"Case #"<<c<<": "<<ans<<endl;
c++;
}
		
	return 0;
}