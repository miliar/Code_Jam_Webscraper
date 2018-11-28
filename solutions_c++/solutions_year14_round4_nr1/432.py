#pragma comment (linker, "/STACK:268435456")
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <queue>
#include <cmath>
#include <cctype>
#include <sstream>
#include <ctime>

using namespace std;

set<pair<int, int>, greater<pair<int, int> > > a;
int n, x;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tn;
    cin >> tn;
    for (int tc = 0; tc < tn; tc++)
    {
    	cin >> n >> x;
    	a.clear();
    	for (int i = 0; i < n; i++)
    	{
    		int p;
    		cin >> p;
    		a.insert(make_pair(p, i));
    	}
    	int result = 0;
    	while (a.size() > 1)
    	{
    		int big = a.begin()->first;
    		set<pair<int, int>, greater<pair<int, int> > >::iterator f = a.lower_bound(make_pair(x - big, 1000000));
    		if (f == a.end())
    		{
    			a.erase(*a.begin());
    			result++;
    		}
    		else
    		{
    			if (f == a.begin())
    				f++;
    			result++;
    			a.erase(*a.begin());
    			a.erase(*f);
    		}
    	}
    	cout << "Case #" << tc + 1 << ": " << result + a.size() << endl;
    }
    return 0;
}