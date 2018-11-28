#include <iostream>
using namespace std;

int main() {
	int t;
	string s;
	cin>>t;
	for(int i = 1; i <= t; i++)
	{
		cin>>s;
		string ans = "";
		ans += s[0];
		for(int j = 1; j < s.length(); j++)
		{
			if(s[j] >= ans[0])
				ans = s[j] + ans;
			else
				ans += s[j];
		}
		cout<<"Case #"<<i<<": "<<ans<<endl; 
	} 
	return 0;
}