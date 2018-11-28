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

	vector<vector <char> > op;
	op.resize(128);
	REP(i, 128)op[i].resize(128);
	op['u']['i'] = 'i';
	op['u']['j'] = 'j';
	op['u']['k'] = 'k';

	op['i']['i'] = 'U';
	op['i']['j'] = 'k';
	op['i']['k'] = 'J';

	op['j']['i'] = 'K';
	op['j']['j'] = 'U';
	op['j']['k'] = 'i';

	op['k']['i'] = 'j';
	op['k']['j'] = 'I';
	op['k']['k'] = 'U';

	op['U']['i'] = 'I';
	op['U']['j'] = 'J';
	op['U']['k'] = 'K';

	op['I']['i'] = 'u';
	op['I']['j'] = 'K';
	op['I']['k'] = 'j';

	op['J']['i'] = 'k';
	op['J']['j'] = 'u';
	op['J']['k'] = 'I';

	op['K']['i'] = 'J';
	op['K']['j'] = 'i';
	op['K']['k'] = 'u';

	REP(test, T){
		int res;
		string inp, str;
		int L, X;
		fin >> L >> X;
		fin >> inp;
		str = "";
		REP(q, X) str += inp;

		char cur = 'u';
		int lasti = str.size() + 1;
		int lastj = str.size();
		REP(i, str.size()){
			cur = op[cur][str[i]];
			if (cur == 'i') lasti = min(i, lasti);
			if (cur == 'k') lastj = i;
		}
		if (cur != 'U' || (lasti >= lastj)){
			fout << "Case #" << test +1 << ": NO\n";
		}
		else {
			fout << "Case #" << test +1<< ": YES\n";
		}
	}

	fin.close();
	fout.close();

	return 0;
}
