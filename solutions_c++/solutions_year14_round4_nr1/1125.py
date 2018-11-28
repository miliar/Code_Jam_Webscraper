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

s32 N, X;
vector<s32> v;

void Smart()
{
}

void Naive()
{
    sort(v.begin(), v.end());
    s32 a = 0;
    vector<s32>::iterator i;
    while (!v.empty()) {
        a ++;
        if (v.size() == 1) break;
        s32 x = v.back();
        v.pop_back();
        i= lower_bound(v.begin(), v.end(), X-x);
        if (i==v.begin()) {
            if (*i+x > X) continue;
        } else i --;
        s32 t = i==v.end() ? v.back() : *i;
        vector<s32> v_new;
        bool done = false;
        FOR (j,0,v.size()) {
            if (!done && v[j] == t) {
                done = true;
                continue;
            }
            v_new.push_back(v[j]);
        }
        v.swap(v_new);
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
		cout << "Case #" << tt+1 << ": ";
        cin >> N >> X;
        s32 tmp;
        v.clear();
        FOR (i,0,N) {
            cin >> tmp;
            v.push_back(tmp);
        }

        //v.clear();
        //N = 10000;
        //X = 100;
        //FOR (i,0,N) v.push_back(rand()%X);

		Naive();
		cout << endl;
	}

	return 0;
}
