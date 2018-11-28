#include <fstream>
#include <iostream>
#include <sstream>
#include <set>
#include <limits.h>
#include <map>

using namespace std;

int T, N, M;

int maxx(int& a, int& b) {
	if(a < b) return b;
	return a;
}

int main() {
	ofstream fout("fence.out");
	ifstream fin("fence.in");
	fin >> T;
	for(int t = 0; t < T; t++) {
		fin >> N >> M;
		int goal[N][M];
		int cur[N][M];
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				fin >> goal[i][j];
				cur[i][j] = 100;
			}
		}
		bool changed = true;
		bool done = false;
		while(changed) {
			changed = false;
			done = true;
			for(int i = 0; i < N; i++) {
				for(int j = 0; j < M; j++) {
					if(cur[i][j]!=goal[i][j])
						done = false;
				}
			}
			if(done) break;
			done = false;
			// Go row by row
			for(int i = 0; i < N; i++) {
				int curMax = 0;
				int goalMax = 0;
				for(int j = 0; j < M; j++) {
					curMax = maxx(cur[i][j], curMax);
					goalMax = maxx(goal[i][j], goalMax);
				}
				if(curMax > goalMax) {
					// cut it
					for(int j = 0; j < M; j++) {
						cur[i][j] = goalMax;
					}
					changed = true;
				}
			}
			// Now go col by col
			for(int j = 0; j < M; j++) {
				int curMax = 0;
				int goalMax = 0;
				for(int i = 0; i < N; i++) {
					curMax = maxx(cur[i][j], curMax);
					goalMax = maxx(goal[i][j], goalMax);
				}
				if(curMax > goalMax) {
					// cut it
					for(int i = 0; i < N; i++) {
						cur[i][j] = goalMax;
					}
					changed = true;
				}
			}
		}
		if(done) {
			fout << "Case #" << t+1 << ": YES\n";
		} else {
			fout << "Case #" << t+1 << ": NO\n";
		}
	}
}
