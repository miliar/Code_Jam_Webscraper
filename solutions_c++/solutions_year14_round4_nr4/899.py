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

void Smart()
{
}

#define L 4
s32 M, N;
map<s32,s32> m;
vector<string> s, t[L];

s32 Do(vector<string> &v) {
    s32 a=1;
    sort(v.begin(), v.end());
    for (s32 i=0; i<v.size();) {
        vector<string> u;
        s32 j;
        for (j=i; j<v.size(); j++) {
            if (v[i][0] == v[j][0]) {
                if (v[j].size() > 1) {
                    string tmp = v[j].substr(1);
                    u.push_back(tmp);
                }
            } else {
                break;
            }
        }
        i = j;
        s32 a0 = Do(u);
        a += a0;
    }
    return a;
}

s32 Get(vector<string> &v) {
    vector<string> u = v;
    return Do(u);
}

void Next(s32 i) {
    if (i==M) {
        FOR (j,0,N) {
            if (t[j].empty()) return;
        }
        s32 a=0;
        FOR (j,0,N) {
            s32 a0 = Get(t[j]);
            a += a0;
        }
        m[a] ++;
        return;
    }
    FOR (j,0,N) {
        t[j].push_back(s[i]);
        Next(i+1);
        t[j].pop_back();
    }
}

void Naive()
{
    m.clear();
    Next(0);
    cout << m.rbegin()->first << " " << m.rbegin()->second;
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
        cin >> M >> N;
        s.clear();
        FOR (i,0,L) t[i].clear();
        FOR (i,0,M) {
            string tmp;
            cin >> tmp;
            s.push_back(tmp);
        }
		Naive();
		cout << endl;
	}

	return 0;
}
