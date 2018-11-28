#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int main()
{
	ifstream infile;
	infile.open("input.txt");
	ofstream outfile;
	outfile.open("output.txt");
	int t; infile >> t;
	for (int i = 1; i <= t; i++){
		int n; infile >> n;
		string s; infile >> s;
		int res = 0;
		int tot = s[0] - '0';
		int tmp = 0;
		for (int j = 1; j < s.length(); j++){
			if (s[j] != 0 && tot < j){
				tmp = j - tot;
				if (tmp < 0){
					tmp = 0;
				}
				tot += tmp;
				res += tmp;
			}
			tot += s[j] - '0';
		}
		outfile << "Case #" << i << ": " << res << endl;
	}
	infile.close();
	outfile.close();
	return 0;
}