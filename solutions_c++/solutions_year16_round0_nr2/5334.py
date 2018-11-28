#include <iostream>
#include <string>
#include <cstdlib>
using namespace std;
int main(void)
{
	int t, n;
	string s;
	getline(cin, s);

	t = atoi(s.c_str());

	for (int i = 1; i <= t; ++i)
	{
		s.clear();
		getline(cin, s);
		cout << "Case #" << i << ": ";

		int len = s.length();
		
		const char* pS = s.c_str();

		int res = 0;
		char pre = '0';
		for (int cur = 0; cur < len - 1; ++cur)
		{
			if (pS[cur] != pS[cur + 1])
			{
				res++; 
			}
		}

		if (pS[len - 1] == '-')
		{
			res++;
		}

		cout << res << endl;
	}

	return 0;
}
