#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>
#include <algorithm>
#include <iomanip>
using namespace std;


int main(int argc, char* argv[])
{
	string fname;
	std::cin >> fname;
	string ifname = fname + ".in";
	string ofname = fname + ".out";
	ifstream in(ifname.c_str());
	ofstream out(ofname.c_str());

	int T;
	double C; // cookie farm cost
	double F; // farm upgrade gives this much cookies
	double X; // goal
	in >> T;
	

	for (int i = 0; i < T; ++i) {
		double actGain = 2.0;
		double time = 0.0;
		in >> C >> F >> X;
		while (true) {
			double tNextFarm = C / actGain;
			double tGoalWithNextFarm = X / (actGain + F);
			double tGoal = X / actGain;
			
			if (tGoal > (tGoalWithNextFarm + tNextFarm)) {
				actGain += F;
				time += tNextFarm;
			}
			else {
				time += tGoal;
				out.setf(std::ios::fixed, std::ios::floatfield);
				out.precision(7);
				out << "Case #" << i + 1 << ": " << time << std::endl;
				break;
			}
		}
	}
	in >> C;
	return 0;
}