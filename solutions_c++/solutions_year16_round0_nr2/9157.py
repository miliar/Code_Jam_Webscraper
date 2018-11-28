#include <string>
#include <unordered_map>
#include <vector>
#include <iostream>
#include <math.h>
#include <fstream>
using namespace std;



int main() {
	ifstream myfile("input.in");
	ofstream out("output.out");
	int T,N;
	myfile >> T;
	string dirt;
	getline(myfile, dirt);

	for (int i =1; i <= T; ++i) {
		string str;
		getline(myfile, str);
		char prev = str[0];
		cout << str << endl;

		if (str.size() == 1 && prev == '+') {
			out << "Case #" << i <<": " << "0" << endl;
			continue;
		} else if (str.size() == 1 && prev == '-'){
			out << "Case #" << i <<": " << "1" << endl;
			continue;
		}

		int count = 0;
		for (int j = 1; j < str.size(); ++j) {
			if (str[j] != prev) {
				++count;
			}
			prev = str[j];
		}

		if (prev == '-')
			++count;

		out << "Case #" << i <<": "  << count << endl;


	}
	return 0;
}


