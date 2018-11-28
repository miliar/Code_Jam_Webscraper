#define _CRT_SECURE_NO_DEPRECATE
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <ctime>
#include <math.h>
#include <vector>
#include <string>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <sstream>
#include <complex>
using namespace std;

#define X first
#define Y second
#define pb push_back
#define mp make_pair

const double PI = acos(-1.0);
const int INF = 1e9;
const int MOD = 1e9 + 7;
const int M = INF;
const double RRR = 180.0 / PI;


typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef vector<int> vi;





int main()
{

	freopen("INPUT.TXT", "r", stdin);
	freopen("OUTPUT.TXT","w",stdout);
	int t;
	cin >> t;
	int test = 1;
	while (t--)
	{
		ld c, f, x;
		cin >> c >> f >> x;
		ld rez = (f*x-f*c-2*c) / (f*c);
		int k1 = floor(rez);
		if (k1 < 0.0)
		{
			k1 = -1.0;
		}
		ld ans = 0.0;
		for (int i = 0; i <= k1; i++)
		{
			ans += c / (2.0 + (ld)i*f);
		}
		ans += x / (2.0 + ((ld)k1 + 1.0)*f);
		cout << "Case #" << test << ": ";
		printf("%.10f\n", (double)ans);
		test++;
	}
	return 0;
}