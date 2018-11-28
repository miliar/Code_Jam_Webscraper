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

using namespace std;

vector<int> getv()
{
	int ch;
	cin >> ch;
	vector<int> result;
	for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
		{
			int cur;
			cin >> cur;
			if (ch - 1 == i)
				result.push_back(cur);
		}
	return result;
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tn;
    cin >> tn;
    for (int tc = 0; tc < tn; tc++)
    {
    	vector<int> a = getv();
    	vector<int> b = getv(); 
    	int m = 0;
    	int g = 0;
    	for (int i = 0; i < 4; i++)
    		for (int j = 0; j < 4; j++)
    			if (a[i] == b[j])
    			{
    				m++;
    				g = a[i];
    			}
    	cout << "Case #" << tc + 1 << ": ";
    	if (m == 0)
    		cout << "Volunteer cheated!";
    	else if (m == 1)
    		cout << g;
    	else
    		cout << "Bad magician!";
    	cout << endl;
    }
    return 0;
}