#include <cstdio>
#include <string>
#include <iostream>
using namespace std;
int tests, n;
string s;

int main()
{
	freopen("ovation.in", "r", stdin);
	freopen("ovation.out", "w", stdout);
	
	cin >> tests;
	for (int test_no = 1; test_no <= tests; test_no++)
	{
		cout << "Case #" << test_no << ": ";
		cin >> n >> s;
		
		int res = 0, curr = 0;
		for (int i = 0; i <= n; i++)
			if (s[i] - '0' > 0)
			{
				if (curr < i)
				{
					res += i - curr;
					curr = i;
				}
				curr += s[i] - '0';
			}
		cout << res << "\n";
	}
	return 0;
}

