#include<iostream>
#include<string>
using namespace std;

#pragma warning (disable : 4996)

int main()
{
	freopen("A-large.in", "rt", stdin);
	freopen("al.out", "wt", stdout);
	int t;
	cin >> t;
	for (int i = 1; i <= t; ++i)
	{
		int k;
		string audience;
		cin >> k >> audience;

		auto soFar = 0, answer = 0;
		for (int j = 0; j < audience.size(); ++j)
		{
			if (soFar < j)
			{
				answer += j - soFar;
				soFar = j;
			}

			soFar += audience[j] - '0';
		}

		cout << "Case #" << i << ": " << answer << endl;
	}

	return 0;
}