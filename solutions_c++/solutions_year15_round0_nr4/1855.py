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
		int x, r, c; infile >> x >> r >> c;
		string res = "RICHARD";
		if (x == 1){
			res = "GABRIEL";
		}
		else if (x == 2){
			if (r*c >= 2 && r*c % 2 == 0){
				res = "GABRIEL";
			}
		}
		else if (x == 3){
			if (r*c > 3 && (r == 3 || c == 3)){
				res = "GABRIEL";
			}
		}
		else{
			if (r*c >= 12){
				res = "GABRIEL";
			}
		}
		outfile << "Case #" << i << ": " << res << endl;
	}

	infile.close();
	outfile.close();
	return 0;
}