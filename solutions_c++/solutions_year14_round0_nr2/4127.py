#include <iostream>
#include <iomanip>

using namespace std;
int main()
{
	int t;
	double c,f,x,s,tt,tb,tf,tc;
	s=2.0;
	cout << setprecision(7) << fixed;
	cin >> t;
	for(int i=1;i<=t;i++)
	{
		cin >> c;
		cin >> f;
		cin >> x;
		s=2.0;
		tc=0.0;
		while(1)
		{
			tt=x/s;
			tb=c/s;
			tf=x/(s+f);
			if(tt<=tb+tf)
			{
				tc+=tt;
				break;
			}
			else
			{
				tc+=tb;
				s+=f;
			}
		}
		cout << "Case #" << i << ": " << tc << endl;
	}
	return 0;
}
