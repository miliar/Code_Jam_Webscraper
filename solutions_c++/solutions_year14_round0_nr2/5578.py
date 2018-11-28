#include <iostream>
#include <fstream>
#include <cstdio>
#include <iomanip>
#include <cassert>
#include <climits>
#include <cmath>
#include <ctime>
#include <vector>
#include <string>
#include <cstring>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <unordered_set>
#include <unordered_map>
#include <functional>
#include <algorithm>
using namespace std;
 
typedef pair<int, int> pii;
typedef long long llong;
typedef pair<llong, llong> pll;
typedef unsigned long long ullong;
#define mp make_pair
#define sqr(x) ((x)*(x))
const double PI = 3.14159265359;
#define y1 Y1
#define y0 alalal1231



int main()
{
#ifdef MYLOCAL
    freopen("input.txt","rt",stdin);
    freopen("output.txt", "wt", stdout);
    clock_t beginTime = clock();
#endif

	int _T;
	scanf("%d", &_T);
	for (int _i = 1; _i <= _T; ++_i)
	{
		double c, f, x;
		scanf("%lf %lf %lf", &c, &f, &x);
		double t = 0.0, fi = 2;
		while (t + x / fi > t + c / fi + x / (fi + f))
			t += c / fi, fi += f;
		t += x / fi;
		printf("Case #%d: %.9lf\n", _i, t);
	}

#ifdef MYLOCAL
    //cout << endl << "time: " << double(clock() - beginTime) / CLOCKS_PER_SEC;
#endif
    return 0;
}