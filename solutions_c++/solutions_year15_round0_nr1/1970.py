#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;

const int MAX = 1001000;
const int MAXC = 15;
const int INF = 1e9;
const int MOD = 1000000007;
const double EPS = 1e-11;

string st;
int n;
int mx()
{
    int crnt = 0;
    int out = 0;
    for(int i = 0; i <= n; ++i)
    {
        int s = (int)(st[i] - '0');
        if(crnt < i)
        {
            out += (i - crnt);
            crnt = i;
        }
        crnt += s;
    }
    return out;
}

int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i)
    {
        cin >> n >> st;
        int answ = mx();
        cout << "Case #" << i << ": " << answ << '\n';
    }
}
