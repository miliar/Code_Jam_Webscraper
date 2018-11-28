// K1
// :)

#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <queue>
#include <bitset>
#include <string>
#include <cmath>
#include <iomanip>
#include <set>
#include <map>

#define EPS 1e-8
#define PI 3.141592653589793
#define X first
#define Y second
#define FX(x) fixed << setprecision((x))

using namespace std;

typedef pair<int, int> point;
typedef set<int>::iterator ITR;
const int MAXN = 2e5 + 123;


int main()
{
	int t;
	cin >> t;
	for (int test = 0; test < t; ++test)
	{
		int r, c, w;
		cin >> r >> c >> w;
		long long result = (r-1) * (c/w) + (c - w) / w + min(w + 1, c - ((c - w) / w) * w);
		cout << "Case #" << test+1 << ": " << result << endl;
	}

	return 0;
}