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

const li M = 1000002013LL;

li len(li n, li a)
{
	return (((n + (n - a + 1)) * a) / 2) % M;
}

int main(int argc, char* argv[])
{
    // freopen("input.txt", "rt", stdin);

    int testCases;
    cin >> testCases;
	li result = 0;

	int n;
	li s;

    forn(tt, testCases)
    {
    	cin >> s >> n;

    	set<li> pos;
    	vector<li> l(n), r(n), c(n);
    	forn(i, n)
    	{
    		cin >> l[i] >> r[i] >> c[i];
    		pos.insert(l[i]);
    		pos.insert(r[i]);
    	}

    	vector<li> x(pos.begin(), pos.end());
    	vector<li> cnt(x.size() - 1);

    	li was = 0;

    	forn(i, n)
    	{
    		int from = lower_bound(x.begin(), x.end(), l[i]) - x.begin();
    		int to = lower_bound(x.begin(), x.end(), r[i]) - x.begin();

    		for (int j = from; j < to; j++)
    			cnt[j] += c[i];

    		was = (was + len(s, r[i] - l[i]) * c[i]) % M;
    		assert(was >= 0);
    	}

    	li now = 0;

    	while (true)
    	{
    		int left = -1;
    		forn(i, cnt.size())
    			if (cnt[i] > 0)
    			{
    				left = i;
    				break;
    			}
    		if (left == -1)
    			break;
    		int right = left;
    		while (right < int(cnt.size()) && cnt[right] > 0)
    			right++;

    		li minv = li(1E18);
    		for (int i = left; i < right; i++)
    			minv = min(minv, cnt[i]);
    		for (int i = left; i < right; i++)
    			cnt[i] -= minv;
    		assert(minv > 0);

    		minv %= M;
    		now = (now + len(s, x[right] - x[left]) * minv) % M;
    		assert(now >= 0);
    	}

    	result = (was - now) % M;
    	result = (result + M) % M;

    	cout << "Case #" << (tt + 1) << ": " << result % M << endl;
    }

    return 0;
}
