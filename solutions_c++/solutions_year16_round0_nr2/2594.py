#include <iostream>
#include <cstdio>
#include <string>

using namespace std;

int main()
{
	int t; cin >> t;
	for(int i=1;i<=t;i++)
	{
		string s;
		cin >> s;

		cout << "Case #" << i << ": ";

		int n = s.length();
		int res = 0;
		string s1 = "";
		s1 += s[0];
		for(int i=1;i<n;i++)
			if(s1[s1.length()-1] != s[i])
				s1 += s[i];
		int m = s1.length();

		if(s1[0] == '+')
		{
			res = m/2; res <<= 1;
		}
		else
		{
			res = (m-1)/2; res <<= 1;
			res++;
		}
		cout << res << endl;
	}
	return 0;
}