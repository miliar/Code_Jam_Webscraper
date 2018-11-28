#include<iostream>
#include<fstream>
#include<iomanip>
 
using namespace std;

double fun(double c, double f, double x)
{
	double summ = 0;
	double temp = 2;
	while(1)
	{
		if((c/temp + x/(temp+f)) < x/temp) 
		{
			summ +=c/temp;
			temp +=f;
		}
		else
		{
			summ +=x/temp;
			return summ;
			break;
		}
	}
}

int main()
{
	ifstream in("B-large.in");
	ofstream out("out.txt");
	int count = 0;
	in>>count;
	for(int i = 0; i < count; i++)
	{
		int t = i + 1;
		double c,f,x = 0.0;
		in>>c>>f>>x;
		out << "Case #" << t << ": ";
		out << fixed << setprecision (7) <<  fun(c,f,x)<<endl;
	}
	return 0;
}