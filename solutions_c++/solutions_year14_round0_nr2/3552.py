#include <fstream>
#include <iomanip>
using namespace std;
int main()
{
	ifstream cin("B-large.in");
	ofstream cout("B-large.out");

	int t;
	cin >> t;
	double c, f, x;
	double time, growth, timetofarm, timetosuccess,
		newtimetosuccess;
	cout << fixed << setprecision(7);
	for (int i = 1; i <= t; ++i)
	{
		cin >> c >> f >> x;
		time = 0; growth = 2;
		timetofarm = 0; timetosuccess = x / growth;
		newtimetosuccess = 0;
		cout << "Case #" << i << ": ";
		while (true)
		{
			timetofarm = c / growth;
			newtimetosuccess = x / (growth + f);
			timetosuccess = x / growth;

			if (timetofarm + newtimetosuccess < timetosuccess)
			{
				growth += f;
				time += timetofarm;
			}
			else
			{
				time += timetosuccess;
				cout << time << endl;
				break;
			}
		}
	}
}