#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

int main()
{
	ifstream fin("test.in");
	ofstream fout("test.out");
	int T = 0;
	fin >> T;
	for(int t = 1;t <= T;t++)
	{
		double price = 0.0f, val = 0.0f, target = 0.0f, ans = 0.0f;
		fin >> price >> val >> target;
		double curSpeed = 2.0f;
		int num = 0;
		bool flag = true;
		if(target < price)
		{
			ans = target / curSpeed;
			flag = false;
		}

		while(flag)
		{
			double t1 = target / curSpeed;
			double t2 = (price / curSpeed) + target / (val + curSpeed);
			if(t1 < t2)
			{
				ans += t1;
				break;
			}
			else
			{
				ans += price / curSpeed;
				curSpeed += val;
			}
		}
		fout << "Case #"<< t << ": " << setiosflags(ios::fixed) << setprecision(7) << ans;
		if(t != T)
			fout << endl;
	}

	return 0;
}