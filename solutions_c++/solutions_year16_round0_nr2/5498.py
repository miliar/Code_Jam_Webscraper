#include <iostream>
#include <string>
#include <stack>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	int t;
	string s;
	stack<char> sk;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{	
		int ans = 0;
		while(!sk.empty())
			sk.pop();

	 	cin >> s;
	 	sk.push(s[0]);
	 	if (s.length() == 1)
	 		ans = s[0] == '+' ? 0 : 1;
		else
		{
			int j = 0;
			bool isAdd = true;
			while (s[j] == '-' && j < s.length())
			{
				sk.push(s[j]);
				ans = 1;
				j++;
			}
		 	for (; j < s.length(); j++)
		 	{
		 		char c = sk.top();
	
		 		if (c != s[j])
	 			{
	 				if (s[j] == '+')
	 					isAdd = true;
					else if (isAdd)
						ans += 2, isAdd = false;
			 	}
			 	sk.push(s[j]);
		 	}
		}
		cout << "Case #" << i << ": "<< ans << endl;
	}
	return 0;
}