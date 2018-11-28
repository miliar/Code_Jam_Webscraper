#include <iostream>

using namespace std;

int main()
{
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int h = 1; h <= t; h++)
	{
		double c, f, x;
		cin >> c >> f >> x;
		double num = 2;
		double ans = 0;
		while (true)
		{
			if (c / num + x / (num + f) < x / num)
			{
				ans += c / num;
				num += f;
			}
			else
			{
				ans += x / num;
				break;
			}
		}
		cout.precision(9);
		cout << "Case #" << h << ": " << fixed << ans << endl;
	}
	return 0;
}