#include <iostream>
using namespace std;

int t, s, i, j;
char ch[1001];

int main() 
{
	cin>>t;
	for (i=1;i<=t;i++)
	{
		cin>>s;
		cin>>ch;
		int ans=0;
		for (j=0;j<s;j++)
		{
			if (ch[j]=='0')
				ans++;
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}