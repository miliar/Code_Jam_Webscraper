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
    	string s;
    	int n, k;
    	cin >> s >> k;
    	n = s.length();
    	int p = 0;
    	for (int i = 0; i < n - k + 1; i++)
    		if (s[i] == '-')
    		{
    			for (int j = i; j < i + k; j++)
    				s[j] = s[j] == '-' ? '+' : '-';
    			p++;
    		}
    	if (s.find('-') + 1)
    		cout << "Case #" << tc + 1 << ": IMPOSSIBLE" << endl;
    	else
    		cout << "Case #" << tc + 1 << ": " << p << endl;
    }
    return 0;
}