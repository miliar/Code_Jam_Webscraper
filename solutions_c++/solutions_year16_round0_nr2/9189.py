#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <string>
#include <sstream>
using namespace std;

bool check(string stack);

int main() {
	ifstream infile("in.in");
	ofstream outfile("out.txt");
	int tasks;
	infile >> tasks;

	string line;
	int res = 0;
	for (int i = 1; i <= tasks; i++) {
		infile >> line;

		while (!check(line)) {
			res++;
			bool flag1 = false;
			bool flag2 = false;

			for (int j = 0; j < line.size(); j++) {
				if (line[j]=='+'&&j==0) {
					flag1 = true;
				}

				if (line[j]=='-'&&j==0) {
					flag2 = true;
					if (j==line.size() - 1) {
						line[0] = '+';
						break;
					}
				}

				if (flag2==true&&(line[j]=='+')) {
					for (int k = 0; k < j; k++) {
						line[k] = '+';
					}
					break;
				} 

				if (flag1==true&&(line[j]=='-')) {
					for (int k = 0; k < j; k++) {
						line[k] = '-';
					}
					break;
				}

				if (flag2==true&&(j==line.size()-1)) {
					for (int k = 0; k < line.size(); k++) {
						line[k] = '+';
					}
					break;
				}	
			}
		}

		outfile << "Case #" << i << ": " << res << "\n";
		res = 0;
	}		
}

bool check(string stack) {
	for (int i = 0; i < stack.size(); i++) {
		if (stack[i] == '-')
			return false;
	}

	return true;
}