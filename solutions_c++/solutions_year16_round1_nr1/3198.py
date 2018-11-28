#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		string S;
		cin >> S;

		string cur = "";
		for (auto c : S)
		{
			string str1 = cur + c;
			string str2 = c + cur;
			cur = max(str1, str2);
		}

		cout << "Case #" << t << ": " << cur << endl;
	}

	return 0;
}