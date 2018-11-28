#include <cstdio>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <iterator>

using namespace std;

int main(int argc, char* argv[])
{
	ifstream f;
	f.open("A-small-attempt1.in");
	if (!f.is_open()) {
		cerr << "Could not open file.\n";
		return -1;
	}

	ofstream out;
	out.open("output_small.txt");
	if (!out.is_open()) {
		cerr << "Could not open output file.\n";
		return -1;
	}

	int n;
	f >> n;

	for(int k = 1; k <= n; ++k) {
		int guess1, guess2;
		vector<int> arrange1, arrange2;
		
		f >> guess1;
		f.ignore(256, '\n');

		for (int i = 1; i <= 4; ++i) {
			if (guess1 == i) {
				for (int j = 0; j < 4; ++j) {
					int c;
					f >> c;
					arrange1.push_back(c);
				}
				f.ignore(256, '\n');
			} else {
				f.ignore(256, '\n');
			}
		}

		f >> guess2;
		f.ignore(256, '\n');

		for (int i = 1; i <= 4; ++i) {
			if (guess2 == i) {
				for (int j = 0; j < 4; ++j) {
					int c;
					f >> c;
					arrange2.push_back(c);
				}
				f.ignore(256, '\n');
			} else {
				f.ignore(256, '\n');
			}
		}

		vector<int> intersection;

		sort(arrange1.begin(), arrange1.end());
		sort(arrange2.begin(), arrange2.end());
		set_intersection(arrange1.begin(), arrange1.end(), arrange2.begin(), arrange2.end(), 
			back_inserter(intersection));

		out << "Case #";
		out << k;
		out << ": ";

		switch(intersection.size()) {
		case 0: 
			out << "Volunteer cheated!" << endl;
			break;
		case 1:
			out << intersection[0] << endl;
			break;
		default:
			out << "Bad magician!" << endl;
		}
	}

	f.close();
	out.flush();
	out.close();
}