#include <iostream>
#include <string>
#include <fstream>

using namespace std;

#define to_digit(c) (c-'0')

int process(string s) {
	// First char is s_max
	int s_max = to_digit(s.c_str()[0]);
	const char *config = s.substr(2).c_str();
	
	int *grid = new int[s_max+1];
	
	int standing = to_digit(config[0]);
	int added = 0;

	for(int i = 1; i <= s_max; i++) {
		if (standing < i) {
			added += i - standing;
			standing += i - standing;
		}
		
		
		standing += to_digit(config[i]);
	}
	return added;
}


int main(int argc, char **argv) {
	if(argc < 2) {
		cout << "Error: no in file provided." << endl;
		return 0;
	}
	
	string line;
	ifstream in_file (argv[1]);
	int *results;
	int n_inputs;
	
	if(in_file.is_open()) {
		getline(in_file, line);
		n_inputs = atoi(line.c_str());
		results = new int[n_inputs];
		
		for(int i = 0; i < n_inputs; i++) {
			getline(in_file, line);
			results[i] = process(line);		
			
		}
		
		in_file.close();
	}
	else {
		cout << "Unable to open file." << endl;
	}
	
	ofstream myfile;
	myfile.open ("test.out");

	for(int i = 0; i < n_inputs; i++) {
		myfile << "Case #" << i+1 << ": " << results[i] << endl;
	}
	myfile.close();
	
	return 0;	
	
}