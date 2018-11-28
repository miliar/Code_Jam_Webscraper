#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <cstring>
#include <bitset>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <climits>
#include <cmath>
#include <utility>

using namespace std;

const long MAXT = 100;

int t;
int n[MAXT];

long solve(long x) {
	int c = 0;
	set<char> d;
	while (d.size() < 10) {
		c++;
		string cn = to_string(c*x);
		for (int i = 0; i < cn.size(); i++) {
			d.insert(cn[i]);
		}
	}
	return c*x;
}

int main() {
	ifstream fin ("A-large.in");
	ofstream fout ("cs.out");
	fin >> t;
	for (int i = 0; i < t; i++) {
		fin >> n[i];
	}
	fin.close();

	for (int i = 0; i < t; i++) {
		fout << "Case #" << i+1 << ": ";
		if (n[i] == 0) fout << "INSOMNIA \n";
		else fout << solve(n[i]) << endl;
	}
	fout.close();
}
