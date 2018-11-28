#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for(int i=0; i<t; i++)
	{
		//cout << "ye" << i <<endl;
		double c, f, x;
		cin >> c >> f >> x;
		//(x-c)/(2+k*f)*f > c
		int k=0;
		while(true)
		{	//cout << "inside\n";
			if((x-c)/(2+k*f)*f>c) k++;
			else break;
		}
		double time=0.0;
		for(int j=0; j<=k; j++)
		{
			time+= c/(2+j*f);
		}
		time+= (x-c)/(2+k*f);
		int time2 = (int)time;
		int digits = 0;
		while(time2>0)
		{
			time2=time2/10;
			digits++;
		}
		cout << "Case #" << i+1<< ": " << setprecision(7+digits) << time << endl;
	}
}
