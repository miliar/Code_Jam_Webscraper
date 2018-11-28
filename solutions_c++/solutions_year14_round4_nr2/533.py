#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include <cctype>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <set>
#include <queue>

using namespace std;

int main()
{
    int T;
    cin >> T;
    
    for (int sc = 0; sc < T; sc++) {
        int i, j, k, n;
        cin >> n;
        vector<int> a;
        for (i = 0; i < n; i++) {
            cin >> k;
            a.push_back(k);
        }
        int ans = 0;
        for (i = 0; i < n; i++) {
            int m = 0;
            for (j = 1; j < a.size(); j++) {
                if (a[j] < a[m]) m = j;
            }
            int swaps = m;
            if (a.size() - m - 1 < swaps) 
                swaps = a.size() - m - 1;
            ans += swaps;
            a.erase(a.begin() + m);
        }

        cout << "Case #" << sc+1 << ": ";
        cout << ans;
        cout << endl;
    }
    
    return 0;
}
