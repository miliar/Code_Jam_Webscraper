#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <iomanip>
#include <string>
#include <sstream>
using namespace std;

ifstream fin("B-large.in");
ofstream fout("B-large.out");

struct State
{
	double cookies;
	double rate;
	double timeElapsed;
	State(const State & state){
		this->cookies = state.cookies;
		this->rate = state.rate;
		this->timeElapsed = state.timeElapsed;
	}
	State(double cookies, double rate, double timeElapsed){
		this->cookies = cookies;
		this->rate = rate;
		this->timeElapsed = timeElapsed;
	}
};

double timeInSeconds(double C, double F, double X)
{
	State state(0.0, 2.0, 0.0);
	while (state.cookies < X)
	{
		double time1 = (X-state.cookies)/state.rate;
		double time2 = C/state.rate + X/(state.rate + F);
		if (time1 < time2)
			return (state.timeElapsed + time1);
		else{
			state.cookies = 0.0;
			state.timeElapsed += (C/state.rate);
			state.rate += F;
		}
	}
	return state.timeElapsed;
}

int main()
{
	int T=0;
	fin >> T;
	for (int t=1; t<=T; t++)
	{
		double C=0.0, F=0.0, X=0.0;
		fin >> C >> F >> X;
		double res = timeInSeconds(C, F, X);
		fout << "Case #" << t << ": " << setprecision(15) << res << "\n";
		cout << "Case #" << t << ": " << setprecision(15) << res << "\n";
	}

	system("PAUSE");
	return 0;
}