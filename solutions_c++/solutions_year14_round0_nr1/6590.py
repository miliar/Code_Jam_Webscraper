#include <iostream>
#include <fstream>
#include <vector>

#include <boost/algorithm/string.hpp>


using namespace std;

void print_v(vector<string> &v) {
	for (unsigned i = 0; i < v.size(); i++) {
		cout << v[i] << " ";
	}
	cout << endl;
}

void compare_and_print(vector<string> &v1, vector<string> &v2, int case_num, ofstream &out_stream) {
	int count = 0;
	string number;

	//print_v(v1);
	//print_v(v2);
	//cout << endl;

	for (int i = 0; i < 4; i++) {
		for (int j = 0; j < 4; j++) {
			if (v1[i].compare(v2[j]) == 0) {
				number = v1[i];
				count++;
			}
		}
	}

	out_stream << "Case #" << case_num << ": ";


	if (count == 0) {
		out_stream << "Volunteer cheated!" << endl;
	} else if (count == 1) {
		out_stream << number << endl;
	} else {
		out_stream << "Bad magician!" << endl;
	}
}


int main (int argc, char *argv[]) {

	if (argc != 2) {
		cout << "usage error" <<endl;
		return 0;
	}

	ofstream out_stream;
  out_stream.open ("output");
  

	ifstream in_stream;
	in_stream.open(argv[1]);
	string line;

	getline(in_stream, line);
	int num_test_case = atoi(line.c_str()); 

	for (int i = 0; i < num_test_case; i++) {

		getline(in_stream, line);
		int row_1_num = atoi(line.c_str());
		vector<string> row_1_vector;

		for (int j = 1; j <= 4; j++) {
			getline(in_stream, line);
			if (j == row_1_num) 
				boost::split(row_1_vector, line, boost::is_any_of(" "));	
		} 

		getline(in_stream, line);
		int row_2_num = atoi(line.c_str());
		vector<string> row_2_vector;

		for (int j = 1; j <= 4; j++) {
			getline(in_stream, line);
			if (j == row_2_num) 
				boost::split(row_2_vector, line, boost::is_any_of(" "));	
		} 

		compare_and_print(row_1_vector, row_2_vector, i + 1, out_stream);
	}

	in_stream.close();
	out_stream.close();
	return 0;
}