#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(int)(b);i++)
#define REP(i,a) for(int i=0;i<(int)(a);i++)
#define ALL(i) i.begin(),i.end()
#define rALL(i) i.rbegin(),i.rend()
#define PB push_back

typedef vector<int> vi;
typedef vector<vector<int> > vvi;

template<class T> string i2a(T x) {ostringstream oss; oss<<x; return oss.str();}

int main()
{

   freopen("B-small-attempt0.in", "r", stdin);
   freopen("B-small-attempt0.out", "w", stdout);

	int cases;
	string s;
	getline(cin, s);
	sscanf(s.c_str(), "%d",&cases);
	REP(k, cases) {
		printf("Case #%d: ", k + 1);
		getline(cin,s);
		int a, b, k;
		sscanf(s.c_str(),"%d %d %d", &a, &b, &k);;
		int count = 0;
		for(int i = 0; i < a; i++) {
			for(int j = 0; j < b; j++) {
				if((i & j) < k) count++;
			}
		}
		printf("%d\n", count);
	}
    return 0;
}
