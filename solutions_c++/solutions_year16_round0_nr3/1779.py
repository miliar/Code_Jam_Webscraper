#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i, a, b) for (int i(a), _b(b); i <= _b; ++i)
#define REP(i, n) for (int i(0), _n(n); i < _n; ++i)

int main(void){
	int T = 1;

	//ifstream fin("1.txt");
	ofstream fout("out.txt");
	//fin >> T;
	int N = 32;
	int J = 500;
	REP(t, T){
		fout << "Case #1:\n";

		vector<int> out;
		out.resize(N);
		int pos, x, y;
		REP(j, J){
			REP(i, N) out[i] = 0;
			out[0] = 1;
			out[N - 1] = 1;
			pos = j % ((N / 2 - 1) * (N / 2 - 2) / 2);
			x = 0; y = 0;
			while (y * (y + 1) / 2 <= pos) y++;
			y--;
			x = pos - (y * (y + 1) / 2);
			y++;
			out[2 + 2 * x] = 1;
			out[2 + 2 * y] = 1;

			pos = j / ((N / 2 - 1) * (N / 2 - 2) / 2);
			x = 0; y = 0;
			while (y * (y + 1) / 2 <= pos) y++;
			y--;
			x = pos - (y * (y + 1) / 2);
			y++;
			out[2 * x + 1] = 1;
			out[2 * y + 1] = 1;

			REP(i, N) fout << out[i];
			fout << " 3 2 3 2 7 2 3 2 3\n";

			/*
			long long toDiv[] = { 0, 0, 3, 2, 3, 2, 7, 2, 3, 2, 3 };
			long long number, base;
			FOR(b, 2, 10){
				number = 0;
				base = 1;
				for (int i = N - 1; i >= 0; i--){
					number += base * out[i];
					base *= b;
				}
				fout << b << ": " << number << endl;
				if (number % toDiv[b] != 0) {
					fout << "--------- fails to div " << toDiv[b] << endl;
					system("pause");
				}
			}
			*/
		}
	}

	
	return 0;
}