#include <iostream>
#include <fstream>

using namespace std;

int res[4][4][4] = {
	{
		{0, 0, 0, 0},
		{0, 0, 0, 0},
		{0, 0, 0, 0},
		{0, 0, 0, 0}
	},
	{
		{1, 0, 1, 0},
		{0, 0, 0, 0},
		{1, 0, 1, 0},
		{0, 0, 0, 0}
	},
	{
		{1, 1, 1, 1},
		{1, 1, 0, 1},
		{1, 0, 0, 0},
		{1, 1, 0, 1}
	},
	{
		{1, 1, 1, 1},
		{1, 1, 1, 1},
		{1, 1, 1, 0},
		{1, 1, 0, 0}
	}
};

int main() {
	ifstream fin("D-small-attempt1.in");
	ofstream fout("output.out");
	int t;
	fin >> t;
	for (int i = 1; i <= t; i++) {
		int x, r, c;
		fin >> x >> r >> c;
		fout << "Case #" << i << ": " << (res[x - 1][r - 1][c - 1] ? "RICHARD" : "GABRIEL") << endl;
	}
	return 0;
}