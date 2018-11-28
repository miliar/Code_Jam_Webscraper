#include<iostream>
#include<string>
#include<memory>
#include<cstring>
#include<set>
#include<stdlib.h>
using namespace std;


int main()
{
	int t,tt;
	cin >> tt;
	double c,f,x;
	double speed;
	double time;
	for(t = 1; t <= tt; t ++)
	{
		speed = 2.0;
		time = 0;
		cin >> c >> f >> x;
		time += c/speed;
		while((x-c)/speed > x/(speed+f))
		{
			speed+=f;
			time+=c/speed;
		}
		time+= (x-c)/speed;
		cout.setf(ios::fixed);
		cout.precision(7);
		cout << "Case #" << t << ": " << time << endl;
	}
	return 0;
}