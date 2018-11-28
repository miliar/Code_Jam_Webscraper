#include<iostream>
#include <iomanip>
#include<fstream>
using namespace std;

int main()
{
	ifstream ist("input.in");
	ofstream ost("output.out");
	int n,i;
	ist >> n;
	for (i = 0;i<n;i++)
	{
		double c,f,x;
		double total_time = 0;
		double speed = 2.0;
		bool buydir = false;
		ist >> c >> f>>x;
		if (x < c) total_time = x / 2.0;
		else
		{
			double remain = x - c;
			while (buydir != true)
			{
				total_time += c / speed;
				if ((remain / speed)<(x / (speed + f))) buydir = true; 
				else speed += f;
			}
			total_time += remain / speed;
		}
		ost<<"Case #"<<i+1<<": "<<fixed<<setprecision(7)<<total_time<<endl;
	//	printf("%.7f\n",total_time);
	}
	system("pause");
}