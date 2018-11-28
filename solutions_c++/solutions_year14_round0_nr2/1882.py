#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	int t;
	double c, f, x;
	double ans, now;
	cin >> t;
	for (int i=1;i<=t;i++)
	{
		ans = 0;
		now = 2;
		cin >> c >> f >> x;
		while (c*(now+f)<x*f)
		{
			ans += c/now;
			now += f;
		}
		ans += x/now;
		cout << "Case #" << i << ": " << fixed << setprecision(7) << ans << endl;
	}
	return 0;
}
