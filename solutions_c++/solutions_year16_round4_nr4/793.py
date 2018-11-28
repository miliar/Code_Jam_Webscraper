#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cassert>
#include <iomanip>
using namespace std;

using ll = long long int;
ifstream fin("1.in");
ofstream fout("1.out");

int N, adjOrig[4][4], adj[4][4]; // Worker i knows machine j

bool possible(int w, int occ, int gone) {
	bool ret = true;
	bool found = false;
	for (int mac = 0; mac < N; mac++) {
		if (adj[w][mac] && !((1 << mac) & occ)) {
			found = true;
			for (int next = 0; next < N; next++) {
				if(!(gone & (1<<next)))
					ret &= possible(next, occ | (1 << mac), gone | (1<<next));
			}
		}
	}
	if (!found)
		return false;
	return ret;
}

int main() {
	int T;
	fin >> T;
	for (int t = 1; t <= T; t++) {
		fout << "Case #" << t << ": ";
		fin >> N;
		int best = 1000;
		for (int i = 0; i < N; i++){
			for (int j = 0; j < N; j++) {
				char c;
				fin >> c;
				adjOrig[i][j] = c == '1';
			}
		}
		for (int i = 0; i < (1 << N*N); i++) {
			int size = 0;
			for (int j = 0; j < N*N; j++) {
				int x = j / N;
				int y = j % N;
				adj[x][y] = adjOrig[x][y];
				if ((1 << j) & i) {
					adj[x][y] = true;
					size++;
				}
			}
			if (size < best) {
				bool good = true;
				for (int i = 0; i < N; i++)
					good &= possible(i, 0, 1<<i);
				if(good)
					best = size;
			}
		}
		fout << best << endl;
	}
}
