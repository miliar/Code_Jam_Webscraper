#include <fstream>
#include <iostream> 

using namespace std;
void printCase(ofstream&,int); 

int main() {

	ifstream input("smalla.in");
	ofstream output("outputsmalla.txt");

	int numTests; 
	input >> numTests;
	for(int test = 1; test <= numTests; test++) { 
		int r_initial, counter = 0;
		double t_initial;
		input >> r_initial;
		input >> t_initial;
		int r = r_initial; 
		double t = t_initial; 
		while(t - (2.0*r+1.0) >= 0 || counter == 0) { 
			counter++; 
			t = t - (2.0*r+1.0);
			r = r + 2; 
		}
		printCase(output,test);
		output << counter << endl; 
	}
	return 0;
}

void printCase(ofstream& file, int num) { 
	file << "Case #" << num << ": ";
}

