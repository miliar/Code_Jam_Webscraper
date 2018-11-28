#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

//#define NDEBUG
#ifdef NDEBUG
#define DEBUG if (false)
#else
#define DEBUG if (true)
#endif

#pragma GCC diagnostic warning "-Wall"
#define WRITE(x) DEBUG { cout << x << endl; }
#define WATCH(x) DEBUG { cout << #x << " = " << x << endl; }
#define ALL(x) (x).begin(), (x).end()
#define FORN(i, a, b) for(typeof(b) i = (a); i < (b); i++)
#define FOREACH(i, c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)

int main(){
	//Descomente para acelerar cin
	//ios::sync_with_stdio(false);
	vector<unsigned long long int> fsv;
	fsv.push_back(1);
	fsv.push_back(4);
	fsv.push_back(9);
	fsv.push_back(121);
	fsv.push_back(484);

	int t;
	scanf("%d", &t);
	FORN(tg, 0, t){
		int A, B;
		int out =0;
		scanf("%d %d", &A, &B);
		FOREACH(v, fsv){
			if (*v >= A && *v <= B) out++;
		}
		printf("Case #%d: %d\n", tg+1, out);
	}
	return 0;
}
