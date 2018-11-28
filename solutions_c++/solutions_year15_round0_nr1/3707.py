#pragma comment(linker, "/STACK:256000000")

#include <iostream>
#include <iomanip>

#include <map>
#include <set>
#include <vector>
#include <string>

#include <queue>
#include <deque>
#include <stack>

#include <cmath>
#include <ctime>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cstdarg>
#include <algorithm>

#include <complex>

#include <sstream>

using namespace std;

#define sqr(x) ((x)*(x))

int main()
{
	#ifdef CRABEN
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	#else
	#define file_name "A-small-attempt0"
	freopen(file_name".in", "r", stdin);
	freopen(file_name".out", "w", stdout);
	#endif

	int t; scanf("%d\n", &t);
	for (int num = 1; num <= t; num++)
	{
		int smax; scanf("%d ", &smax);

		int ans = 0, count = 0;
		for (int i = 0; i <= smax; i++)
		{
			char c = getc(stdin);
			if (count < i) count++, ans++;
			count += c - '0';
		}

		printf("Case #%d: %d\n", num, ans);
	}

	return 0;
}