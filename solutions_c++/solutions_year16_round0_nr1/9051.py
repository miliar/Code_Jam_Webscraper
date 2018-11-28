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

	for (int i =1; i <= T; ++i){
		myfile >> N;
		int num = N;
		vector<bool> digits(10);
		int counter = 10;
		if (num == 0) {
			out << "Case #" << i <<": INSOMNIA" << endl;
			continue;
		}

		int k = 1;
		while (counter != 0)  {
			num = k*N;
			string str = to_string(num);
			for (int j = 0; j < str.size(); ++j) {
				char c = str[j];
				if (!digits[atoi(&c)]) {
					digits[atoi(&c)] = true;
					--counter;
				}
			}
			++k;
		}

		out << "Case #" << i <<": " << num << endl;


	}
	return 0;
}


