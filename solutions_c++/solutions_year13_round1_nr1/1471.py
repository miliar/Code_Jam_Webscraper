#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <ctime>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <bitset>

#define all(v) v.begin(),v.end()

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
const ld epsylon = 1e-9;
typedef unsigned int ui;
inline long double get_time(){   
	return (long double)clock()/CLOCKS_PER_SEC;
};



int main()
{
	freopen("Bullseye.in","r",stdin);
	freopen("Bullseye.out","w",stdout);
	//program
	int tests;
	scanf("%d\n", &tests);
	ll r, t;
	for (int CASE = 1; CASE <= tests; ++CASE)
	{
		cin >> r >> t;
		int res = 0;
		while (t > 0)
		{
			t -= 2 * r + 1;
			r += 2;
			if (t >= 0) res++;
		}
		printf("Case #%d: %d\n", CASE, res);
	}


	//end program
	return 0;
}






