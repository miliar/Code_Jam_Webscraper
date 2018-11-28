#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <assert.h>
#include <unordered_map>
#include <limits.h>
#include <assert.h>
#include <string.h>
#include <Util.h>

using namespace std;

int N;
int px[1024];
int py[1024];
int pz[1024];
int vx[1024];
int vy[1024];
int vz[1024];
int speed;
double best[1024];

double distance(int i, int j) {
	int dx = px[i] - px[j];
	int dy = py[i] - py[j];
	int dz = pz[i] - pz[j];
	return sqrt(dx * dx + dy * dy + dz * dz);
}

double solve() {
	for (int i = 0; i < N; i++) {
		best[i] = distance(i, 0);
	}

	bool changed = true;
	while (changed) {
		changed = false;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (i == j) continue;
				double d = distance(i, j);
				double mj = max(best[j], d);
				if (best[i] > mj) {
					best[i] = mj;
					changed = true;
				}
			}
		}
	}
	return best[1];
}

int main(int argc, const char * argv[]) {

	istream &fin = cin;
	// fstream fin("tiny.in");

	int T;
	fin >> T;
	string s;
	for (int CASE = 1; CASE <= T; CASE++) {
		fin >> N;
		fin >> speed;
		for (int i = 0; i < N; i++) {
			fin >> px[i];
			fin >> py[i];
			fin >> pz[i];
			fin >> vx[i];
			fin >> vy[i];
			fin >> vz[i];
		}
		double result = solve();
		printf("Case #%d: %.8lf\n", CASE, result);
	}
    return 0;
}
