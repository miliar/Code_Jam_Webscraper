#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <list>
#include <algorithm>
#include <cctype>
#include <queue>
#include <complex>
#include <functional>
#include <sstream>
#include <tuple>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tn;
    cin >> tn;
    for (int tc = 0; tc < tn; tc++)
    {
    	int x, r, c;
    	cin >> x >> r >> c;
    	if (r > c)
    		swap(r, c);
    	int fail = r * c % x != 0 || r >= 7;
    	if (x == 3)
    		if (r == 1)
    			fail = 1;
    	if (x == 4)
    		if (r <= 2)
    			fail = 1;
    	if (x == 5)
    		if (r <= 2 || r == 3 && c == 5)
    			fail = 1;
    	if (x == 6)
    		if (r <= 3)
    			fail = 1;
    	cout << "Case #" << tc + 1 << ": " << (fail ? "RICHARD" : "GABRIEL") << endl;
    }
    return 0;
}