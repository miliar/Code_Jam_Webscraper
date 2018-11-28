#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <string>
#include <math.h>
using namespace std;

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	cin>>t;
	for (int l = 0; l < t; ++l)
	{
		string s;
		cin>>s;
		bool t = false;
		int res = 0;
		for (int i = 0; i < s.length(); ++i)
		{
			if (s[i] == '+')
				t = true;
			if (i < s.length() - 1 && s[i] == s[i + 1])
			{
				continue;
			}
			if (s[i] == '-')
			{
				if (t)
					res += 2;
				else res += 1;
			}
		}
			cout<<"Case #"<<l + 1<<": "<<res<<endl;
	}
	return 0;
}