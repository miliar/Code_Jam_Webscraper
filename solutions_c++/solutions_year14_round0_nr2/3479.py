#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	int cases = 0;
	int count = 1;
	cin >> cases;
	while(count <= cases)
	{
		double c, f, x;
	        cin >> c >> f >> x;
		double time = 0.0;
		double r = 0;
		double g = 2.0;
	        while((x - c) / g > x / (g + f))
		{
			time = time + c / g;
			g = g + f;
		}	
		time = time + x / g;
		cout << "Case #" << count << ": " << fixed << setprecision(7) << time << endl;
		count++;
	}
	return 0;
}
