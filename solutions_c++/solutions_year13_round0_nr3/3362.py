// Takemoto.cpp : 定义控制台应用程序的入口点。
//

#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

int main()
{
	freopen("..\\C-small.in","r",stdin);
	freopen("..\\C-small.out","w",stdout);
	//freopen("..\\C-large.in","r",stdin);
	//freopen("..\\C-large.out","w",stdout);

	int t = 0;
	cin >> t;

	vector<string> strOutput;

	for (int n = 0; n < t; ++n)
	{
		__int64 a = 0, b = 0;
		cin >> a;
		cin >> b;

		__int64 p = ceil(sqrt((double)a));
		__int64 q = floor(sqrt((double)b));

		int count = 0;
		for (__int64 i = p; i <= q; ++i)
		{
			__int64 r = i;
			vector<int> numList;
			while (r > 0)
			{
				numList.push_back(r % 10);
				r /= 10;
			}

			int x = 0, y = numList.size() - 1;
			while (x < y)
			{
				if (numList[x] != numList[y])
				{
					break;
				}

				++x;
				--y;
			}

			if (x < y)
			{
				continue;
			}

			r = i * i;
			numList.clear();
			while (r > 0)
			{
				numList.push_back(r % 10);
				r /= 10;
			}

			x = 0;
			y = numList.size() - 1;
			while (x < y)
			{
				if (numList[x] != numList[y])
				{
					break;
				}

				++x;
				--y;
			}

			if (x >= y)
			{
				++count;
			}
		}

		stringstream ss;
		ss << "Case #" << n + 1 << ": " << count;
		strOutput.push_back(ss.str());
	}

	for (vector<string>::iterator it = strOutput.begin(); it != strOutput.end(); ++it)
	{
		cout << *it << endl;
	}
	
	return 0;
}

