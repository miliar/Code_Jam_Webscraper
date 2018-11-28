#include <iostream>
using namespace std;
double best_time(double C, double F, double X);
void fun()
{
	int T;
	cin >> T;
	double C, F, X;

  	std::cout.precision(7);
 	std::cout.setf( std::ios::fixed, std:: ios::floatfield );
	for(int i = 1; i <= T; ++i)
	{
		cin >> C >> F >> X;
		cout << "Case #" << i << ": ";
		cout << best_time(C, F, X) <<endl;	
	}
}

double best_time(double C, double F, double X)
{
	int farm = 0;
	double time = 0;
	while(true)
	{
		double t1 = X / (farm *F + 2);
		double t2 = C / (farm * F + 2)  + X / ((farm + 1) * F + 2);
		if(t1 > t2)
		{
			time += C / (farm * F + 2);
			++farm; 
		}
		else
		{
			time += t1;
			return time;
		}
	}
}

int main()
{
	fun();
}
