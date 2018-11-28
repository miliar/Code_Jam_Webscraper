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
s64 N, M, O[1000], E[1000], P[1000];

void Smart()
{
}

s64 Cost(s64 i, s64 j) {
    return (j-i)*(2*N-j+i+1)/2;
}

void Naive()
{
    vector<s64> v(N+1);
    s64 a=0, b=0;
    FOR (i,0,M) {
        FOR (j,O[i],E[i]) v[j] += P[i];
        b += P[i] * Cost(O[i],E[i]);
    }
    while (true) {
        // Check
        bool ok=true;
        FOR (i,0,v.size()) {
            if (v[i]>0) { ok=false; break; }
        }
        if (ok) break;
        bool ok2=false;
        FOR (i,0,v.size()) {
            if (ok2) break;
            if (v[i]==0) continue;
            for (s32 j=i; ; j++) {
                if (j==v.size() || v[j]==0) {
                    a += Cost(i,j);
                    ok2=true;
                    break;
                }
                v[j] --;
            }
        }
    }
    cout << b-a ;
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
        cin >> N >> M;
        FOR (i,0,M) cin >> O[i] >> E[i] >> P[i];
		Naive();
		cout << endl;
	}

	return 0;
}
