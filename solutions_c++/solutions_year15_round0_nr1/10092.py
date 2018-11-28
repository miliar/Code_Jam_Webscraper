#include <iostream>
using namespace std;

int main() {
	// your code goes here
	char s[7];
	int i,j,k,t,c=0,f=0;
	cin>>t;
	for(j=0;j<t;j++)
	{
			cin>>k;
			cin>>s;
		for(i=0;i<=k;i++)
		{	
			c+=s[i]-'0';
			if(c<(i+1))
			{
			f++;
			c++;
			}
		}
		cout<<"\n"<<"Case #"<<j+1<<": "<<f;
		f=0;
		c=0;
	}	
	return 0;
}