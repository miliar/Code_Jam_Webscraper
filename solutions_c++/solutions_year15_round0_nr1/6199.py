#define ACTIVE
#ifdef ACTIVE
//#define SUBMIT

#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <climits>
#include <cassert>
#include <sstream>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>
#include <ctime>
#include <set>
#include <map>

using namespace std;

#define IFILE "/Users/nikitatarasov/Downloads/A-large.in"
#define OFILE "/Users/nikitatarasov/Downloads/A-large.out"
//#define SUBMIT

int main()
{
#ifdef SUBMIT
    freopen(IFILE, "r", stdin);
    freopen(OFILE, "w", stdout);
#endif
    
    int t;
    cin >> t;
    
    for (int c = 0; c < t; ++c)
    {
        int len;
        string str;
        cin >> len >> str;
        int ans = 0, prefsum = 0;
        for (int i = 0; i <= len; ++i)
        {
            if(prefsum >= i)
                prefsum += str[i]-'0';
            else
            {
                ans += i - prefsum;
                prefsum = i + str[i]-'0';
            }
        }
        cout << "Case #" << c+1 << ": " << ans << endl;
    }
}
#endif