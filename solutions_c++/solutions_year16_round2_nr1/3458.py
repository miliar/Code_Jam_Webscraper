#pragma comment(linker, "/STACK:134217728")
#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <string>
#include <numeric>
#include <complex>
#include <functional>
#include <cmath>
#include <time.h>

using namespace std;

typedef long long LL;

set<map<char, int>> dp;
vector<int> answ;

bool go(map<char,int> v) {
	bool f = true;
	for (int i = 'A'; i <= 'Z'; i++) {
		if (v[i]!= 0) {
			f = false;
			break;
		}
	}
	if (f) {
		return true;
	}
	if (dp.find(v) != dp.end())
		return false;
	dp.insert(v);
	if (v['O'] > 0 && v['N'] > 0 && v['E'] > 0) {
		v['O']--;
		v['N']--;
		v['E']--;
		if (go(v)) {
			answ.push_back(1);
			return true;
		}
		v['O']++;
		v['N']++;
		v['E']++;
	}

	if (v['T'] > 0 && v['W'] > 0 && v['O'] > 0) {
		v['T']--;
		v['W']--;
		v['O']--;
		if (go(v)) {
			answ.push_back(2);
			return true;
		}
		v['T']++;
		v['W']++;
		v['O']++;
	}

	if (v['Z'] > 0 && v['E'] > 0 && v['R'] > 0 && v['O'] > 0) {
		v['Z']--;
		v['E']--;
		v['R']--;
		v['O']--;
		if (go(v)) {
			answ.push_back(0);
			return true;
		}
		v['Z']++;
		v['E']++;
		v['R']++;
		v['O']++;
	}

	if (v['T'] > 0 && v['H'] > 0 && v['R'] > 0 && v['E'] > 1) {
		v['T']--;
		v['H']--;
		v['R']--;
		v['E']--;
		v['E']--;
		if (go(v)) {
			answ.push_back(3);
			return true;
		}
		v['T']++;
		v['H']++;
		v['R']++;
		v['E']++;
		v['E']++;
	}

	if (v['F'] > 0 && v['O'] > 0 && v['U'] > 0 && v['R'] > 0) {
		v['F']--;
		v['O']--;
		v['U']--;
		v['R']--;
		if (go(v)) {
			answ.push_back(4);
			return true;
		}
		v['F']++;
		v['O']++;
		v['U']++;
		v['R']++;
	}

	if (v['F'] > 0 && v['I'] > 0 && v['V'] > 0 && v['E'] > 0) {
		v['F']--;
		v['I']--;
		v['V']--;
		v['E']--;
		if (go(v)) {
			answ.push_back(5);
			return true;
		}
		v['F']++;
		v['I']++;
		v['V']++;
		v['E']++;
	}

	if (v['S'] > 0 && v['I'] > 0 && v['X'] > 0) {
		v['S']--;
		v['I']--;
		v['X']--;
		if (go(v)) {
			answ.push_back(6);
			return true;
		}
		v['S']++;
		v['I']++;
		v['X']++;
	}
	if (v['S'] > 0 && v['E'] > 1 && v['V'] > 0 && v['N'] > 0) {
		v['S']--;
		v['E']--;
		v['V']--;
		v['E']--;
		v['N']--;
		if (go(v)) {
			answ.push_back(7);
			return true;
		}
		v['S']++;
		v['E']++;
		v['V']++;
		v['E']++;
		v['N']++;
	}

	if (v['E'] > 0 && v['I'] > 0 && v['G'] > 0 && v['H'] > 0 && v['T'] > 0) {
		v['E']--;
		v['I']--;
		v['G']--;
		v['H']--;
		v['T']--;
		if (go(v)) {
			answ.push_back(8);
			return true;
		}
		v['E']++;
		v['I']++;
		v['G']++;
		v['H']++;
		v['T']++;
	}

	if (v['N'] > 1 && v['I'] > 0 && v['E'] > 0) {
		v['N']--;
		v['I']--;
		v['N']--;
		v['E']--;
		if (go(v)) {
			answ.push_back(9);
			return true;
		}
		v['N']++;
		v['I']++;
		v['N']++;
		v['E']++;
	}
	return false;
}
int main()
{
	//Z,E,R,O,N,T,W,H,F,I,X,S
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int k;
	cin >> k;
	int t = 1;
	while (k--> 0) {
		string s;
		cin >> s;
		printf("Case #%d: ", t++);
		map<char, int> res;
		answ.clear();
		dp.clear();
		for (int i = 'A'; i <= 'Z'; i++) {
			res[i] = 0;
		}
		for (int i = 0; i < s.size(); i++) {
			res[s[i]]++;
		}
		if (!go(res)) {
			cout << "Pizda";
		}
		sort(answ.begin(), answ.end());
		for (int i = 0; i < answ.size(); i++)
			cout << answ[i];
		cout << endl;
	}
	return 0;
}