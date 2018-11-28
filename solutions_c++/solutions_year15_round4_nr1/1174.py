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

struct P {
	s32 x, y;
};

s32 R, C;
const s32 M = 101;
s32 d[M][M];

void Smart()
{
}

void Naive()
{
	s32 l[M][M], r[M][M], t[M][M], b[M][M];
	memset(l, 0, sizeof(s32)*M*M);
	memset(r, 0, sizeof(s32)*M*M);
	memset(t, 0, sizeof(s32)*M*M);
	memset(b, 0, sizeof(s32)*M*M);
	FOR(i, 0, R) {
		s32 c = 0;
		FOR(j, 0, C) {
			l[i][j] = c;
			if (d[i][j] != 0) c = 1;
		}
	}
	FOR(i, 0, R) {
		s32 c = 0;
		for (s32 j = C - 1; j >= 0; j--) {
			r[i][j] = c;
			if (d[i][j] != 0) c = 1;
		}
	}
	FOR(j, 0, C) {
		s32 c = 0;
		FOR(i,0,R) {
			t[i][j] = c;
			if (d[i][j] != 0) c = 1;
		}
	}
	FOR(j, 0, C) {
		s32 c = 0;
		for (s32 i = R - 1; i >= 0; i--) {
			b[i][j] = c;
			if (d[i][j] != 0) c = 1;
		}
	}
	s32 a = 0;
	FOR(i, 0, R) FOR(j, 0, C) {
		if (d[i][j] == 0) continue;
		if (!l[i][j] && !r[i][j] && !t[i][j] && !b[i][j]) {
			cout << "IMPOSSIBLE";
			return;
		}
		if (d[i][j] == 1) {
			if (!t[i][j]) a++;
		}
		if (d[i][j] == 2) {
			if (!b[i][j]) a++;
		}
		if (d[i][j] == 3) {
			if (!l[i][j]) a++;
		}
		if (d[i][j] == 4) {
			if (!r[i][j]) a++;
		}
	}
	cout << a;
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
	FOR (tt,0,num_of_trial) {

		memset(d, 0, sizeof(s32)*M*M);
		cin >> R >> C;
		FOR(i, 0, R) {
			string s;
			cin >> s;
			FOR(j, 0, C) {
				if (s[j] == '.') d[i][j] = 0;
				if (s[j] == '^') d[i][j] = 1;
				if (s[j] == 'v') d[i][j] = 2;
				if (s[j] == '<') d[i][j] = 3;
				if (s[j] == '>') d[i][j] = 4;
			}
		}

		cout << "Case #" << tt+1 << ": ";
		Naive();
		cout << endl;
	}

	return 0;
}
