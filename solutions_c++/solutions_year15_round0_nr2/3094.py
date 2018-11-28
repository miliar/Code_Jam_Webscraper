#include <iostream>
#include <fstream>
#include <stdio.h>
#include <algorithm>
#include <functional>
#include <queue>
#include <math.h>

using namespace std;

ifstream fin ("B-large.in");
ofstream fout ("B-large.out");

int T, D;
int pancakes[1000];

int main() {
	fin >> T;

	for (int t = 1; t <= T; ++t) {
		fin >> D;
		priority_queue<int, vector<int>, less<int> > pq;
		for (int i = 0; i < D; ++i)
			fin >> pancakes[i];
		sort(pancakes, pancakes + D, greater<int>());
		int mintime = pancakes[0];

		for (int dinnertime = 1; dinnertime <= mintime; ++dinnertime) {
			int special_time = 0;
			for (int i = 0; i < D && pancakes[i] > dinnertime; ++i)
				if (pancakes[i] % dinnertime == 0)
					special_time += pancakes[i] / dinnertime - 1;
				else
					special_time += pancakes[i] / dinnertime;
//			printf("dinnertime: %d, special_time: %d\n", dinnertime, special_time);
			mintime = min(mintime, special_time + dinnertime);
		}
		fout << "Case #" << t << ": " << mintime << endl;
	}
	return 0;
}
