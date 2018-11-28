#include <bits/stdc++.h>

#define pb push_back
#define f first
#define s second
#define pii pair<int, int>
#define mp make_pair
 
using namespace std;
 
const string name = "B",
             in_file = name + ".in",
             out_file = name + ".out";
 
ifstream fin(in_file);
ofstream fout(out_file);
 
string str;
int tests;
long long sol;

void solve() {
	sol = 0;
	unsigned i = 0;
	while (i < str.size()) {
		while (i < str.size() && str[i] == '+')
			i++;
		bool begin = (i == 0 ? true : false);
		if (i == str.size())
			break;
		while (i < str.size() && str[i] == '-') 
			i++;
		if (begin)
			sol++;
		else sol += 2;
	}
}

int main() {
	fin >> tests;
	for (int t = 1; t <= tests; t++) {
		fin >> str;
		solve();
		fout << "Case #" << t << ": " << sol << '\n';
	}
	return 0;
}