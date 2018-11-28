#include <iostream>
#include <string>
#include <vector>
#include<iomanip>
using namespace std;



int main()
{
	int cases;
	cin>>cases;
	int T = 1;
	double C,F,X,times;
	double remainX,remainC;
	double speed;
	while(T<=cases)
	{
		times = 0.0;
		cin>> C>>F>>X;
		remainX = X;
		remainC = C;
		speed = 2.0;
		while(remainX>0)
		{
			if(remainX/speed > (remainC/speed+ remainX/(speed+F)) )
			{
				times += remainC/speed;
				speed += F;
			}
			else
			{
				times+=remainX/speed;
				break;
			}
		}

		cout<<"Case #"<<T<<":  "<<setiosflags(ios::fixed)<<setiosflags(ios::right)<<setprecision(7)<<times<<endl;
		T++;
	}

	return 0;

}