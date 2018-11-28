#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <queue>
#include <set>
#include <map>

using namespace std;

#define ll long long
#define pii pair<int,int>

ofstream fout ("QB.out");
ifstream fin ("QB.in");

int main() {
int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Working on Case #" << t << endl;
		int N,M;
		fin >> N >> M;
		int grid[100][100];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				fin >> grid[i][j];
			}
		}
		int rmax[100];
		int cmax[100];
		for (int i = 0; i < N; i++) {
			rmax[i] = 0;
			for (int j = 0; j < M; j++) rmax[i] = max(rmax[i],grid[i][j]);
		}
		for (int j = 0; j < M; j++) {
			cmax[j] = 0;
			for (int i = 0; i < N; i++) cmax[j] = max(cmax[j],grid[i][j]);
		}
		bool ans = true;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (grid[i][j] != cmax[j] && grid[i][j] != rmax[i]) ans = false;
			}
		}
		fout << "Case #" << t << ": " << (ans?"YES":"NO") << endl;
	}
    return 0;
}