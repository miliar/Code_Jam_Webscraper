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

	ifstream fin("B-small-attempt0.in");
	ofstream fout("out.txt");
	fin >> T;
	REP(t, T){
		int ret = 0;
		string str;
		fin >> str;
		vector<bool> vec, cpy;
		vec.resize(str.length());
		cpy.resize(vec.size());
		REP(i, vec.size()) vec[i] = (str[i] == '+')?true:false;
		int lastMinus = vec.size() - 1;
		while (lastMinus >= 0){
			while ((lastMinus >= 0) && vec[lastMinus]) lastMinus--;
			if (lastMinus < 0) break;

			if (vec[0]){
				int firstMinus = 0;
				while (vec[firstMinus]) firstMinus++;
				cpy = vec;

				REP(i, firstMinus){
					vec[i] = !cpy[firstMinus - i - 1];
				}
				ret++;
			}
			
			cpy = vec;

			REP(i, lastMinus + 1){
				vec[i] = !cpy[lastMinus - i];
			}
			ret++;
		}

		fout << "Case #" << t + 1 << ": " << ret << endl;
	}
	return 0;
}
