#include <cstdlib>
#include <map>
#include <algorithm>
#include<iostream>
#include <vector>
#include <string>
#include<fstream>
using namespace std;
map<pair<char, int>, string> cache;
int T;
int N, S, R, P;

string solve(char x, int n) {
	auto key = make_pair(x, n);
	if (n == 0) {
		string ret; ret += x;
		return ret;
	}
	if (cache.find(key) != cache.end()) {
		return cache[key];
	}
	string sol1, sol2;
	if (x == 'P') {
		sol1 = solve('P', n - 1);
		sol2 = solve('R', n - 1);
	}
	if (x == 'R') {
		sol1 = solve('S', n - 1);
		sol2 = solve('R', n - 1);
	}
	if (x == 'S') {
		sol1 = solve('S', n - 1);
		sol2 = solve('P', n - 1);
	}
	string ret = min(sol1 + sol2, sol2 + sol1);
	cache[key] = ret;
	return ret;
}

bool check_sol(string sol) {
	map<char, int> count;
	for (int i = 0; i < sol.size(); ++i)
		count[sol[i]]++;
	return count['R'] == R && count['P'] == P && count['S'] == S;
}

int main(int argc, char** argv) {
	ifstream fin("A-large.in");
	fin.exceptions(ifstream::failbit | ifstream::badbit);

	ofstream fo("A-large.out");
	fin >> T;
	for (int t = 1; t <= T; ++t) {
		fin >> N >> R >> P >> S;
		string sol1 = solve('P', N);
		string sol2 = solve('R', N);
		string sol3 = solve('S', N);
		
		if (!check_sol(sol1)) sol1 = "Z";
		if (!check_sol(sol2)) sol2 = "Z";
		if (!check_sol(sol3)) sol3 = "Z";
		string sol = min(min(sol1, sol2), sol3);
		if (sol == "Z") {
			sol = "IMPOSSIBLE";
		}
		fo << "Case #" << t << ": " << sol << endl;
	}
	fo.close();
	return 0;
}

