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
    	int m;
    	string s;
    	cin >> m >> s;
    	vector<int> a;
    	for (int i = 0; i <= m; i++)
    		for (int j = 0; j < s[i] - '0'; j++)
    			a.push_back(i);
    	int result = 0;
    	for (int i = 0; i < a.size(); i++)
    		result = max(result, a[i] - i);
    	cout << "Case #" << tc + 1 << ": " << result << endl;
    }
    return 0;
}