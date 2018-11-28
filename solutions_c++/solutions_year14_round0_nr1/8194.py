#include <iostream>
#include <math.h>
#include <sstream>
#include <vector>
#include <fstream>
#include <string>
#include <cstdlib>

using namespace std;

string Check(vector<int> one, vector<int> two) {
	int check = 0;
	stringstream ans;
	for (int i = 0; i < one.size(); ++i)
	{
		for (int j = 0; j < two.size(); ++j)
		{
			if(one[i] == two[j]) {
				check++;
				
				ans << one[i];
			}
		}
	}

	if(check == 1)	return ans.str();
	else if (check == 0) return "Volunteer cheated!";
	else if (check > 1) return "Bad magician!";
}

int main() {

	ifstream fin; fin.open("testinput.in");
	ofstream fout; fout.open("output.txt");

	int cases, rownumber, garbage;
	int casenumber = 1;

	fin >> cases;
	while (!fin.eof()) {
		if(casenumber > cases) break;
		fout << "Case #" << casenumber++ << ": ";

		fin >> rownumber;
		std::vector<int> row1;
		for (int i = 0; i < 16; ++i)
		{
			fin >> garbage;
			if( (i/4) + 1 == rownumber) row1.push_back(garbage);
		}

		fin >> rownumber;
		std::vector<int> row2;
		for (int i = 0; i < 16; ++i)
		{
			fin >> garbage;
			if( (i/4) + 1 == rownumber) row2.push_back(garbage);
		}

		fout << Check(row1,row2) << endl;
	}
	fin.close();
	fout.close();


}
