#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <algorithm>
#include <iomanip>
#include <queue>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <stack>
#include <bitset>
#include <sstream>
#include <fstream>

typedef unsigned long long ull;
#define mp make_pair
#define pb push_back

const long double eps = 1e-9;
const double pi = acos(-1.0);
const long long inf = 1e18;

using namespace std;

int main (int argc, const char * argv[])
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T;
    string str;
    cin >> T;
    getline(cin, str);
    for (int i = 1; i <= T; ++i)
    {
        int ans = 0;
        getline(cin, str);
        size_t pos = str.find(' ');
        string res = str.substr(pos+1);
        int cur = 0;
        for (int j = 0; j < res.size(); ++j)
        {
            if (cur < j && res[j] != '0')
            {
                ans += j - cur;
                cur += j - cur;
            }
            cur += (res[j]-'0');
        }
        printf("Case #%d: %d\n", i, ans);
    }
    return 0;
}
