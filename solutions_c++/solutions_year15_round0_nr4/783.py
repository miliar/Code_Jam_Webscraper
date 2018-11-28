// CodeJam.cpp : 定義主控台應用程式的進入點。
//

#include "stdafx.h"
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <iostream>
#include <assert.h>
#include <unordered_map>
#include <algorithm>
#include <queue>

using namespace std;
typedef long long ll;

struct Shape {
	Shape(int X, int Y) : W(X), H(Y) { grid = new bool[W * H];  memset(grid, false, W * H); }
	~Shape() { delete[] grid;}
	void set(int x, int y, bool val) { assert(x < W && y < H); grid[x + y * H] = val; }
	bool get(int x, int y) { assert(x < W && y < H); return grid[x + y * H]; }

	bool *grid;
	int W, H;
};

bool solve(const int &X, const int &R, const int &C) {
	if (X == 1) return true;
	if (X >= 7) return false;

	if (R < X && C < X) return false;
	if (R % X != 0 && C % X != 0) return false;
	if (R < X - 1 || C < X - 1) return false;
	
	return true;

	//if (X == 3 && (R < 2 || C < 2)) return false;
	//if (X == 4 && (R < 3 || C < 3)) return false;

	/*
	if (X == 2) return R*C % 2 == 0;
	if (X == 3) {
		if (R == 1 || C == 1) return false;
		if (R*C % 3 != 0) return false;
		return true;
	}

	if (X == 4) return R > 2 && C > 2 && (R % 4 == 0 || C % 4 == 0);
	*/

	/*for (int i = 0; i < g.W; ++i) {
		for (int j = 0; j < g.H; ++j) {
			if (!g.get(i, j)) {
				g.fill()
			}
		}
	}*/

	return false;
}

int _tmain(int argc, _TCHAR* argv[])
{
	ifstream infile("D-small-attempt0.in");
	ofstream outfile("D-small-attempt0.out");

	//ifstream infile("test.txt");
	//ofstream outfile("test.out");

	string line;
	int numCase;
	getline(infile, line);
	istringstream iss(line);
	iss >> numCase;
	cout << "numCase: " << numCase << endl;

	int curCase = 0;
	while (getline(infile, line)) {
		int X, R, C;
		stringstream ss2(line);
		ss2 >> X >> R >> C;
		printf("X: %d, R: %d, C: %d\n", X, R, C);

		bool ans = 0;
		ans = solve(X, R, C);
		outfile << "Case #" << ++curCase << ": " << (ans ? "GABRIEL" : "RICHARD") << endl;
		//system("pause");

	}
	assert(curCase == numCase);
	infile.close();
	outfile.close();

	system("pause");
	return 0;
}

