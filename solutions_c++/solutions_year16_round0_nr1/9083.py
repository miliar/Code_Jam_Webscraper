#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <string>
#include <sstream>
using namespace std;

void printVec(vector<int> v);
bool findVec(vector<int> v, int val);

int main() {
	ifstream infile("in.in");
	ofstream outfile("out.txt");
	int tasks;
	infile >> tasks;

	int line;
	for (int i = 1; i <= tasks; i++) {
		vector<int> arr;
		infile >> line;
		int n = line;
		int c = 1;

		if (n != 0) {
			while (arr.size() < 10) {
				line = n*c;
				// cout << "Line: " << line;
				c++;

				ostringstream ss;
				ss << line;
				string line_str = ss.str();
				
				for (int j = 0; j < line_str.size(); j++) {
					if (!findVec(arr, (int) line_str[j])) {
						arr.push_back((int) line_str[j]);
					}
					// printVec(arr);
				}
			}

			outfile << "Case #" << i << ": " << line << "\n";
		} else {
			outfile << "Case #" << i << ": " << "INSOMNIA" << "\n";
		}
	}
}

bool findVec(vector<int> v, int val) {
	for (int i = 0; i < v.size(); i++) {
		if (v[i] == val) {
			return true;
		}
	}

	return false;
}

void printVec(vector<int> v) {
	for (int i = 0; i < v.size(); i++) {
		cout << v[i] << " ";
	}
	cout << endl;
}