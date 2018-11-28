#include <iostream>  
#include <fstream>
#include <vector>
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
string CountingSheep(int start) {
	vector<bool> been(10, false);
	int bc = 0;

	for (int n = 1; n < 1002; n++) {
		int tmp = start*n;
		while (tmp > 0) {
			int rem = tmp % 10;
			tmp /= 10;
			if (!been[rem]) {
				been[rem] = true;
				bc++;
				if (bc == 10) return to_string(start*n);
			}
		}
	}
	return "INSOMNIA";
}
void main() {
	ifstream infile("2016Qual\\A-large.in");
	ofstream outfile("2016Qual\\A-large.out");
	int cnt;
	infile >> cnt;

	for (int n = 1; n <= cnt; n++) {
		int num;
		infile >> num;
		string ret = CountingSheep(num);
		outfile << "Case #" + to_string(n) + ": " + ret << "\n";
	}
	
}