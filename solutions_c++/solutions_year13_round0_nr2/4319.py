#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		int N, M;
		fin >> N >> M;
		short lawn[100][100];
		for (int r = 0; r < N; r++)
			for (int c = 0; c < M; c++)
				fin >> lawn[r][c];
		short maxR[100] = {0}, maxC[100] = {0};
		for (int r = 0; r < N; r++)
			for (int c = 0; c < M; c++)
				if (lawn[r][c] > maxR[r]) maxR[r] = lawn[r][c];
		for (int c = 0; c < M; c++)
			for (int r = 0; r < N; r++)
				if (lawn[r][c] > maxC[c]) maxC[c] = lawn[r][c];
		bool flag = true;
		for (int r = 0; r < N && flag; r++)
			for (int c = 0; c < M && flag; c++)
				if (lawn[r][c] < maxR[r] && lawn[r][c] < maxC[c]) flag = false;
		fout << "Case #" << t << ": " << (flag?"YES":"NO") << endl;
	}
}