#include <iostream>
#include <iomanip> // std:setprecision
using namespace std;

int main()
{
	int T, t;
	double C, F, X;
	double t1, t2;
	bool isfirst;

	cin >> T;	
	for(int t = 1; t <= T; t++)
	{
		cin >> C >> F >> X;
		
		//t2 = 99999999;
		isfirst = true;
		for(int cnt = 0; ; cnt++)
		{
			t1 = 0;
			for(int i = 0; i < cnt; i++)
				t1 += C/(2 + i * F);

			t1 += X/(2 + cnt * F);
		
			if (isfirst)
			{	
				t2 = t1;
				isfirst = false;	
			}	
			if (t1 > t2)
			{
				cout << "Case #" << t << ": ";
				cout << setprecision(7) << fixed << t2 << endl;
				break;
			}
			else
			{
				t2 = t1;
			}
		}
	}

	return 0;
}
