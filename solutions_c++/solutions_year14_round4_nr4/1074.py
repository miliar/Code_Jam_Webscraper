// ================================================================================================
//  Written by Luis Garcia, 2014
// ================================================================================================

#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <string>
#include <iterator>
#include <numeric>
#include <iostream>

using namespace std;

#if defined _OJ_PROJECT
_BEGIN_PROBLEM(_GCJ14_05D, "GCJ14 05D")
#endif // _OJ_PROJECT

#define infinite_loop for (;;)

int main(
	) {
		int T, N, M;
		cin >> T;

		for (int _T = 1; _T <= T; ++_T) {
			cin >> M >> N;

			int cases = 1;
			for (int i = 0; i < M; ++i) cases *= N;

			char words[8][20];
			for (int i = 0; i < M; ++i) scanf("%s", words[i]);

			int worst = 0, worstTimes = 0;

			for (int j = 0; j < cases; ++j) {
				int servers[4][8] = {}, serversCount[4] = {};
				for (int i = 0, p = j; i < M; ++i, p /= N)
					servers[p % N][serversCount[p % N]++] = i;

				if (find(serversCount, serversCount + N, 0) != serversCount + N) continue;

				int total = 0;
				for (int i = 0; i < N; ++i) {
					set<string> nodes;
					for (int k = 0; k < serversCount[i]; ++k) {
						char * word = words[servers[i][k]];
						for (int h = 0; h <= strlen(word); ++h)
							nodes.insert(string(word, word + h));
					}
					total += nodes.size();
				}
				if (total > worst)
					worst = total, worstTimes = 1;
				else if (total == worst)
					++worstTimes;
			}

			cout << "Case #" << _T << ": " << worst << " " << worstTimes << endl;
		}

		return 0;
	}

#if defined _OJ_PROJECT
_END_PROBLEM
#endif // _OJ_PROJECT

// ================================================================================================
//  End of file.
// ================================================================================================
