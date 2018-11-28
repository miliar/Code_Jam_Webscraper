#include<iostream>
using namespace std;
int main()
{
	long double F , C , X;
	int T;
	cin >> T;
	cout.precision(7);
	for(int t = 1;t <= T;t ++)
	{
		cin >> C >> F >> X;
		long double ans = 0.0 , rate = 2.0;
		while(true)
		{
			long double t1 = X / rate;
			long double t2 = C / rate + X / (rate + F);
			if(t1 < t2)
			{
				ans += t1;
				break;
			}
			else
			{
				ans += C / rate;
				rate += F;
			}
		}
//		cout << rate << endl;
		cout <<"Case #" << t << ": " <<  fixed << ans << endl;
	}
	return 0;
}
