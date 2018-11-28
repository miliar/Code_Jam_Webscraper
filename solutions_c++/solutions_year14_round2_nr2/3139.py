/*
	Author: Zhaohai Nathaniel Lee <Nathanielben@gmail.com> @ inspiratune.com
*/

// Include the header files
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <ctype.h>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <math.h>
#include <memory>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <time.h>
#include <utility>
#include <vector>

// Input/Output
#define IN "in"
#define OUT "out"

#define START_INPUT ifstream cin (IN);freopen (IN, "r", stdin);
#define START_OUTPUT ofstream cout (OUT);freopen (OUT, "w", stdout);
#define END_INPUT fclose (stdin);cin.close ();
#define END_OUTPUT fclose (stdout);cout.close ();

// Set the namespace
using namespace std;

// Align of types
typedef complex < double >pnt;
typedef long double LD;
typedef long long ll;
typedef unsigned long long ull;
typedef pair < int, int >pii;
typedef vector < int >vi;
typedef vector < string > vs;
typedef vector < vector < int > >vii;

// Global declear
const double eps = 1e-11;

// Quick marco defination
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define twoL(X) (((int64)(1))<<(X))
#define two(X) (1<<(X))
#define containL(S,X) (((S)&twoL(X))!=0)
#define contain(S,X) (((S)&two(X))!=0)
#define VAR(a,b) __typeof(b) a=(b)
#define ALL(x) (x).begin(), (x).end()
#define RANGE(x,a,b) (x).begin(a), (x).end()
#define SIZE(x) ((int)(x.size()))
#define LENGTH(x) ((int)(x.length()))
#define MP(x,y) make_pair(x,y)
#define CLR(x,a) memset(x,a,sizeof(x))
#define ZERO(x) memset(x,0,sizeof(x))
#define foreach(c,itr) for(__typeof((c).begin()) itr=(c).begin();itr!=(c).end();itr++)
#define fabsl __builtin_fabsl
#define atan2l __builtin_atan2l
#define cosl __builtin_cosl
#define sinl __builtin_sinl
#define sqrtl __builtin_sqrtl
#define ST first
#define ND second
#define PB push_back
#define MAXN 65535

inline long long int gen (long long int a, long long int b);

int main()
{
	START_INPUT
	START_OUTPUT

    int T_period = 0;
    cin >> T_period;
    for (int T_cycle = 1; T_cycle <= T_period; ++T_cycle)
	{
		// input here
		long long int a = 0, b = 0, k = 0;
		int cnt = 0;
		cin >> a >> b >> k;
		// solve here
		long long int a1 = a, b1 = b;
		for (long long int i = a - 1; i >= 0; --i)
		{
			for (long long int j = b - 1; j >= 0; --j)
			{
				if (k > gen(i,j))
				//cout << i << " " << j << " " << gen (i,j)<<endl;
					++cnt;
			}
		}
		//output here
		cout << "Case #" << T_cycle << ": " << cnt << endl;
	}

    END_INPUT
    END_OUTPUT
    return 0;
}

inline long long int gen (long long int a, long long int b)
{
	return a & b;
}
