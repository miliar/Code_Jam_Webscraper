#include <iostream>
#include <string>
using namespace std;
int main()
{
	int t, i, j, r;
	string s;
	char c;
	cin>>t;
	for (j=1; j<=t; ++j)
	{
		cin>>s;
		s =s +'+';
		r=0;
		c=s[0];
		for(i=1; i<s.size(); ++i)
		{
			if (c!=s[i])
			{
				++r;
				c=s[i];
			}
		}
		cout<<"Case #"<<j<<": "<<r<<endl;
	}
	return 0;
}