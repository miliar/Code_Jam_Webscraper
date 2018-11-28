// codejam_template.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
#include <bitset>
#include <unordered_map>
#include <unordered_set>

//#define DEBUG

#ifdef DEBUG
#define		fin		cin
#define		fout	cout
#endif

using namespace std;

int main()
{
#ifndef DEBUG
	fstream fin, fout;
	fin.open("A-large.in", ios::in);
	fout.open("A-large.out", ios::out);
#endif

	int T;
	fin >> T;
	for (int cases = 1; cases <= T; cases++) {
		unordered_map<char, int> hmap;
		string s;
		fin >> s;

		for (int i = 0; i < s.length(); i++)
			hmap[s[i]]++;

		string r = "";

		while (hmap['Z'] > 0) {
			r += "0";
			hmap['Z']--;
			hmap['E']--;
			hmap['R']--;
			hmap['O']--;
		}

		while (hmap['W'] > 0) {
			r += "2";
			hmap['T']--;
			hmap['W']--;
			hmap['O']--;
		}

		while (hmap['G'] > 0) {
			r += "8";
			hmap['E']--;
			hmap['I']--;
			hmap['G']--;
			hmap['H']--;
			hmap['T']--;
		}

		while (hmap['U'] > 0) {
			r += "4";
			hmap['F']--;
			hmap['O']--;
			hmap['U']--;
			hmap['R']--;
		}

		while (hmap['X'] > 0) {
			r += "6";
			hmap['S']--;
			hmap['I']--;
			hmap['X']--;
		}

		while (hmap['F'] > 0) {
			r += "5";
			hmap['F']--;
			hmap['I']--;
			hmap['V']--;
			hmap['E']--;
		}

		while (hmap['S'] > 0) {
			r += "7";
			hmap['S']--;
			hmap['E']--;
			hmap['V']--;
			hmap['E']--;
			hmap['N']--;
		}

		while (hmap['T'] > 0) {
			r += "3";
			hmap['T']--;
			hmap['H']--;
			hmap['R']--;
			hmap['E']--;
			hmap['E']--;
		}

		while (hmap['O'] > 0) {
			r += "1";
			hmap['O']--;
			hmap['N']--;
			hmap['E']--;
		}

		while (hmap['N'] > 0) {
			r += "9";
			hmap['N']--;
			hmap['I']--;
			hmap['N']--;
			hmap['E']--;
		}

		sort(r.begin(), r.end());
		fout << "Case #" << cases << ": " << r << endl;
	}

	return 0;
}

