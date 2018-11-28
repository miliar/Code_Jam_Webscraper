// topcoder.cpp : �R���\�[�� �A�v���P�[�V�����̃G���g�� �|�C���g���`���܂��B
//

#include <stdio.h>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <numeric>
#include "assert.h"

using namespace std;
static const double EPS = 1e-9;
int ROUND(double x) { return (int)(x+0.5); }
bool ISINT(double x) { return fabs(ROUND(x)-x)<=EPS; }
bool ISEQUAL(double x,double y) { return fabs(x-y)<=EPS*max(1.0,max(fabs(x),fabs(y))); }
double SQSUM(double x,double y) { return x*x+y*y; }
template<class T> bool INRANGE(T x,T a,T b) { return a<=x&&x<=b; }
template<class T> void amin(T &a,T v){if(a>v) a=v;}
template<class T> void amax(T &a,T v){if(a<v) a=v;}
#define PI	(3.14159265358979323846)
#define ARRAY_NUM(a) (sizeof(a)/sizeof(a[0])) 
#define NG (-1)
#define BIG (987654321)
#define SZ(a) ((int)a.size())
typedef long long ll;

#define FOR(v,i) for(__typeof((v).begin())i=(v).begin();i!=(v).end();++i)
// BEGIN CUT HERE
#undef FOR
#define FOR(v,i) for(auto i=(v).begin();i!=(v).end();++i)
// END CUT HERE

#define PRINTF(fmt,...) fprintf(stderr,fmt,__VA_ARGS__); printf(fmt,__VA_ARGS__);


int main(){

	freopen("_google_code_jam_input.txt","r",stdin);
	freopen("_google_code_jam_output.txt","w",stdout);

	int T;
	scanf("%d",&T);

	for (int testcase = 0; testcase < T; testcase++)
	{
		int N;
		cin >> N;
		vector <ll> m(N);
		for (int i = 0; i < N; ++i)
		{
			cin >> m[i];
		}

		ll ret1 = 0, ret2 = 0;
		{
			for (int i = 0; i < N-1; ++i)
			{
				ret1 += max(0LL,m[i]-m[i+1]);
			}
		}

		{
			ll waste = 0;
			for (int i = 0; i < N-1; ++i)
			{
				amax(waste,max(0LL,m[i]-m[i+1]));
			}

			for (int i = 0; i < N-1; ++i)
			{
				ret2 += min(waste,m[i]);
			}
		}


		



		PRINTF("Case #%d: %lld %lld\n",testcase+1, ret1, ret2);
	}

	return 0;
}
