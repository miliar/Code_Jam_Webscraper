#include <iostream>
#include <thread>
#include <Windows.h>
#include <algorithm>
#include <vector>

using namespace std;

void threadFun()
{
	cout << "hi from thread" << endl;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int r, c, w, index = 1;
	int T;
	cin >> T;
	while (T--)
	{
		cout << "Case #" << index++ << ": ";
		cin >> r >> c >> w;
		if (w == 1)cout << r*c << endl;
		else if (w == c)cout << (r - 1) + c << endl;
		else
		{
			if (2 * w - c > 0)cout << (r - 1) + w + 1 << endl;
			else if (2 * w - c == 0)cout << (r - 1) * 2 + w + 1 << endl;
			else
			{
				cout << (r - 1)*(c / w) + ((c%w == 0) ? ((c / w) + (w - 1)) : ((c / w) + w)) << endl;
			}
		}
	}
	return 0;
}