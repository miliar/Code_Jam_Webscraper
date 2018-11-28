#include <iostream>
#include <string>

using namespace std;

int main()
{
	int T, test, K, i, j, sz, count;
	bool is;
	string S;

	cin>>T;

	for (test = 1; test <= T; test++)
	{
		cin>>S>>K;

		count = 0;
		sz = S.size();

		for (i = 0; i + K - 1 < sz; i++)
		{
			if (S[i] == '-')
			{
				count++;

				for (j = i; j < i + K; j++)
				{
					S[j] = (S[j] == '+') ? '-' : '+';
				}
			}
		}

		is = false;
		for (i = 0; i < sz; i++)
		{
			if (S[i] == '-')
			{
				is = true;
				break;
			}
		}

		if (is)
		{
			cout<<"Case #"<<test<<": IMPOSSIBLE"<<endl;
		}
		else
		{
			cout<<"Case #"<<test<<": "<<count<<endl;
		}
	}

	return 0;
}

