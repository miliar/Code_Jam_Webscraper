#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <ctime>
#include <climits>
#include <cassert>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <bitset>
#include <utility>
#include <algorithm>

#define forn(i, n) for (int i = 0; i < int(n); i++)

using namespace std;

typedef long long li;

li place(li n, li index)
{
	if (index == n)
	{
		return n;
	}
	else
	{
		li r = n - index - 1;
		li l = index - 1;
		return place(n / 2, n / 2 - r / 2);
	}
}

li bad(li before, li n, li index)
{
	if (index == 1)
	{
		return before + 1;
	}
	else
	{
		li r = n - index;
		li l = index - 2;
		return bad(before + n / 2, n / 2, 1 + l / 2);
	}
}

int main(int argc, char* argv[])
{
    // freopen("input.txt", "rt", stdin);

    int testCases;
    cin >> testCases;
	li a = 0;
	li b = 0;

    forn(tt, testCases)
    {
    	li n, size;
    	cin >> n >> size;
    	n = 1LL << n;

    	{
        	li l = 1;
        	li r = n;
        	while (r - l > 1)
        	{
        		li mid = (l + r) / 2;
        		if (place(n, mid) <= size)
        			l = mid;
        		else
        			r = mid;
        	}

        	for (li i = l; i <= r; i++)
        		if (place(n, i) <= size)
        			b = i;
    	}

    	{
        	li l = 1;
        	li r = n;
        	while (r - l > 1)
        	{
        		li mid = (l + r) / 2;
        		if (bad(0, n, mid) <= size)
        			l = mid;
        		else
        			r = mid;
        	}

        	for (li i = l; i <= r; i++)
        		if (bad(0, n, i) <= size)
        			a = i;
    	}

    	cout << "Case #" << (tt + 1) << ": " << a - 1 << " " << b - 1 << endl;
    }

    return 0;
}
