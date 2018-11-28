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

	ifstream fin("A-large.in");
	ofstream fout("out.txt");
	fin >> T;
	REP(t, T){
		int N;
		fin >> N;
		if (N == 0){
			fout << "Case #" << t + 1 << ": INSOMNIA\n";
		}
		else {
			int num = 0;
			vector<bool> seen;
			int totalSeen, tmp;
			seen.resize(10);
			REP(i, 10) seen[i] = false;
			totalSeen = 0;
			while (totalSeen < 10){
				num += N;
				tmp = num;
				while (tmp > 0){
					seen[tmp % 10] = true;
					tmp /= 10;
				}
				totalSeen = 0;
				REP(i, 10) if (seen[i]) totalSeen++;
			}

			fout << "Case #" << t + 1 << ": " << num << endl;
		}
	}
	return 0;
}