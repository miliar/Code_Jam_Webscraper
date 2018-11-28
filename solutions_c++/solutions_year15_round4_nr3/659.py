#include <stdio.h>
#include <cstdlib>
#include <string.h>
#include <math.h>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <iostream>
#include <fstream>
#include <map>
#include <algorithm>
#include <sstream>
#include "windows.h"
//#include "../../gmp_int.h"
//#include "../../common.h"
#define MAX(a, b)		((a)>(b)?(a):(b))
#define MAX3(a, b, c)	(MAX((a),MAX((b),(c))))
#define FOR(a,b,c)		for (s32(a)=(b);(a)<(s32)(c);(a)++)
#define BL				{char bl[10];cin.getline(bl, 10);}
#define GL(c)			cin.getline(c, sizeof(c))
typedef char					s8;
typedef unsigned char			u8;
typedef short					s16;
typedef unsigned short			u16;
typedef int						s32;
typedef unsigned int			u32;
typedef long long int			s64;
typedef unsigned long long int	u64;
using namespace std;

ifstream test_input;
#define cin test_input

s32 N;
vector<vector<string>> w;

void Smart()
{
}

void Put(set<string> &d, vector<string> &s) {
	FOR(i, 0, s.size()) {
		d.insert(s[i]);
	}
}

map<string, s32> mm;
s32 ToInt(string s) {
	auto i = mm.find(s);
	if (i == mm.end()) {
		mm.insert(pair<string, s32>(s, mm.size()));
		return mm.size() - 1;
	}
	else return i->second;
}

void Put(vector<s32> &d, vector<s32> &s) {
	//FOR(i, 0, s.size()) {
	//	//s32 k = ToInt(s[i]);
	//	d.push_back(s[i]);
	//}
	d.insert(d.end(), s.begin(), s.end());
}

void Put(vector<bool> &d, vector<s32> &s) {
	FOR(i, 0, s.size()) {
		d[s[i]] = true;
	}
//	d.insert(d.end(), s.begin(), s.end());
}


void Naive()
{
	mm.clear();
	s32 m_best = 1000000;
	vector<vector<s32>> x;
	FOR(i, 0, N) {
		vector<s32> y;
		FOR(j, 0, w[i].size()) {
			y.push_back(ToInt(w[i][j]));
		}
		x.push_back(y);
	}
	s32 p = mm.size();
	vector<bool> EE(p), FF(p);
	vector<s32> E, F;
	Put(EE, x[0]);
	Put(FF, x[1]);

	for (s32 i = 0; i < (1 << (N - 2)); i++) {
		vector<bool> e = EE, f = FF;
		//Put(e, x[0]);
		//Put(f, x[1]);
		FOR(j, 0, N - 2) {
			if (i & (1 << j)) Put(e, x[j+2]);
			else Put(f, x[j+2]);
		}
		//sort(e.begin(), e.end());
		//e.erase(unique(e.begin(), e.end()), e.end());
		//sort(f.begin(), f.end());
		//f.erase(unique(f.begin(), f.end()), f.end());


		s32 m = 0;
		//for (auto j = e.begin(); j != e.end(); j++) {
		//	if (std::binary_search(f.begin(), f.end(), *j)) {
		//		m++;
		//	}
		//}
		FOR(j, 0, p) {
			if (e[j] && f[j]) m++;
		}
		if (m_best > m) {
			m_best = m;
		}
	}
	cout << m_best;
}

int main(int argc, char* argv[])
{
	cout.precision(15);
	if (argc!=2) {
		cout << "Need input file name." << endl;
		return 0;
	}
	test_input.open(argv[1]);
	if (test_input.fail()) {
		cout << "Cannot open input file " << argv[1] << "." << endl;
		return 0;
	}

	s32 num_of_trial;
	cin >> num_of_trial;
	string str;
	FOR(tt, 0, num_of_trial) {

		w.clear();
		cin >> N;
		getline(cin, str);
		FOR(i, 0, N) {
			getline(cin, str);
			vector<string> v;
			stringstream ss(str);
			string buffer;
			while (std::getline(ss, buffer, ' ')) {
				v.push_back(buffer);
			}
			w.push_back(v);
		}
		cout << "Case #" << tt+1 << ": ";
		Naive();
		cout << endl;
	}

	return 0;
}
