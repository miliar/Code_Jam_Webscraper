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
		int res;
		int smax;
		res = 0;

		fin >> smax;
		int cur = 0;
		REP(q, smax + 1){
			char digit;
			fin >> digit;
			cur += digit - '0';
			cur--;
			if (cur < 0) {
				res++;
				cur++;
			}
		}

		fout << "Case #" << test + 1 << ": " << res << endl;
	}
	fin.close();
	fout.close();

	system("pause");
	return 0;
}
