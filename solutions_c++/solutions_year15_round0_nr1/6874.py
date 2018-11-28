#include <iostream>
#include <sstream>
#include <fstream>

using namespace std;

#define S_MAX 6
#define T_MAX 100

void main() {
	
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	unsigned T;
	unsigned S;
	int count;
	int extra_count;
	int num_audience;
	string str_audience;
	stringstream str;

	fin >> T;

	for(unsigned j= 1; j<= T; j++) {

		fin >> S;
		fin >> str_audience;

		count= 0;
		extra_count= 0;

		for(unsigned i= 0; i < str_audience.size(); i++) {

			str.clear();
			str << str_audience[i];
			str >> num_audience;

			if(((count + extra_count)<i) && (num_audience != 0)) {
				extra_count += (i - count - extra_count);
			}
			
			count+= num_audience;
		}

		fout<<"Case #" << dec << j << ": " << extra_count << endl;
	}

	fin.close();
	fout.close();
}