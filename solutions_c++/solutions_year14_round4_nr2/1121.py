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

s32 N;
vector<s32> v;

void Smart()
{
}

bool Ok(vector<s32> &w) {
    bool b=false;
    FOR (i,0,w.size()-1) {
        if (b) {
            if (w[i] < w[i+1]) return false;
        } else {
            if (w[i] > w[i+1]) b = true;
        }
    }
    return true;
}

void Swap(vector<s32> &w, s32 i, s32 j) {
    s32 tmp = w[i];
    w[i] = w[j];
    w[j] = tmp;
}

void Naive()
{
    vector<vector<s32>> u, u_new;
    u.push_back(v);
    if (Ok(v)) {
        cout << 0;
        return;
    }
    set<vector<s32>> dic;
    for (s32 m=1; ;m++) {
        FOR (i,0,u.size()) {
            FOR (j,0,N-1) {
                Swap(u[i], j, j+1);
                if (Ok(u[i])) {
                    cout << m;
                    return;
                }
                if (dic.insert(u[i]).second) {
                    u_new.push_back(u[i]);
                }
                Swap(u[i], j, j+1);
            }
        }
        u.swap(u_new);
        u_new.clear();
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

        cin >> N;
        v.assign(N,0);
        FOR (i,0,N) cin >> v[i];

		Naive();
		cout << endl;
	}

	return 0;
}
