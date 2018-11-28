#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>

using namespace std;

int main ()
{
	ios_base::sync_with_stdio(false);
	ifstream cin ( "B-small-attempt0.in" );
	ofstream cout ( "output.txt" );
	int t;
	cin >> t;
	int k = 1;
	while (t--)
	{
		long double c, f, x;
		cin >> c >> f >> x;
		long double cur_speed = 0;
		long double ans = 1000000000;
		for (int i = 0; i < 50000; ++i)
		{
			ans = min (ans, cur_speed + x/(i*f + 2));
			cur_speed += c/(i*f + 2);
		}
		cout << "Case #" << k++ << ": ";
		cout << fixed << setprecision (7) << ans << endl;
	}
}