//#define LOCAL
#include <iostream>
using namespace std;

int main()
{
#ifdef LOCAL
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int t;
	cin >> t;
	for (int i = 0; i<t; i++)
	{
		int max;//max level of shyness
		cin >> max;
		int count=0;
		int need=0;
		for (int j = 0; j <= max; j++)
		{
			char shyness;
			cin >> shyness;
			if (j <= count)count += shyness-'0';
			else{
				need += j - count;
				count += j - count;
				count += shyness - '0';
			}
		}
		cout << "Case #" << i + 1 << ": " << need << endl;
	}
	return 0;
}