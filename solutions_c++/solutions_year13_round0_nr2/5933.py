#include <iostream>
#include <fstream>
using namespace std;

ifstream fin ("input.in");
ofstream fout ("output.out");

int T, N, M;
int a[100][100];
bool row[100], col[100];
/*
void flood (int x, int y)
{
	if (vis[x][y]) return;
	if (done) return;
	if ((x == 0) || (x == N-1) || (y == 0) ||( y == M-1)) {
		done = true;
		return;
	}
	vis[x][y] = true;
	if (x > 0 && a[x-1][y] <= a[x][y])
		flood (x-1, y);
	if (x < N-1 && a[x+1][y] <= a[x][y])
		flood(x+1, y);
	if (y > 0 && a[x][y-1] <= a[x][y])
		flood (x,y-1);
	if (y < M-1 && a[x][y+1] <= a[x][y])
		flood(x,y+1);
}*/
int main()
{
	fin >> T;
	for (int c=1; c<=T; c++) {
		fin >> N >> M;
		for (int i=0; i<N; i++)
			for (int j=0; j<M; j++)
				fin >> a[i][j];
		for (int i=0; i<N; i++) row[i] = true;
		for (int j=0; j<M; j++) col[j] = true;
		for (int i=0; i<N; i++) {
			for (int j=0; j<M; j++)
				if (a[i][j] == 2) {
					row[i] = false;
					col[j] = false;
				}
		}
		bool good = true;
		for (int i=0; i<N; i++) {
			for (int j=0; j<M; j++)
				if (a[i][j] == 1) {
					if (!row[i] && !col[j]) {
						good = false;
					}
				}
		}
		if (good) fout << "Case #" << c << ": YES\n";
		else fout << "Case #" << c << ": NO\n";					  			
	}
}
