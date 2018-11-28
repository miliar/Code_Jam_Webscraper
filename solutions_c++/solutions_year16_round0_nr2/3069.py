#include<iostream>
#include<vector>
#include<string>

using namespace std;

int main()
{
	int T, t;
	cin >> T;
	t = 1;
	while (T >= t)
	{
		int res = 0;
		string S;

		cin >> S;

		char tmp = '+';
		for (int i = S.size() - 1; i >= 0; i--)
		{
			if (S[i] != tmp)
			{
				res++;
				if (tmp == '+')
					tmp = '-';
				else
					tmp = '+';

			}
		}

		cout << "Case #" << t << ": " << res << endl;
		t++;
	}
}