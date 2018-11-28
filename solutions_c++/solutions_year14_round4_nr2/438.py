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

int n;
pair<int, int> a[1100];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tn;
    cin >> tn;
    for (int tc = 0; tc < tn; tc++)
    {
    	cin >> n;
    	for (int i = 0; i < n; i++)
    	{
    		cin >> a[i].first;
    		a[i].second = i;
    	}
    	sort(a, a + n);
    	int result = 0;
    	for (int i = 0; i < n; i++)
    	{
    		int l = 0, r = 0;
    		for (int j = i + 1; j < n; j++)
    			if (a[j].second < a[i].second)
    				l++;
    			else
    				r++;
    		result += min(l, r);
    	}
    	cout << "Case #" << tc + 1 << ": " << result << endl;
    }
    return 0;
}