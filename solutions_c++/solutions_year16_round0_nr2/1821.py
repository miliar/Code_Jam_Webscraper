#include <iostream>
#include <string>

using namespace std;

int main()
{
	int T, test, i, sz, count;
	char ch;
	string S;

	cin>>T;
	for (test = 1; test <= T; test++)
	{
		cin>>S;
		sz = S.size();

		ch = S[0];
		count = 0;
		for (i = 1; i < sz; i++)
		{
			if (ch != S[i])
			{
				ch = S[i];
				count++;
			}
		}
		if (ch == '-')
		{
			count++;
		}

		cout<<"Case #"<<test<<": "<<count<<endl;
	}

	return 0;
}
