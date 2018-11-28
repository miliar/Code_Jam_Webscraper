#include <iostream>
#include <string>
#include <fstream>

using namespace std;



int main() {
	ifstream input("D-small-attempt0.in");
	ofstream output("D_small_answer.txt");
	string num;
	getline(input, num);
	int n = stoi(num);
	for (int i = 0; i < n; ++i) {
		output << "case #" << i + 1 << ": ";
		getline(input, num);
		int position = num.find_first_of(' ');
		int S = stoi(num.substr(0, position));
		for (int i = 1; i <= S; ++i) {
			output << i << ' ';
		}
		output << endl;
	}
	return 0;
}