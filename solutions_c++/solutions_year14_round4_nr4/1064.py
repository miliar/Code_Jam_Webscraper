#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <iomanip>
#include <string>
#include <string.h>
#include <sstream>
#include <algorithm>
#include <time.h>
#include <set>
using namespace std;

int main() {
	int T;
	int N;
	int M;
	string s[10];
	int go[10];
	int times[165536];
	set<string> ss[5];

	cin >> T;

	for (int j = 1; j <= T; j++) {
		cin >> M >> N;

		for (int i = 0; i < M; ++i) {
			cin >> s[i];
			go[i] = 0;
		}

		int trytimes = (int) pow(N, M);
		for (int tt = 0; tt < trytimes; ++tt) {
			for (int i =0; i < N; ++i)
				ss[i].clear();

			for (int i =0; i < M; ++i) {
				//push
				for (int len = s[i].length(); len >= 0; --len)
					ss[go[i]].insert(s[i].substr(0, len));
			}

			times[tt] = 0;
			for (int i =0; i < N; ++i)
				times[tt] += ss[i].size();

			go[0] += 1;

			for (int i = 0; i < M; ++i)
				if (go[i] >= N) {
					go[i] = 0;
					go[i+1]++;
				}
				else
					break;
		}

		int max = 0;
		int maxcount = 0;
		for (int i = 0; i < trytimes; ++i)
			if (times[i] > max)
				max = times[i];

		for (int i = 0; i < trytimes; ++i)
			if (times[i] == max)
				maxcount++;

		cout << "Case #" << j << ": " << max << " " << maxcount << endl;
	}

	return 0;
}
