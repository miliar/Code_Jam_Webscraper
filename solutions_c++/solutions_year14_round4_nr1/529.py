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

const int maxn = 10010;

int s[maxn];

int main()
{
    int T;
    cin >> T;
    for (int sc = 0; sc < T; sc++) {
        int n, x;
        cin >> n >> x;
        for (int i = 0; i < n; i++) {
            cin >> s[i];
        }
        sort(s + 0, s + n);
        int l = 0, r = n-1;
        int ans = 0;
        while (l <= r) {
            if (l < r && s[l] + s[r] <= x) {
                ans++;
                l++; r--;
            } else {
                ans++;
                r--;
            }
        }
         
        cout << "Case #" << sc+1 << ": ";
        cout << ans;
        cout << endl;
    }
    
    return 0;
}
