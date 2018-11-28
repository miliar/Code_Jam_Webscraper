/*
 * new
 *      Author: AbdullaAshraf
 */
#include<bits/stdc++.h>
using namespace std;
const int OO = 1000000000;
const int maxn = 1e5 + 5;

typedef long long ll;
#define REP(i,n) for(int(i)=0; (i)<(n); (i)++)

ofstream sout ("output.txt");

int n, j, c = 0;
vector<int> di;

int getd(ll x) {
	int l = sqrt(x);
	for (int i = 2; i <= l; i++) {
		if (x % i == 0)
			return i;
	}
	return 0;
}

void generate(int i, string g) {
	if (c == j)
		return;
	if (i == n - 1) {
		g += '1';
		di.clear();
		for (int a = 2; a < 11; a++) {
			ll s = 0;
			REP(b,g.length())
				s += (g[b] - '0') * pow(a, g.length() - b -1);
			int x = getd(s);
			if (x == 0)
				return;
			di.push_back(x);
		}
		c++;
		sout << g;
		for (auto it : di)
			sout << " " << it;
		if (c == j)
			return;
		sout << endl;
		return;
	}
	generate(i + 1, g + '0');
	generate(i + 1, g + '1');
}

int main(void) {
	ifstream sin ("C-small-attempt0.in");
	int T;
	sin >> T;
	REP(i,T)
	{
		sin >> n >> j;
		sout << "Case #" << i + 1 << ":" << endl;
		generate(1, "1");
	}
	return 0;
}
