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
#include <climits>

using namespace std;

typedef unsigned long long ull;

int solve(int r, int c, int w)
{
	if (w>c) return 0;
	if (w==1) return r*c;
	if (w==c) return (r-1)+c;
	if (r==1) return (c-1)/w+w;

	return solve(1,c,w)+(r-1)*(c/w);
}

int main() {
int t,r,c,w;

	FILE *in, *out;
	freopen_s(&in, "in.txt", "r", stdin);
	freopen_s(&out, "out.txt", "w", stdout);

	cin >> t;

	for (int i=1;i<=t;i++)
	{
		cin >> r >> c >> w;
		cout << "Case #" << i << ": " << solve(r,c,w) << endl;
	}

	return 0;
}
