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

s64 L, X;
string s;

void Smart()
{
}

s32 Key(char c) {
    if (c=='i') return 1;
    if (c=='j') return 2;
    if (c=='k') return 3;
    return 0;
}

// p * q (g:sign).
s32 Next(s32 j, s32 &g, s32 p, s32 q) {
    if (q==0) return p;
    if (p==1) {
        if (q==1) { q=0; g*=-1; }
        else if (q==2) { q=3; }
        else if (q==3) { q=2; g*=-1; }
    } else if (p==2) {
        if (q==1) { q=3; g*=-1; }
        else if (q==2) { q=0; g*=-1; }
        else if (q==3) { q=1; }
    } else if (p==3) {
        if (q==1) { q=2; }
        else if (q==2) { q=1; g*=-1; }
        else if (q==3) { q=0; g*=-1; }
    }
    return q;
}

void Naive()
{
    string t;
    FOR (i,0,X) t += s;
    s32 g = 1, q = 0;
    FOR (i,0,t.size()) {
        s32 p = Key(t[i]);
        q = Next(i, g, q, p);
    }
    if (!(g==-1 && q==0)) {
        cout << "NO";
        return;
    }

    bool ok1 = false, ok2 = false;
    s32 p1, p2;
    g = 1, q = 0;
    FOR (i,0,t.size()) {
        s32 p = Key(t[i]);
        q = Next(i, g, q, p);
        if (!(g==1 && q==1)) continue;
        ok1 = true;
        p1 = i;
        break;
    }
    g = 1, q = 0;
    FOR (i,0,t.size()) {
        s32 p = Key(t[t.size()-i-1]);
        q = Next(i, g, p, q);
        if (!(g==1 && q==3)) continue;
        ok2 = true;
        p2 = t.size()-i-1;
        break;
    }
    if (!ok1 || !ok2) cout << "NO";
    else if (p1 < p2) cout << "YES";
    else cout << "NO";
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
        cin >> L >> X >> s;
		Naive();
		cout << endl;
	}

	return 0;
}
