#include <iostream>  
#include <fstream>
#include <vector>
#include <string>
using namespace std;
string RevengePancakes(string str) {
	int ret = 0;
	if (str[0] == '-') ret++;
	for (int n = 1; n < str.size(); n++)
		if (str[n] != str[n - 1] && !(str[n] == '+' && str.find_last_of('-') < n)) {
			if (ret == 0 && str[n] == '-') ret++;
			ret++;
		}

	return to_string(ret);
}
void main() {
	ifstream infile("2016Qual\\B-large.in");
	ofstream outfile("2016Qual\\B-large.out");
	int cnt;
	infile >> cnt;

	for (int n = 1; n <= cnt; n++) {
		string str;	
		infile >> str;
		string ret = RevengePancakes(str);
		outfile << "Case #" + to_string(n) + ": " + ret << "\n";
	}

}