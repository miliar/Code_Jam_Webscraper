#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector> 

using namespace std;
 
int main()
{
	ifstream infile;
	infile.open("A-large.in");
	ofstream outfile;
	outfile.open("A-large.out");

	string line;
	int CaseNum, flag_X, flag_O, result, completed;
	char t[4][4];
	istringstream stream;
	getline(infile, line);
	stream.str(line);
	stream >> CaseNum;
	
	for (int i = 0; i < CaseNum; i++) {
		ostringstream ss;
		result = 0;
		completed = 1;
		for (int row = 0; row < 4; row++) {
			getline(infile, line);
			for (int col = 0; col < 4; col++) {
				t[row][col] = line[col];
				if (line[col] == '.') completed = 0;
			}
		}

		for (int p = 0; p < 4; p++) {
			flag_X = 1;
			flag_O = 1;
			for (int k = 0; k < 4; k++) {
				if (t[p][k] == 'O' || t[p][k] == '.')
					flag_X = 0;
				if (t[p][k] == 'X' || t[p][k] == '.')
					flag_O = 0;
			}
			if (flag_X) {
				ss << "Case #" << (i + 1) << ": X won\n";
				result = 1;
				break;
			}
			if (flag_O) {
				ss << "Case #" << (i + 1) << ": O won\n";
				result = 1;
				break;
			}
			
			flag_X = 1;
			flag_O = 1;
			for (int k = 0; k < 4; k++) {
				if (t[k][p] == 'O' || t[k][p] == '.')
					flag_X = 0;
				if (t[k][p] == 'X' || t[k][p] == '.')
					flag_O = 0;
			}
			if (flag_X) {
				ss << "Case #" << (i + 1) << ": X won\n";
				result = 1;
				break;
			}
			if (flag_O) {
				ss << "Case #" << (i + 1) << ": O won\n";
				result = 1;
				break;
			}
		}
		
		flag_X = 1;
		flag_O = 1;
		if (!result) {
			for (int p = 0; p < 4; p++) {
				if (t[p][p] == 'O' || t[p][p] == '.')
					flag_X = 0;
				if (t[p][p] == 'X' || t[p][p] == '.')
					flag_O = 0;
			}
			if (flag_X) {
				ss << "Case #" << (i + 1) << ": X won\n";
				result = 1;
			}
			if (flag_O) {
				ss << "Case #" << (i + 1) << ": O won\n";
				result = 1;
			}
		}

		flag_X = 1;
		flag_O = 1;
		if (!result) {
			for (int p = 0; p < 4; p++) {
				if (t[p][3 - p] == 'O' || t[p][3 - p] == '.')
					flag_X = 0;
				if (t[p][3 - p] == 'X' || t[p][3 - p] == '.')
					flag_O = 0;
			}
			if (flag_X) {
				ss << "Case #" << (i + 1) << ": X won\n";
				result = 1;
			}
			if (flag_O) {
				ss << "Case #" << (i + 1) << ": O won\n";
				result = 1;
			}

		}

		if (!result)
			if (completed)
				ss << "Case #" << (i + 1) << ": Draw\n";
			else
				ss << "Case #" << (i + 1) << ": Game has not completed\n";
		
		outfile << ss.str();
		getline(infile, line);
	}

	infile.close();
	outfile.close();
  	return 0;
}
/*

		int *a = tmp;
		istringstream stream1;
		getline(infile, line);
		stream1.str(line);
		while (stream1 >> *(a++));

		int size = a - tmp - 1;
		for (int j = 0; j < size; j++)
			for (int k = j + 1; k < size; k++)
				if ((tmp[j] + tmp[k]) == c) {
					ostringstream ss;
					ss << "Case #" << (i + 1) << ": " << (j + 1) << " " << (k + 1) << '\n';
					outfile << ss.str(); 
					break;
				}
	}

	infile.close();
	outfile.close();
  return 0;
}
*/
