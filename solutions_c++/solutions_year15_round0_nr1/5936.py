#include <iostream>
#include <string>
using namespace std;
int main()
{
	int T;
	int sMax;
	string str;
	cin >> T;
	for (int k = 0; k < T; ++k)
	{
		int extralCount = 0;
		int curCount = 0;
		cin >> sMax;
		cin >> str;
		for (int i = 0; i < sMax + 1; ++i)
		{
			if (curCount < i)
			{
				extralCount += (i - curCount);
				curCount = i;
			}
			curCount += int(str[i] - '0');
		}
		cout << "Case #" << (k + 1) << ": " << extralCount << endl;
	}
	return 0;
}