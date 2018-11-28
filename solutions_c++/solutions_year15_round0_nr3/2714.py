#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int ucal(char l, char r){
	int i=0, j=0;
	char x[] = { '1', 'i', 'j', 'k' };
	for (int idx = 0; idx < 4; idx++){
		if (l == x[idx]) i = idx;
		if (r == x[idx]) j = idx;
	}
	int board[4][4] = 
	{ 1, 'i', 'j', 'k', 
	'i', -1, 'k', -'j', 
	'j', -'k', -1, 'i', 
	'k', 'j', -'i', -1 };

	return board[i][j];
}
int main()
{
	ifstream infile;
	infile.open("input.txt");
	ofstream outfile;
	outfile.open("output.txt");

	int t; infile >> t;
	for (int i = 1; i <= t; i++){
		string res = "NO";
		int L, X; infile >> L >> X;
		string str; infile >> str;
		int checker = 0;
		if (str.find("i") != string::npos){
			checker++;
		}
		if (str.find("j") != string::npos){
			checker++;
		}
		if (str.find("k") != string::npos){
			checker++;
		}

		if (checker != 1){
			string tmp = str;
			for (int j = 1; j < X; j++){
				str += tmp;
			}
			if (str == "ijk"){
				res = "YES";
			}
			else if (str.length() >= 3){
				int chk1 = 1, chk2 = 1, chk3 = 1;
				int c = str[0];
				int pm = 1;
				for (int j = 1; j < str.length(); j++){
					if (chk1 && char(c) == 'i'){
						chk1 = 0;
						c = str[j];
						j++;
					}
					else if (!chk1 && chk2 && char(c) == 'j'){
						chk2 = 0;
						c = str[j];
						j++;
					}
					
					if (c < 0){
						c = ucal(char(c)*-1, str[j])*-1;
					}
					else{
						c = ucal(char(c), str[j]);
					}
				}
				if (!chk1 && !chk2 && char(c) == 'k'){
					res = "YES";
				}
			}
		}
		outfile << "Case #" << i << ": " << res << endl;
	}

	infile.close();
	outfile.close();
	return 0;
}