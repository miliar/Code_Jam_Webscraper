#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

const string input = "a.in",
			 output = "a.out";

int main()
{
	int T;
	ifstream fin(input.c_str());
	ofstream fout(output.c_str());
	fin >> T;
	for (int time = 0; time < T; ++time) {
		int row;
		int a[4], b[4], tmp;
		fin >> row;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j)
				if (i == row - 1) fin >> a[j]; else fin >> tmp;
		}
		fin >> row;
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j)
				if (i == row - 1) fin >> b[j]; else fin >> tmp;
		}
		vector<int> ans(0);
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				if (a[i] == b[j])
					ans.push_back(a[i]);
		fout << "Case #" << time + 1 << ": ";
		if (ans.size() == 0) fout << "Volunteer cheated!\n";
		else {
			if (ans.size() == 1) fout << ans[0] << endl;
			else fout << "Bad magician!\n";
		}
	}
	return 0;
}