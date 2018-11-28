// Takemoto.cpp : 定义控制台应用程序的入口点。
//

#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

int main()
{
	//freopen("..\\B-small.in","r",stdin);
	//freopen("..\\B-small.out","w",stdout);
	freopen("..\\B-large.in","r",stdin);
	freopen("..\\B-large.out","w",stdout);

	int t = 0;
	scanf("%d", &t);

	vector<string> strOutput;

	for (int a = 0; a < t; ++a)
	{
		int n = 0, m = 0;
		scanf("%d", &n);
		scanf("%d", &m);
		vector<int> lawnList;
		vector<bool> lawnmowerList;
		for (int b = 0; b < n; ++b)
		{
			for (int c = 0; c < m; ++c)
			{
				int h = 0;
				scanf("%d", &h);
				lawnList.push_back(h);
				lawnmowerList.push_back(false);
			}
		}

		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < m; ++j)
			{
				int h = lawnList[i * m + j];
				bool bEnable1 = true;
				bool bEnable2 = true;
				for (int k = j; k >= 0; --k)
				{
					if (lawnList[i * m + k] > h)
					{
						bEnable1 = false;
						break;
					}
				}
				for (int k = j; k < m; ++k)
				{
					if (lawnList[i * m + k] > h)
					{
						bEnable2 = false;
						break;
					}
				}
				if (bEnable1 && bEnable2)
				{
					lawnmowerList[i * m + j] = true;
					continue;
				}

				bEnable1 = true;
				bEnable2 = true;
				for (int k = i; k >= 0; --k)
				{
					if (lawnList[k * m + j] > h)
					{
						bEnable1 = false;
						break;
					}
				}
				for (int k = i; k < n; ++k)
				{
					if (lawnList[k * m + j] > h)
					{
						bEnable2 = false;
						break;
					}
				}
				if (bEnable1 && bEnable2)
				{
					lawnmowerList[i * m + j] = true;
					continue;
				}
			}
		}

		bool bPossible = true;
		for (vector<bool>::iterator it = lawnmowerList.begin(); it != lawnmowerList.end(); ++it)
		{
			if (!(*it))
			{
				bPossible = false;
				break;
			}
		}
		stringstream ss;
		ss << "Case #" << a + 1 << ": " << (bPossible ? "YES" : "NO");
		strOutput.push_back(ss.str());
	}

	for (vector<string>::iterator it = strOutput.begin(); it != strOutput.end(); ++it)
	{
		cout << *it << endl;
	}
	
	return 0;
}

