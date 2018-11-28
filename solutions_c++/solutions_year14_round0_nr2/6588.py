#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <iomanip>
#include <boost/algorithm/string.hpp>


using namespace std;

// Print vector content
template<class T>
void print_v(vector<T> &v) {
	for (unsigned i = 0; i < v.size(); i++) {
		cout << v[i] << " ";
	}
	cout << endl;
}


int main (int argc, char *argv[]) {

	// Check usage
	if (argc != 2) {
		cout << "usage error" <<endl;
		return 0;
	}

	// Input file
	ofstream out_stream;
  out_stream.open ("output");
  
  // Output file
	ifstream in_stream;
	in_stream.open(argv[1]);

	// Get test case number
	string line;
	getline(in_stream, line);
	int test_case_num = atoi(line.c_str()); 

	for (int i = 1; i <= test_case_num; i++) {
		getline(in_stream, line);
		vector<string> input_str_v;
		vector<double> input_str_double;

		boost::split(input_str_v, line, boost::is_any_of(" "));	

		for (unsigned j = 0; j < input_str_v.size(); j++) 
			input_str_double.push_back(atof(input_str_v[j].c_str()));
		
		double cost = input_str_double[0];
		double increment = input_str_double[1];
		double goal = input_str_double[2];

		double t = 0;
		double rate = 2;

		//print_v(input_str_double);

		while (true) {
			double buy_t = (goal) / (rate + increment);
			double not_buy_t = (goal - cost) / rate;

			if (buy_t < not_buy_t) {
				t += cost / rate;
				rate += increment;

			} else {
				t += goal / rate;
				break;
			}
			
		}
		out_stream << fixed;
		out_stream << "Case #"<< i << ": " << setprecision(7) << t << endl;
	}

	// Close files
	in_stream.close();
	out_stream.close();

	return 0;
}