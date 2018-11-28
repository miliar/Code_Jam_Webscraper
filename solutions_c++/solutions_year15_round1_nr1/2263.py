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
#define MAXN 1010

const long double eps = 1e-9;
const double pi = acos(-1.0);
const long long inf = 1e18;
const int inf2 = 1000*1000*1000;
using namespace std;

long long n;
int t;
int main (int argc, const char * argv[])
{
    ios_base::sync_with_stdio(false);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> t;
    for (int k = 1; k <= t; ++k)
    {cin >> n;
    vector<int> v(n);
    for (int i = 0; i < n; ++i)
        cin >> v[i];
    long long ans1 = 0;
    for (int i = 1; i < n; ++i)
    {
        if (v[i] < v[i-1])
            ans1 += v[i-1] - v[i];
    }
    long long ans2 = 0;
    int speed = 0;
    for (int i = 1; i < n; ++i)
        if (v[i] < v[i-1] && speed < v[i-1]-v[i])
            speed = v[i-1]-v[i];
    for (int i = 0; i < n-1; ++i)
        if (v[i] <= speed)
            ans2 += v[i];
        else
        {
            ans2 += speed;
        }
    cout << "Case #" << k << ": " << ans1 << " " << ans2 << endl;}
    return 0;
}
