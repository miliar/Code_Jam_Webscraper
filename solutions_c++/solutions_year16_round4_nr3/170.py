#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <assert.h>
#include <unordered_map>

using namespace std;

int R, C;

char m[101][101];
int love[10201];
int ring[10201];
int N;

enum Dir {
	North, East, South, West
};

const char *name(Dir dir) {
	switch (dir) {
		case North: return "N";
		case East: return "E";
		case South: return "S";
		case West: return "W";
		default: return "?";
	}
}

bool route(int from, int to) {
	int rf, cf;
	Dir dirf;
	int rt, ct;
	Dir dirt;
	if (from < C) {  // north;
		rf = 0;
		cf = from;
		dirf = North;
	} else if (from < R + C) {  // east;
		rf = from - C;
		cf = C - 1;
		dirf = East;
	} else if (from < R + C + C) {  // south;
		rf = R - 1;
		cf = (C - 1) - (from - R - C);
		dirf = South;
	} else {
		rf = (R - 1) - (from - R - C - C);
		cf = 0;
		dirf = West;
	}
	if (to < C) {  // north;
		rt = 0;
		ct = to;
		dirt = North;
	} else if (to < R + C) {  // east;
		rt = to - C;
		ct = C - 1;
		dirt = East;
	} else if (to < R + C + C) {  // south;
		rt = R - 1;
		ct = (C - 1) - (to - R - C);
		dirt = South;
	} else {
		rt = (R - 1) - (to - R - C - C);
		ct = 0;
		dirt = West;
	}

	// printf("route: %d(%d,%d,%s) --> %d(%d,%d,%s)\n", from + 1,
	//	rf, cf, name(dirf), to + 1, rt, ct, name(dirt));

	while (true) {
		char h = m[rf][cf];
		Dir nextDirf;
		if (h == ' ') {  // right turn, whether possible;
			switch (dirf) {
				case North: m[rf][cf] = '/'; break;
				case East: m[rf][cf] = '\\'; break;
				case South: m[rf][cf] = '/'; break;
				case West: m[rf][cf] = '\\'; break;
			}
		}
		h = m[rf][cf];
		if (h == '/') {
			switch (dirf) {
				case North: nextDirf = West; break;
				case East: nextDirf = South; break;
				case South: nextDirf = East; break;
				case West: nextDirf = North; break;
				default: return false;
			}
		} else if (h == '\\') {
			switch (dirf) {
				case North: nextDirf = East; break;
				case East: nextDirf = North; break;
				case South: nextDirf = West; break;
				case West: nextDirf = South; break;
				default: return false;
			}
		}
		dirf = nextDirf;

		if (dirf == dirt && rf == rt && cf == ct) {
			return true;  // successful;
		}
		switch (dirf) {
			case North: rf--; dirf = South; break;
			case East: cf++; dirf = West; break;
			case South: rf++; dirf = North; break;
			case West: cf--; dirf = East; break;
		}
		if (rf >= R || rf < 0 || cf >= C || cf < 0)
			return false;
	}
}

bool solve0(int CASE) {
	for (int r = 0; r < R; r++) {
		for (int c = 0; c < C; c++) {
			m[r][c] = ' ';
		}
		m[r][C] = '\n';
	}
	int n = N;
	while (n > 0) {
		bool found = false;
	//	printf("ring: ");
	//	for (int i = 0; i < n; i++) {
	//		printf("%d,", ring[i]);
	//	}
	//	printf("\n");
		for (int i = 0; i < n; i++) {
			int a = ring[i];
			int b = ring[(i + 1) % n];
			if (love[a] == b) {
				assert(love[b] == a);
				if (!route(b, a)) return false;
				found = true;
				if (b == 0) {
					for (int j = 1; j < n - 1; j++) {
						ring[j - 1] = ring[j];
					}
				} else {
					for (int j = i + 2; j < n; j++) {
						ring[j - 2] = ring[j];
					}
				}
				n -= 2;
			}
			if (found) break;
		}
		if (!found) return false;
	}
	for (int r = 0; r < R; r++) {
		for (int c = 0; c < C; c++) {
			if (m[r][c] == ' ') m[r][c] = '/';
		}
	}
	return true;	
}

void solve(int CASE) {
	printf("Case #%d:\n", CASE);
	if (solve0(CASE)) {
		for (int r = 0; r < R; r++) {
			for (int c = 0; c < C; c++) {
				printf("%c", m[r][c]);
			}
			printf("\n");
		}
	} else {
		printf("IMPOSSIBLE\n");
	}
}

int main(int argc, const char * argv[]) {

	istream &fin = cin;
	// fstream fin("tiny.in");

	int T;
	fin >> T;
	for (int CASE = 1; CASE <= T; CASE++) {
		fin >> R;
		fin >> C;
		N = 2 * (R + C);
		for (int i = 0; i < N; i += 2) {
			int a, b;
			fin >> a;
			fin >> b;
			a--;
			b--;
			love[a] = b;
			love[b] = a;
		}
		for (int i = 0; i < N; i++) ring[i] = i;
		solve(CASE);
	}
    return 0;
}
