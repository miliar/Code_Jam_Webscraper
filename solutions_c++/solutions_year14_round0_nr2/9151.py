#include <iostream>
#include <cstdlib>
#include <string>
#include <iomanip>
#include <sstream>

using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	string temp;
	int num_tests = 0;
	getline(cin, temp);
	num_tests = atoi(temp.c_str());

	long double C = 0, F = 0, X = 0, R = 2.0;
	long double T;
	ostringstream out;
	out << fixed << setprecision(7);
	for(int test = 1; test <= num_tests; ++test){
		T = 0.0;
		R = 2.0;
		getline(cin,temp);
		istringstream in(temp);

		in >> C >> F >> X;

		while(X/R > C/R + X/(R+F)){
			T += C/R;
			R += F;
		}
		T += X/R;
		out << "Case #" << test << ": " << T << '\n';
	}
	cout << out.str();

	return 0;
}