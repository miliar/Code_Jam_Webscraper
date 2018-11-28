

#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
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
#include "stdio.h"
using namespace std;

int kk[2000];

void solve_case(int test_case)
{
	int n, a , b , k;
	cin >> a >> b >> k;
	memset(kk, 0, sizeof(kk));
	for (int i = 0; i < a; ++i)
	for (int j = 0; j < b; ++j)
		kk[i & j]++;

	int res = 0;
	for (int i = 0; i < k; ++i)
		res += kk[i];

	cout << "Case #" << test_case << ": ";

	
	cout << res << endl;

}

int main()
{

#ifdef __OLIMP__
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

	int T;
	scanf("%d", &T);

	for (int tc = 1; tc <= T; tc++)
		solve_case(tc);

	return 0;
}