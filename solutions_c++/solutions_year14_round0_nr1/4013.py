#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<algorithm>
#include<fstream>
#include<sstream>
#include <cmath>
#include <iomanip>
#include "stdio.h"

using namespace std;
typedef  double ld;

string process_testcase(string s)
{
	istringstream iss(s);
	ld C, F, X;
	ld cur_rate = 2.0;
	ld time_req = 0.0;

	iss >> C >> F >> X;
	
	while (1) {
		ld without_fact = X / cur_rate;
		ld with_new_fact = (ld)(X /(ld) (F + cur_rate)) +(ld) ((ld)C /(ld) cur_rate);

		if (with_new_fact < without_fact) {
			time_req += (ld)(C / cur_rate);
			cur_rate += F;
		}
		else {
			time_req += (ld)((ld)X /(ld) cur_rate);
			break;
		}
	}
	ostringstream oss;
	oss << std::fixed << setprecision(7) << time_req;
	// cout << "op : " << setprecision(10) << time_req << endl;
	return oss.str();
}

string process_testcase2(int first, vector<vector<int> > first_arr,
					   	int second, vector<vector<int> > second_arr)
{
	first -= 1;
	second -= 1;
	vector<int> possible_solns;

	for (int i = 0; i < 4; ++i){
		for (int j = 0; j < 4; ++j){
			if (first_arr[first][i] == second_arr[second][j]) {
				possible_solns.push_back(first_arr[first][i]);
				break;
			}
		}
	}

	ostringstream oss;
	switch (possible_solns.size())
	{
	case 0:
		oss << "Volunteer cheated!";
		break;
	case 1:
		oss << possible_solns[0];
		break;
	default:
		oss << "Bad magician!";
		break;
	}

	return oss.str();
}
int main(int argc, const char *argv[])
{
	int tc = 0;
	ifstream is;
	if (argc == 1)
		is.open("c:\\shiv\\gcj\\input.txt");
	else
		is.open(argv[1]);
	ofstream os;
	os.open("c:\\shiv\\gcj\\output.txt");

	string s;
	getline(is, s);
	istringstream iss(s);
	int numchars, dic;
	iss >> tc;

	for (int i = 1; i <= tc; i++)
	{
		os << "Case #" << i << ": ";
		getline(is, s);
		vector<vector<int> > first, second;
		int first_soln, second_soln;
		istringstream iss(s);
		iss >> first_soln;
		for (int i = 0; i < 4; ++i){
			getline(is, s);
			istringstream iss(s);
			vector<int> cur_line;
			int cur_ip;
			for (int j = 0; j < 4; ++j){
				iss >> cur_ip;
				cur_line.push_back(cur_ip);
			}

			first.push_back(cur_line);
		}

		getline(is, s);

		istringstream iss2(s);
		iss2 >> second_soln;
		for (int i = 0; i < 4; ++i){
			getline(is, s);
			istringstream iss(s);
			vector<int> cur_line;
			int cur_ip;
			for (int j = 0; j < 4; ++j){
				iss >> cur_ip;
				cur_line.push_back(cur_ip);
			}

			second.push_back(cur_line);
		}
		os << process_testcase2(first_soln, first, second_soln, second) << endl;
	}

	is.close();
	os.close();
	//getchar();
	return 0;
}