
#include "stdafx.h"
#include <cstdio>
#include <cassert>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ifstream fin;
	ofstream fout;
	fin.open("C:\\Users\\ravill\\Documents\\Algo\\A-large.in");
	fout.open("C:\\Users\\ravill\\Documents\\Algo\\A-large.out");
	int T;
	fin >> T;
	char C[10];

	vector<pair<char, int>> v;
	v.push_back(pair<char, int>('U', 4));
	v.push_back(pair<char, int>('Z', 0));
	v.push_back(pair<char, int>('W', 2));
	v.push_back(pair<char, int>('X', 6));
	v.push_back(pair<char, int>('G', 8));
	v.push_back(pair<char, int>('O', 1));
	v.push_back(pair<char, int>('T', 3));
	v.push_back(pair<char, int>('F', 5));
	v.push_back(pair<char, int>('S', 7));
	v.push_back(pair<char, int>('I', 9));

	vector<string> str;
	str.push_back("ZERO");
	str.push_back("ONE");
	str.push_back("TWO");
	str.push_back("THREE");
	str.push_back("FOUR");
	str.push_back("FIVE");
	str.push_back("SIX");
	str.push_back("SEVEN");
	str.push_back("EIGHT");
	str.push_back("NINE");

	for (int ccnt = 1; ccnt <= T; ccnt++) {
		char s[2002];
		int N[200];
		memset(N, 0, sizeof(N));
		fin >> s;
		for (int i = 0; i < strlen(s); i++) {
			N[s[i]]++;
		}
		string ret = "";
		for (int i = 0; i < 10; i++) {
			int count = N[v[i].first];
			for (int j = 0; j < count; j++) {
				ret += (char)(v[i].second +'0');
				for (int k = 0; k < str[v[i].second].size(); k++) {
					N[str[v[i].second][k]]--;
				}
			}
		}
		sort(ret.begin(), ret.end());
		cout << "Case #" << ccnt << ": " <<ret << endl;
		fout << "Case #" << ccnt << ": " << ret << endl;
	}
	return 0;
}

