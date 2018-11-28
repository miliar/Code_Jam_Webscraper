#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <array>
#include <algorithm>
#include <iomanip>

using namespace std;

struct Problem {
	double building_cost; // C
	double building_rate; // F
	double winning_cost;  // X
};

double solve(const Problem& p){

	double rate = 2;
	double buildup_time = 0;
	for (;;){
		double if_built_rate = rate + p.building_rate;
		double if_built_buildup_time = buildup_time + (p.building_cost / rate);

		double no_build_time = buildup_time + (p.winning_cost / rate);
		double build_time = if_built_buildup_time + (p.winning_cost / if_built_rate);
/*
		cout << "Rate:\t" << rate << endl;
		cout << "Buildup:\t" << buildup_time << endl;
		cout << "Time Build:\t" << build_time << endl;
		cout << "Time Nobuild:\t" << no_build_time << endl;
*/
		if (no_build_time <= build_time) return no_build_time;

		rate = if_built_rate;
		buildup_time = if_built_buildup_time;
	}

	return 0;
}

int main(int argc, char** argv){
	ifstream in(argv[1]);

	string line;

	int T;
	in >> T;

	cout << setprecision(7) << fixed;

	for (int i = 1; i <= T; i += 1){
		Problem p;
		in >> p.building_cost >> p.building_rate >> p.winning_cost;

		double answer(solve(p));

		cout << "Case #" << i << ": " << answer << endl;
	}
}