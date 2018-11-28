#include <fstream>
#include <iomanip>
#include <iostream>
using namespace std;

char filename[30]="B-large.in";

int main(int argc, char const *argv[])
{
	ifstream in(filename);
	ofstream out("2out");
	out.fill('0');
	out.precision(7);

	int casenum;
	in>>casenum;

	for(int i=0;i<casenum;i++){
		out<<"Case #"<<i+1<<": ";
		double farm;
		double added;
		double goal;

		in>>farm>>added>>goal;

		double rate=2;

		if(goal<=farm){
			out<<setprecision(7)<<setiosflags(ios::fixed)<<goal/rate<<endl;
			continue;
		}

		int buynum = (((goal-farm) * added / farm) -2) /added + 1;

		double needTime = 0;
		for(int i=0;i<buynum;i++){
			needTime += (farm) / rate;
			rate += added;
		}

		needTime += goal / rate;

		out<<setprecision(7)<<setiosflags(ios::fixed)<<needTime<<endl;

	}


	return 0;
}