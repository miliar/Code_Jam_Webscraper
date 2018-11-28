#include <iostream>
using namespace std;

int main(void)
{
	int cases;
	cin >> cases;
	for (int t = 0; t < cases; ++t)
	{
		int a,b,k;
		cin >> a >> b >> k;

		int ret = 0;
		for (int i = 0; i < a; ++i)
		{
			for (int j = 0; j < b; ++j)
			{
				int c = i & j;
				if (c < k)
					++ret;
			}
		}
		cout << "Case #" << (t + 1) << ": " << ret << endl;
	}
	return 0;
}
