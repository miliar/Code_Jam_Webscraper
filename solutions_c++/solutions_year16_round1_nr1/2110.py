#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cfloat>
#include <climits>
#include <cstring>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#define ARBLIMIT 1000
using namespace std;

int main()
{
    int T, n;
    cin >> T;
    for(int t=1; t <= T; ++t)
    {
        string s, z;
        cin >> s;
        n = s.size();
        for(int i=0; i < n; ++i)
        {
            if(s[i] < z[0])
            {
                z.push_back(s[i]);
            }
            else
            {
                reverse(z.begin(), z.end());
                z.push_back(s[i]);
                reverse(z.begin(), z.end());
            }
        }
        cout << "Case #" << t << ": " << z << endl;
    }

    return 0;
}
