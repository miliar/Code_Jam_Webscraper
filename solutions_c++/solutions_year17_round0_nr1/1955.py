#define _USE_MATH_DEFINES
#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <complex>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <numeric>
#include <limits>
#include <climits>
#include <cfloat>
#include <functional>
#include <iterator>
using namespace std;

int solve(const string& s, int k)
{
    int n = s.size();
    string t(n, '+');

    int ans = 0;
    for(int i=0; i<=n-k; ++i){
        if(s[i] != t[i]){
            ++ ans;
            for(int j=0; j<k; ++j)
                t[i+j] = '+' + '-' - t[i+j];
        }
    }

    if(s == t)
        return ans;
    else
        return -1;
}

int main()
{
    int tMax;
    cin >> tMax;

    for(int t=1; t<=tMax; ++t){
        string s;
        int k;
        cin >> s >> k;
        int ans = solve(s, k);

        if(ans == -1)
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;
        else
            cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}
