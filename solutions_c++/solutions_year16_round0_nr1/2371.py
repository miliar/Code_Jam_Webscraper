#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <queue>
#include <map>
#include <stack>
#include <complex>
#include <random>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;

int T, N;

int go()
{
	set<int> d;
	int cur = N;
	for (int num = cur; num > 0; num /= 10)
		d.insert(num % 10);
	while (d.size() != 10)
	{
		cur += N;
		for (int num = cur; num > 0; num /= 10)
			d.insert(num % 10);
	}
	return cur;
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	ios::sync_with_stdio(0);

	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		cin >> N;
		if (N == 0)
			cout << "Case #" << t << ": INSOMNIA\n";
		else
			cout << "Case #" << t << ": " << go() << "\n";
	}

	return 0;
}