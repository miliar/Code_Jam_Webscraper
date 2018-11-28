#include <cctype>
#include <iostream>
#include <fstream>
#include <string.h>
#include <algorithm>
#include <vector>
#include <math.h>
#include <cmath>
#include <vector>
#include <queue>
#include <map>
#include <list>
#include <set>
#include <string>
#include <iomanip>
#include <iterator>

#define forn(i, n) for (i64 i = 0; i < n; ++i)
#define revn(i, n) for (i64 i = n-1; i>=0; --i)
#define cyc(i, s, n) for (i64 i = s; i <= n; ++i)
#define pb push_back
#define mp(a,b) make_pair(a,b)
#define all(x) x.begin(), x.end()
#define F first
#define S second
#define eps 1e-7
#define inf 1e15

using namespace std;
typedef unsigned long long u64;
typedef long long i64;
typedef long double ld;
typedef vector < i64 > vi64;
typedef vector < u64 > vu64;
typedef pair < i64, i64 > pi64;
typedef vector < vi64 > graph;
typedef int huint;
#define huint int

//fstream in("input.txt"), out("output.txt", 2);

void testcase(i64 numb)
{
    i64 n;
    cin >> n;
    vi64 v(n+1);
    string s;
    cin >> s;
    cyc(i, 0, n)
        v[i]=s[i]-'0';
    i64 stand = v[0];
    i64 friends = 0;
    cyc(i, 1, n)
    {
        if (stand>=i)
            stand+=v[i];
        else {
            i64 plus;
            plus=i-stand;
            friends+=plus;
            stand+=v[i]+plus;
        }
    }
    cout << endl << "Case #" << numb << ": " << friends;
}

int main()
{
    i64 t;
    cin >> t;
    forn(i, t)
        testcase(i+1);
    return 0;
}




















