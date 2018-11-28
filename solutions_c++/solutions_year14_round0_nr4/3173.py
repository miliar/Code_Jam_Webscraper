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

const int maxn = 1100;

double a[maxn];
double b[maxn];
int n;

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
    		cin >> a[i];
    	for (int i = 0; i < n; i++)
    		cin >> b[i];
    	sort(a, a + n);
    	sort(b, b + n);
    	int dw = 0;
    	for (int i = 0; i <= n; i++)
    	{
    		int fail = 0;
    		for (int j = 0; j < i; j++)
    			fail |= b[j] > a[n - i + j];
    		if (!fail)
    			dw = i;
    	}
    	vector<bool> used(n);
    	int w = 0;
    	for (int i = 0; i < n; i++)
    	{
    		int fail = 1;
    		for (int j = 0; j < n; j++)
    			if (!used[j] && b[j] > a[i])
    			{
    				used[j] = 1;
    				fail = 0;
    				break;
    			}
    		w += fail;
    	}
    	cout << "Case #" << tc + 1 << ": " << dw << " " << w << endl;
    }    
    return 0;
}