#include <iostream>
#include <iomanip>
using namespace std;
double cookieClicker(double c, double f, double x, double speed)
{
	
	if(x/speed <= (c/speed + x/(speed+f)) ) return x/speed;
	else{
		return c/speed + cookieClicker(c, f, x, speed+f);

	}
}
int main()
{
	int num;
	cin >> num;
	for(int i =1;i <= num; i ++)
	{
		double C, F, X;
		cin >>C;
		cin >>F;
		cin >>X;
		cout<<"Case #"<<i<<": "<<fixed<<setprecision(7)<<cookieClicker(C,F,X,2.0)<<endl;
		
	}
	return 0;
}