#include <bits/stdc++.h>
using namespace std;
int main () {
    ios :: sync_with_stdio (false);
    cin.tie (0);
    freopen("C:\\Users\\wego\\Downloads\\A-large.in", "r", stdin);
    freopen("C:\\Users\\wego\\Downloads\\output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
    	int g;
    	cin >> g;
    	int s [1001];
    	for (int j = 1; j <= g; ++j)
    		cin >> s [j];
    	int m1a = 0;
    	int v = 0;
    	for (int j = 1; j < g; ++j)
    	    if (s [j] > s [j + 1]) {
    	        m1a += s [j] - s [j + 1];
    	        v = max (v, s [j] - s [j + 1]);
    	    }
        int m2a = 0;
		for (int j = 1; j < g; ++j)
		    m2a += min (s [j], v);
		cout << "Case #" << i << ": " << m1a << ' ' << m2a << endl;    	    
    }
    return 0;
}

