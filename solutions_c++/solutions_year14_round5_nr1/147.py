#pragma comment(linker, "/STACK:512000000")
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <sstream>

using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define for1(i, n) for (int i = 1; i <= int(n); i++)
#define forv(i, v) forn(i, v.size())

#define all(x) x.begin(), x.end()
#define pb push_back
#define mp make_pair

#define CIN_FILE "input.txt"
#define COUT_FILE "output.txt"

typedef long double ld;
typedef long long ll;
typedef pair<int, int> pii;

const int NMAX = 1000006;

int a[NMAX];
ll sum[NMAX];

void solve(int test)
{
    printf("Case #%d: ", test);

    int n, p, q, r, s;
    scanf("%d %d %d %d %d\n", &n, &p, &q, &r, &s);

    sum[0] = 0;
    forn(i, n)
    {
        a[i] = (ll(i) * p + q) % r + s;        
        sum[i + 1] = sum[i] + a[i];
    }

    int j = 0;
    ll res = sum[n];

    forn(i, n)
    {
        if (j < i) j++;

        res = min(res, max(sum[i], max(sum[j] - sum[i], sum[n] - sum[j])));
         
        while (j < n && sum[j] - sum[i] < sum[n] - sum[j])
        {
            j++;
            res = min(res, max(sum[i], max(sum[j] - sum[i], sum[n] - sum[j])));
        }            
        j--;
    }

    res = sum[n] - res;
    printf("%.10lf\n", double(res) / sum[n]);
}
int main()
{
    freopen(CIN_FILE, "rt", stdin);
    freopen(COUT_FILE, "wt", stdout);

    int tc;
    scanf("%d\n", &tc);
    forn(it, tc) solve(it + 1);
    
    return 0;
}
