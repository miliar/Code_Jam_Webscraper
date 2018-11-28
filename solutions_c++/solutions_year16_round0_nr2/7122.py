#include <iostream>
#include <string>

using namespace std;

int solve( string s) {
	
	char c = s[0], n;
	int ans = 0;
	for (int i = 1; i < s.size(); ++i)
	{
		n = s[i];
		if ( n == c)
			continue;
		else 
			ans += 1;
		c = n;
	}
	if( c == '-')
		ans+=1;

	return ans;
}

int main(int argc, char const *argv[])
{
	int t, ans ;
	string s;

	cin>>t;

	for (int i = 1; i < t+1; ++i)
	{
		cin>>s;
		cout << "Case #" << i << ": " << solve(s) << endl;
	}

	return 0;
}