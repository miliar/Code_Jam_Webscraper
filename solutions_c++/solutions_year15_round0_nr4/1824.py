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

s32 X, R, C;

void Smart()
{
}

void Swap(s32 &x, s32 &y) {
    s32 tmp = x;
    x = y;
    y = tmp;
}

string Naive()
{
    if ((R*C)%X != 0) return "RICHARD";
    if (X==1) return "GABRIEL"; //‚Ç‚¤‚â‚Á‚Ä‚àƒnƒ‚ê‚È‚¢
    if (X==2) return "GABRIEL";
    if (R<C) Swap(R,C);
    if (X==3) {
        if (R>=3 && C>=2) return "GABRIEL";
        return "RICHARD";
    }
    if (X==4) {
        if (R==4 && C==2) return "RICHARD";
        if (R>=4 && C>=2) return "GABRIEL";
        return "RICHARD";
    }
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
		cout << "Case #" << tt+1 << ": ";
        cin >> X >> R >> C;
		string s = Naive();
		cout << s << endl;
	}

	return 0;
}
