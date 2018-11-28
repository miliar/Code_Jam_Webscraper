#include<iostream>
#include<vector>
#include<deque>
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

int
old_strategy(deque<double> N, deque<double> K)
{
	int num = N.size();
	int result = 0;
	for (int i = 0; i < num; ++i) {
		double curN = N.front();
		
		bool found = false;
		for (deque<double>::iterator itr = K.begin(); itr != K.end(); ++itr) {
			if (curN < *itr) {
				found = true;
				*itr = -1;
				break;
			}
		}

		if (! found) {
			return N.size();
#if 0
			++result;
			double temp = K.front();
			K.pop_front();
			while (temp == -1) {
				temp = K.front();
				K.pop_front();
    		}
#endif
		}
		N.pop_front();
	}

	return result;
}

int
new_strategy(deque<double> N, deque<double> K)
{
	int num = N.size();
	int result = 0;
	for (int i = 0; i < num; ++i) {
		double curN = N.front();
		N.pop_front();
		double curK = K.front();
		if (curN < curK) {
			K.pop_back();
		}
		else {
			K.pop_front();
			++result;
		}
	}
	return result;
}
string process_testcase3(deque<double>& N, deque<double>& K)
{
	int new_strategy_score = new_strategy(N, K);
	int old_strategy_score = old_strategy(N, K);

	ostringstream oss;
	oss << new_strategy_score << " " << old_strategy_score;
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
		istringstream iss(s);
		int num;
		iss >> num;
		deque<double> N, K;
		getline(is, s);
		istringstream iss2(s);
		for (int i = 0; i < num; ++i){
			double cur_val;
			iss2 >> cur_val;
			N.push_back(cur_val);
		}

		getline(is, s);
		istringstream iss3(s);
		for (int i = 0; i < num; ++i){
			double cur_val;
			iss3 >> cur_val;
			K.push_back(cur_val);
		}
		sort(N.begin(), N.end());
		sort(K.begin(), K.end());

		os << process_testcase3(N, K) << endl;
	}

	is.close();
	os.close();
	//getchar();
	return 0;
}