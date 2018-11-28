// ConsoleApplication2.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <ctgmath>
#include <algorithm>
#include <set>
#include <utility>

#define min(a,b) a<b?a:b
#define max(a,b) a>b?a:b
#define ull unsigned long long
#define ll unsigned long long
#define FOR(i,n) for(ull i = 0; i<n; ++i)
#define all(v) v.begin(),v.end()

using namespace std;

void simplify(string& s) {
	int ii = 0;
	for (size_t i = 1; i < s.size(); i++)
	{
		if (s[i] != s[ii]) {
			ii++;
			s[ii] = s[i];
		}
	}
	s.resize(ii + 1);
}

int main()
{
	ifstream fin("a.in");
	ofstream fout("a.out");

	ull T, N;
	fin >> T;

	string tmp;
	for (int t = 1; t <= T; ++t) {
		ull sol = 1;
		fin >> N;
		vector<string> strs;

		FOR(n, N) {
			fin >> tmp;
			simplify(tmp);
			strs.push_back(tmp);
		}

		sort(all(strs));

		set<string> pieces;
		ull cnt = 0;
		ull bzaf = 1000000007;
		for (auto itStrs = strs.begin(); itStrs < strs.end(); itStrs++) {
			pieces.insert(*itStrs);
			ull currentCount = count(itStrs + 1, strs.end(), *itStrs);
			itStrs += currentCount;
			sol *= currentCount+1;
			sol %= bzaf;
			if (currentCount != 0 && itStrs->size() != 1) {
				sol = 0;
			}
		}
		if (sol != 0) {
		ull gdach = pieces.size();
		while (gdach-- >0)
		{
			sol *= gdach;
			sol %= bzaf;
		}

		}

		fout << "Case #" << t << ": " << sol << endl;
	}


	return 0;
}