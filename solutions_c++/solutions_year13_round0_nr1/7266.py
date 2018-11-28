#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream fin ("input.in");
ofstream fout ("output.out");

int T;
string grid[4];

char checkwinner() {
	int xcnt=0, ocnt=0, tcnt=0;
	for (int i=0; i<4; i++) {
		xcnt = 0; ocnt = 0; tcnt = 0;
		for (int j=0; j<4; j++) {
			if (grid[i][j] == 'X')
				xcnt++;
			else if (grid[i][j] == 'O')
				ocnt++;
			else if (grid[i][j] == 'T')
				tcnt++;
		}
		if (xcnt == 4 || (xcnt == 3 && tcnt == 1))
			return 'X';
		if (ocnt == 4 || (ocnt == 3 && tcnt == 1))
			return 'O';
	}
	for (int i=0; i<4; i++) {
		xcnt = 0; ocnt = 0; tcnt = 0;
		for (int j=0; j<4; j++) {
			if (grid[j][i] == 'X')
				xcnt++;
			else if (grid[j][i] == 'O')
				ocnt++;
			else if (grid[j][i] == 'T')
				tcnt++;
		}
		if (xcnt == 4 || (xcnt == 3 && tcnt == 1))
			return 'X';
		if (ocnt == 4 || (ocnt == 3 && tcnt == 1))
			return 'O';
	}
	xcnt = 0; ocnt = 0; tcnt = 0;
	for (int i=0; i<4; i++) {
		if (grid[i][i] == 'X')
			xcnt++;
		else if (grid[i][i] == 'O')
			ocnt++;
		else if (grid[i][i] == 'T')
			tcnt++;
	}
	if (xcnt == 4 || (xcnt == 3 && tcnt == 1))
		return 'X';
	if (ocnt == 4 || (ocnt == 3 && tcnt == 1))
		return 'O';
	xcnt = 0; ocnt = 0; tcnt = 0;
	for (int i=0; i<4; i++) {
		if (grid[i][3-i] == 'X')
			xcnt++;
		else if (grid[i][3-i] == 'O')
			ocnt++;
		else if (grid[i][3-i] == 'T')
			tcnt++;
	}
	if (xcnt == 4 || (xcnt == 3 && tcnt == 1))
		return 'X';
	if (ocnt == 4 || (ocnt == 3 && tcnt == 1))
		return 'O';
	for (int i=0; i<4; i++) for (int j=0; j<4; j++) if (grid[i][j] == '.') return 'N';
	return 'D';
}
int main()
{
	fin >> T;
	for (int i=0; i<T; i++) {
		for (int j=0; j<4; j++)
			fin >> grid[j];
		char ans = checkwinner();
		if (ans == 'N')
			fout << "Case #" << i+1 << ": Game has not completed\n";
		else if (ans == 'D')
			fout << "Case #" << i+1 << ": Draw\n";
		else
			fout << "Case #" << i+1 << ": " << ans << " won\n";
		//		fin >> grid[0];	
	}
}
