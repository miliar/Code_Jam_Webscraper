#include<iostream>
#include<string>
#include<fstream>

using namespace std;
int main() {
	ifstream input("input.in");
	ofstream output("output.txt");
	int t; input >> t;
	for (int k = 1; k <= t; ++k){
		int smax; input >> smax;
		string val; input >> val;
		int total = val[0] - '0', needed = 0;
		for (int i = 1; i < val.size(); ++i) {
			if (i > total && val[i] != '0') {
				needed += i - total;
				total += i - total;
			}
			total += val[i] - '0';
		}
		output << "Case #" << k << ": " << needed << endl;
	}
	return 0;
}