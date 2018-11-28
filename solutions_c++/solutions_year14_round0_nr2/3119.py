#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

void ptc(int t, double ans)
{
	string tp = "Case #";
	cout << setprecision(7) << fixed;
	cout << tp << t << ": " << ans << endl;
}


int main()
{
	int n;
	cin >> n;
	for(int t = 1; t <= n; t++)
	{
		double cost, fbonus, target;
		cin >> cost >> fbonus >> target;
		double rate = 2.0;
		double spent = 0.0;
		double currentMin = 1000000000;

		while(true)
		{
			double noMoreFarm = target / rate + spent;
			if(noMoreFarm > currentMin)
				break;
			currentMin = noMoreFarm;
			spent += cost / rate;
			rate += fbonus;
		}
		ptc(t, currentMin);
	}
}



