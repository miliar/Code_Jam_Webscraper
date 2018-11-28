#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
#include <map>
#include <set>
#include <cmath>

using namespace std;

long long L[] = {1, 4, 9, 121, 484, 12321};
//calculated by hand
int T;
long long a, b;
int main (int argc, char const* argv[])
{
    ifstream cin ("C-small.in");
	ofstream cout ("C-small.out");
	cin >> T;
	for (int t = 0; t < T; t += 1)
	{
	    cin >> a >> b;
		int hi = 0, lo = 0;
		while ( L[hi] <= b ) hi++; hi--;
		while ( L[lo] <= (a-1) ) lo++; lo--;
		cout << "Case #" << t+1 << ": " << hi - lo << '\n';
	}
	return 0;
}
