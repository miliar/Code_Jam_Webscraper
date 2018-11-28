#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(int argc, char* argv[])
{
	int T;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	cin >> T;
	vector<string> S;
	for (int i = 0; i < T; i++)
	{
		string tmp;
		cin >> tmp;
		S.push_back(tmp);
	}

	for (int i = 0; i < T; i++)
	{
		int count = 0;
		char cur = '-';
		for (int j = S[i].size() - 1; j >= 0; j--)
		{
			if (S[i][j] == cur)
			{
				count++;
				if (cur == '-')
					cur = '+';
				else
					cur = '-';
			}
		}
		cout << "Case #" << i + 1 << ": " << count << endl;
	}

	return 0;
}