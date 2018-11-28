/***********************************************
* Author - LUONG VAN DO                        *
*
* Algorithm
* Time Limit
* *********************************************/
#include <iostream>
#include <stdio.h>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <cmath>
#include <math.h>
#include <cstring>
#include <string.h>
#include <stdlib.h>
#include <algorithm>

#define FileIn(file) freopen(file".inp", "r", stdin)
#define FileOut(file) freopen(file".out", "w", stdout)
#define FOR(i,a,b) for (int i=a;i<=b;i++)
#define FORD(i,a,b) for (int i=a;i>=b;i--)
#define REP(i, n) for (int i=0; i<n; i++)
#define fill(ar, val) memset(ar, val, sizeof(ar))
#define pb push_back
#define A first
#define B second
#define PI 3.1415926535897932385
#define uint64 unsigned long long
#define int64 long long
#define INF 500000000
#define N 100000

using namespace std;

inline int max(int a, int b) { return a > b ? a : b; }
inline int min(int a, int b) { return a < b ? a : b; }
inline int gcd(int a, int b) { if (a % b) return gcd(b, a % b); else return b; }
inline int lcm(int a, int b) { return (a * (b / gcd(a, b) )); }

inline int And(int mask, int bit) { return mask & (1 << bit); }
inline int Xor(int mask, int bit) { return mask & (~(1 << bit)); }

typedef pair<string, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
int cases, caseNo = 0;
string s, str;
int ans, n;

string flip(string str, int x)
{
    for (int i = 0;i <= x;i++)
        if (str[i] == '+') str[i] = '-';
        else str[i] = '+';
    for (int i = 0;i <= x / 2;i++)
        swap(str[i], str[x - i]);
    return str;
}
bool check(string str)
{
    for (int i = 0;i < str.size();i++)
        if (str[i] == '-') return false;
    return true;
}
int main() {
    freopen("exam.inp","r",stdin);
    freopen("exam.out","w",stdout);
    scanf(" %d ",&cases);
    while (cases--)
    {
        cin >> s; n = (int)s.size();
        queue <ii> q;
        q.push(ii(s, 0));
        map <string, bool> ha; ha[s] = true;
        while (!q.empty()) {
            ii u = q.front(); q.pop();
            if (check(u.first)) {
                ans = u.second;
                break;
            }
            for (int i = 0;i < n;i++)
            {
                str = flip(u.first, i);
                if (!ha[str]) {
                    ha[str] = true;
                    q.push(ii(str, u.second + 1));
                }
            }
        }
        printf("Case #%d: %d\n", ++caseNo, ans);
    }
    return 0;
}
