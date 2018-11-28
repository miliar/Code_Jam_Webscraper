#include <iostream>
#include "stdio.h"

using namespace std;

int main() {
	int t;
	cin >> t;

	int r,c;
	char d[128][128];

	for (int tcount = 1; tcount <= t; ++tcount) {
		cin >> r >> c;

		for (int i = 0; i < r; ++i)
			for (int j = 0; j < c; ++j)
				cin >> d[i][j];

		int count = 0;

		for (int i = 0; i < r; ++i)
			for (int j = 0; j < c; ++j) {
				if (d[i][j] == '.')
					continue;

				int di, dj;

				if (d[i][j] == '<') {
					di = 0;
					dj = -1;
				}
				else if (d[i][j] == '>') {
					di = 0;
					dj = 1;
				}
				else if (d[i][j] == '^') {
					di = -1;
					dj = 0;
				}
				else if (d[i][j] == 'v') {
					di = 1;
					dj = 0;
				}

				int it = i;
				int jt = j;

				while (true){
					it += di;
					jt += dj;
					if (!(it >= 0 && it < r && jt >= 0 && jt < c))
						break;
					if (d[it][jt] != '.')
						break;
				}

				if (it >= 0 && it < r && jt >= 0 && jt < c)
					continue; //safe

				int tpcount = 0;

				it = 0; jt = j;
				while (it >= 0 && it < r && jt >= 0 && jt < c){
					
					if (d[it][jt] != '.')
						++ tpcount;
					it ++;
				}
				it = i; jt = 0;
				while (it >= 0 && it < r && jt >= 0 && jt < c){
					
					if (d[it][jt] != '.')
						++ tpcount;
					jt ++;
				}

				if (tpcount <= 2) {
					goto fail;
					break;
				}
				else
					++count;
			}

		cout << "Case #" << tcount << ": " << count << endl;
		continue;
fail:
		cout << "Case #" << tcount << ": IMPOSSIBLE" << endl;
	}

	return 0;
}