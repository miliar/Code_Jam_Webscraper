#include <iostream>
#include <fstream>
#include <iomanip>
#include <algorithm> 
#include <vector>
using namespace std;

ifstream input;
ofstream output;

bool solution(int i, int j, vector<vector<char> > &field, int toOpen)
{
	int R = field.size();
	int C = field[0].size();
	
	
	if (toOpen == 0) {
		//output << "be Called Print (" << i << ", " << j << ", " << toOpen << ")" << endl;																		
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				output << field[r][c];
			}
			if (r != R-1)
				output << endl;
		}
		return true;
	}

	int left_up = 0, up = 0, right_up = 0, left = 0, right = 0, left_down = 0, down = 0, right_down = 0;
	if (i - 1 >= 0 && j - 1 >= 0 && field[i-1][j-1] == '*') {
		left_up = 1;
	}
	if (i - 1 >= 0 && field[i-1][j] == '*') {
		up = 1;
	}
	if (i - 1 >= 0 && j + 1 < C && field[i-1][j+1] == '*') {
		right_up = 1;
	}
	if (j - 1 >= 0 && field[i][j-1] == '*') {
		left = 1;
	}
	if (j + 1 < C && field[i][j+1] == '*') {
		right = 1;
	}
	if (i + 1 < R && j - 1 >= 0 && field[i+1][j-1] == '*') {
		left_down = 1;
	}
	if (i + 1 < R && field[i+1][j] == '*') {
		down = 1;
	}
	if (i + 1 < R && j + 1 < C && field[i+1][j+1] == '*') {
		right_down = 1;
	}
	int open = left_up + up + right_up + left + right + left_down + down + right_down;

	if (toOpen - open >= 0) {
		if (left_up)
			field[i-1][j-1] = '.';
		if (up)
			field[i-1][j] = '.';
		if (right_up)
			field[i-1][j+1] = '.';
		if (left)
			field[i][j-1] = '.';
		if (right)
			field[i][j+1] = '.';
		if (left_down)
			field[i+1][j-1] = '.';
		if (down)
			field[i+1][j] = '.';
		if (right_down)
			field[i+1][j+1] = '.';
				
		if (left_up) {
//output << "left_up (" << i-1 << ", " << j-1 << ", " << toOpen-open << ")" << endl;		
			if (solution(i-1, j-1, field, toOpen-open))
				return true;
		}
		if (up) {
//output << "up (" << i-1 << ", " << j << ", " << toOpen-open << ")" << endl;	
			if (solution(i-1, j, field, toOpen-open))
				return true;
		}
		if (right_up) {
//output << "right_up (" << i-1 << ", " << j+1 << ", " << toOpen-open << ")" << endl;
			if (solution(i-1, j+1, field, toOpen-open))
				return true;
		}
		if (left) {
//output << "left (" << i << ", " << j-1 << ", " << toOpen-open << ")" << endl;
			if (solution(i, j-1, field, toOpen-open))
				return true;
		}
		if (right) {
//output << "right (" << i << ", " << j+1 << ", " << toOpen-open << ")" << endl;
			if (solution(i, j+1, field, toOpen-open))
				return true;
		}
		if (left_down) {
//output << "left_down (" << i+1 << ", " << j-1 << ", " << toOpen-open << ")" << endl;
			if (solution(i+1, j-1, field, toOpen-open))
				return true;
		}
		if (down) {
//output << "down (" << i+1 << ", " << j << ", " << toOpen-open << ")" << endl;
			if (solution(i+1, j, field, toOpen-open))
				return true;
		}
		if (right_down) {
//output << "right_down (" << i+1 << ", " << j+1 << ", " << toOpen-open << ")" << endl;
			if (solution(i+1, j+1, field, toOpen-open))
				return true;
		}
		
		if (left_up) {
			field[i-1][j-1] = '*';
		}
		if (up) {
			field[i-1][j] = '*';
		}
		if (right_up) {
			field[i-1][j+1] = '*';
		}
		if (left) {
			field[i][j-1] = '*';
		}
		if (right) {
			field[i][j+1] = '*';
		}
		if (left_down) {
			field[i+1][j-1] = '*';
		}
		if (down) {
			field[i+1][j] = '*';
		}
		if (right_down) {
			field[i+1][j+1] = '*';
		}
	}
	
	return false;
}

int main(int argc, char* argv[])
{
	input.open(argv[1]);
	output.open("output.out");

	int T;
	input >> T;

	for (int c = 1; c <= T; c++) {
		int R, C, M;
		input >> R >> C >> M; 

		output << "Case #" << c << ": " << endl;

		vector<vector<char> >field(R, vector<char>(C, '*'));
		
		bool possible = false;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				field[i][j] = 'c'; //click on this one
				if (possible = solution(i, j, field, R*C - M - 1)) {
					//cout << "hit go to" << endl;
					goto outside;
				}

				field[i][j] = '*';
			}
		}
outside:
		if (!possible)
			output << "Impossible";
		if (c != T) {
			output << endl;
		}
	}
	
	input.close();
	output.close();
}
