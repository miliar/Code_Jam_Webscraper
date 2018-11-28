#include <iostream>
#include <string>

using namespace std;

int main()
{
	int tl,l = 0;
	cin>>tl;
	while(tl--)
	{
		l++;
		string s;
		int a,b,c = 0;
		char t;
		cin>>s;
		t = s[0];
		a = 1;
		while(a < s.length())
		{
			if(t==s[a])
			{
				a++;
				continue;
			}
			t = s[a];
			c++;
			a++;
		}
		if(s[s.length()-1] == '-')
			c++;
		cout<<"Case #"<<l<<": "<<c<<endl;
	}
}