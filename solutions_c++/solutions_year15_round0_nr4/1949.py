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
	int T;
	ofstream fout = ofstream("out.txt");
	ifstream fin = ifstream("in.txt");

	fin >> T;

	REP(test, T){
		int x, r, c;
		fin >> x >> r >> c;
		if ((r * c) % x != 0){
			fout << "Case #" << test + 1 << ": RICHARD\n";
			continue;
		}
		if (x == 1) {
			fout << "Case #" << test +1 << ": GABRIEL\n";
			continue;
		}
		if (x == 2) {
			fout << "Case #" << test + 1 << ": GABRIEL\n";
			continue;
		}
		if (x == 3){
			if (r*c == 3){
				fout << "Case #" << test + 1 << ": RICHARD\n";
				continue;
			}
			fout << "Case #" << test + 1 << ": GABRIEL\n";
			continue;
		}
		if (x == 4) {
			if (r*c == 4){
				fout << "Case #" << test + 1 << ": RICHARD\n";
				continue;
			}
			if (r*c == 8){
				fout << "Case #" << test + 1 << ": RICHARD\n";
				continue;
			}
			fout << "Case #" << test + 1 << ": GABRIEL\n";
			continue;
		}
		
	}

	fin.close();
	fout.close();

	return 0;
}
