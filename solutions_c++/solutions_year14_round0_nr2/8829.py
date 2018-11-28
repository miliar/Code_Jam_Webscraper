#include <iostream>
#include <vector>
#include <string>
#include <iomanip>
using namespace std;

int main()
{
	cout << setprecision(10) << fixed;
	int cases = 0;
	cin >> cases;
	for(int j = 0; j < cases; j++)
	{
		double c,f,x;
		cin >> c >> f >> x;

		double cps = 2.0;
		double resultOld = 9999999999999.0;
		double resultNew = x/cps;
		vector<double> times;
		
		for(int countFarms = 0; resultNew < resultOld;countFarms++)
		{
			resultOld = resultNew;
			
			for(int i = countFarms-1; i < countFarms; i++)
			{
				times.push_back(c/cps);
				cps += f;
			}
			//times.push_back(x/cps);
			double result = 0;
			//std::cout << "Times: " << endl;
			for(int i = 0; i < times.size(); i++)
			{
				result += times[i];
				//cout << "\t-" << times[i] << endl;
			}
			result += (x/cps);
			resultNew = result;
			//cout << "RO: " << resultOld << " RN: " << resultNew << endl;
		}

		cout << "Case #" << j+1 << ": " << resultOld << endl;
	}
	return 0;
}