#include <iostream>
#include <string>
#include <cstdlib>
#include <deque>
using namespace std;
int main(void)
{
	char max[2000];
	deque<char> deq;
	char res[2000];
	int t, n;
	string s;
	getline(cin, s);

	t = atoi(s.c_str());

	for (int i = 1; i <= t; ++i)
	{
		deq.clear();
		s.clear();
		getline(cin, s);
		cout << "Case #" << i << ": ";

		int len = s.length();

		const char* pS = s.c_str();

		max[0] = pS[0];
		deq.push_front(pS[0]);

		for (int k = 1; k < len; ++k)
		{
			if (pS[k] >= max[k - 1])
			{
				max[k] = pS[k];
				deq.push_front(pS[k]);
			}
			else
			{
				max[k] = max[k - 1];
				deq.push_back(pS[k]);
			}
		}

		deque<char>::iterator it = deq.begin();
		
		int kLen = 0;
		for (; it != deq.end(); ++it, ++kLen)
		{
			res[kLen] = *it;
		}

		res[kLen] = 0;

		cout << res << endl;;
	}

	return 0;
}
