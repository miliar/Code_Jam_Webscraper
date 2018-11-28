#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() 
{	
	int t, ans, c = 1;
	string s;
	cin>>t;
	while(t--)
	{
		ans = 0;
		cin>>s;
		if(s[0] == '-')
			ans++;
		for (int i = 1; i < s.size(); i++)
				if (s[i] == '-' && s[i-1] == '+')
					ans += 2;
		cout<<"Case #"<<c<<": "<<ans<<endl;	
		c++;
	}
	return 0;
}