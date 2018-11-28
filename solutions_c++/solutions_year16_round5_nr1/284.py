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
using namespace std;

int solve(const string& s)
{
    int n = s.size();

    stack<char> stk;
    int ans = n / 2 * 5;
    for(int i=0; i<n; ++i){
        if(!stk.empty() && stk.top() == s[i]){
            ans += 5;
            stk.pop();
        }
        else{
            stk.push(s[i]);
        }
    }
    return ans;
}

int main()
{
    int T;
    cin >> T;

    for(int t=1; t<=T; ++t){
        string s;
        cin >> s;
        int ans = solve(s);
        cout << "Case #" << t << ": " << ans << endl;
    }

    return 0;
}