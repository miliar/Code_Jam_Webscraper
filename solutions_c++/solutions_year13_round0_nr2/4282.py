#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

bool ok(const vector<vector<int> >& lawn);

int main(int argc, char* argv[])
{
	ifstream in("in.txt");
	int t, r, c;
	in >> t;
	ofstream out("out.txt");
	for (int i = 0; i < t; ++i) {
		in >> r >> c;
		vector<vector<int> > lawn(r,c);
		for (int j=0; j < r; j++)
			for (int k=0; k < c; ++k)
				in >> lawn[j][k];
		out << "Case #" << i+1 << ": " << (ok(lawn) ? "YES" : "NO") << endl;
	}
}

bool ok(const vector<vector<int> >& lawn) {
	vector<int> indexOneMaxes(lawn.size(), 0);
	vector<int> indexTwoMaxes(lawn[0].size(), 0);
	for (size_t i=0; i <indexOneMaxes.size(); i++) {
		for (size_t j=0; j < lawn[i].size(); j++) {
			if (lawn[i][j] > indexOneMaxes[i]) indexOneMaxes[i] = lawn[i][j]; 
		}
	}
	for (size_t i=0; i <indexTwoMaxes.size(); i++) {
		for (size_t j=0; j < lawn.size(); j++) {
			if (lawn[j][i] > indexTwoMaxes[i]) indexTwoMaxes[i] = lawn[j][i]; 
		}
	}
	for (size_t i=0; i < lawn.size(); i++)
		for (size_t j=0; j < lawn[0].size(); j++)
			if (lawn[i][j] < indexOneMaxes[i] && lawn[i][j] < indexTwoMaxes[j])
				return false;
	return true;
}