#include <iostream>
#include <fstream>

using namespace std;

void printLawn(int n, int m, int* heights) {

	cout << "\n";

	for(int y = 0; y < n; ++y) {
		for(int x = 0; x < m; ++x) {
			cout << heights[x + y*m] << " ";
		}

		cout << "\n";
	}
	cout << "\n";
}

int maxRow(int n, int m, int row, int* heights) {
	int maxI = 0;

	for(int x = 0; x < m; ++x)
		if(heights[x + m*row] > maxI)
			maxI = heights[x + m*row];

	return maxI;
}

int maxColumn(int n, int m, int col, int *heights) {
	int maxI = 0;

	for(int y = 0; y < n; ++y)
		if(heights[col + m*y] > maxI)
			maxI = heights[col + m*y];

	return maxI;
}

void cutRow(int n, int m, int row, int level, int *heights) {
	for(int x = 0; x < m; ++x)
		if(heights[x + m*row] > level)
			heights[x + m*row] = level;	
}

void cutColumn(int n, int m, int col, int level, int *heights) {
	for(int y = 0; y < n; ++y)
		if(heights[col + m*y] > level)
			heights[col + m*y] = level;
}

bool matchLawn(int n, int m, int *lawn1, int *lawn2) {
	for(int i = 0; i < n * m; ++i)
		if(lawn1[i] != lawn2[i])
			return false;

	return true;
}

int main(int argc, char **argv) {
	fstream inFile(argv[1]);
	fstream outFile("lawn.out", fstream::trunc | fstream::out);

	int lawns; inFile >> lawns;
	cout << "Number of lawns: " << lawns << endl;

	// Remove later
	// lawns = 1;

	for(int i = 0; i < lawns; i++) {
		int n, m;
		inFile >> n;
		inFile >> m;
		cout << "Lawn: " << i + 1 << ", n = " << n << ", m = " << m << endl;

		int *wantedHeight = new int(n*m);
		int *uncutLawn = new int(n*m);
		for(int j = 0; j < n*m; ++j)
			uncutLawn[j] = 100;

		for(int y = 0; y < n; ++y)
			for(int x = 0; x < m; ++x) {
				int height;
				inFile >> height;
				wantedHeight[x + y*m] = height;
			}

		printLawn(n,m,wantedHeight);

		for(int row = 0; row < n; ++row)
			cutRow(n,m,row,maxRow(n,m,row,wantedHeight),uncutLawn);
		for(int col = 0; col < m; ++col)
			cutColumn(n,m,col,maxColumn(n,m,col,wantedHeight),uncutLawn);

		outFile << "Case #" << i + 1 << ": ";

		if(matchLawn(n,m,wantedHeight,uncutLawn))
			outFile << "YES\n";
		else
			outFile << "NO\n";

		delete wantedHeight, uncutLawn;
	}

	inFile.close();
	outFile.close();
	
}