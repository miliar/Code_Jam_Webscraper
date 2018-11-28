#include <iostream>
#include <vector>
#include <algorithm>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <math.h>
#include <string>
#include <cstdio>

using namespace std;

void solveCase(int t)
{
	int N, X;
	cin >> N >> X;
	list<int> sizes;

	for (int i = 0; i < N; ++i)
	{
		int Si;
		cin >> Si;
		sizes.push_back(Si);
	}

	sizes.sort(std::greater<int>());

	int CDs = 0;
	while (!sizes.empty())
	{
		CDs++;

		int x = X;
		bool firstFile = true;
		for (list<int>::iterator it = sizes.begin(); it != sizes.end(); ++it)
		{
			if (*it <= x)
			{
				x -= *it;
				it = sizes.erase(it);
				it--;

				if (!firstFile)
					break;
				firstFile = false;
			}
		}
	}

	cout << CDs;
}

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t)
	{	
		cout << "Case #" << t << ": ";
        solveCase(t);
        cout << endl;
	}
	
	return 0;
}