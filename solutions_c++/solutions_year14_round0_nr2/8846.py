#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
   int tests_num;
   cin >> tests_num;

   for (auto i=0; i<tests_num; ++i)
   {
	double C, F, X;
	cin >> C >> F >> X;
	
	double time=0.00;
	double cookies=0;
	double speed=2;

	while (cookies < X)
	{
		if (X - cookies < C)
		{
		   time += (double) (X - cookies) / speed;
		   break;
		}

		time += (double) C / speed;
		cookies += C;
		if ((X-cookies+C) / (speed+F) < (X-cookies) / speed)
		{
		   speed += F;
		   cookies -= C;
		}
	}
	
        cout << fixed << std::setprecision(7);
	cout << "Case #" << i+1 << ": "  << time << endl;

   }

}
