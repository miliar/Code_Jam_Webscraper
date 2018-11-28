#pragma comment(linker, "/STACK:255000000")
#include <cstdio>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <functional>
#include <stack>
#include <memory.h>
#include <algorithm>
#include <math.h>
#include <valarray>
#include <complex>
#include <bitset>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> vint;
typedef vector<vint> vvint;
typedef complex<double> comp;

long double eps = 1e-7;
const int BASE = (int) 1e9;
const long double PI = 3.1415926535897932384626433832795;
const int MOD = (int) 1e9 + 7;
const int HMOD = (1 << 18) - 1;
const int N = 4000000;
const int INF = 1 << 30;
const LL LLINF = 1ll << 60;

int t;
int a1, a2;
int a[5][5], b[5][5];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		scanf("%d", &a1);
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				scanf("%d", &a[j][k]);
		scanf("%d", &a2);
		for (int j = 0; j < 4; j++)
			for (int k = 0; k < 4; k++)
				scanf("%d", &b[j][k]);
		set<int> s1, s2;
		for (int j = 0; j < 4; j++)
				s1.insert(a[a1 - 1][j]);
		for (int j = 0; j < 4; j++)
				s2.insert(b[a2 - 1][j]);
		for (int j = 0; j < 4; j++)
				if (s2.find(a[a1 - 1][j]) == s2.end())
					s1.erase(a[a1 - 1][j]);
		printf("Case #%d: ", i + 1);
		if (s1.size() == 1)
			printf("%d\n", *s1.begin());
		if (s1.size() == 0)
			printf("Volunteer cheated!\n");
		if (s1.size() > 1)
			printf("Bad magician!\n");
	}
	return 0;
}