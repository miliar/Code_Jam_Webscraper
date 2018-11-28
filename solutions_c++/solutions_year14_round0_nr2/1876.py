#include<fstream>
#include<vector>
#include<string>

using namespace std;
double cookie_time(double C, double F, double X);
int main()
{
	ifstream in("G:\\job\\google_jam\\data\\B-large.in");
	ofstream out("G:\\job\\google_jam\\data\\B-large-practice.out");
	int num_cases;
	in >> num_cases;
	for(int i = 1; i <= num_cases; ++i)
	{
		double C, F, X, time;
		in >> C >> F >> X;
		time = cookie_time(C, F, X);
		out << "Case #" << i << ": ";
		out.setf(ios::fixed); out.precision(7);
		out << time << endl;
	}
	out.close();
	in.close();
}

double cookie_time(double C, double F, double X)
{
	double rate = 2.0;
	double farm_time = 0.0;

	//not buy farm
	double time1 = farm_time + X/rate;

	// buy farm
	farm_time = farm_time + C/rate;
	rate = rate + F;
	double time2 = farm_time + X/rate;

	while(time2 < time1)
	{
		time1 = time2;
		farm_time = farm_time + C/rate;
		rate = rate + F;
		time2 = farm_time + X/rate;
	}
	return time1;
}