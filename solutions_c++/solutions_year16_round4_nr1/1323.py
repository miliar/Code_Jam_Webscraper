#include <cstdlib>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <deque>
#include <iomanip>
#include <iostream>
#include <list>
#include <numeric>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>

using namespace std;

#define sz(X) ((int)(X).size())
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define all(X) (X).begin(),(X).end()
#define FOR(i, a, n) for(int i=(a), __ ## i=(n); i<__ ## i; i++)
#define REP(I,N) FOR(I,0,N)
#define PR(X) cout<<#X<<" = "<<(X)<<" "
#define PRL cout<<endl
#define PRV(X) {cout<<#X<<" = {";REP(__prv,sz(X)-1)cout<<(X)[__prv]<<",";if(sz(X))cout<<*(X).end();cout<<"}"<<endl;}

template<class T1, class T2> ostream &operator<<(ostream &os, const pair<T1, T2> &par);

template<class T> ostream &operator<<(ostream &os, const vector<T> &vec)
{
    os << '{';
    bool first = true;
    for (const auto & x : vec)
    {
        if (!first)
            os << ',';
        first = false;
        os << x;
    }
    os << '}';
    return os;
}

template<class K, class V> ostream &operator<<(ostream &os, const unordered_map<K, V> &vec)
{
    os << '{';
    bool first = true;
    for (const auto & x : vec)
    {
        if (!first)
            os << ',';
        first = false;
        os << x.X << ':' << x.Y;
    }
    os << '}';
    return os;
}

template<class T> ostream &operator<<(ostream &os, const unordered_set<T> &vec)
{
    return os << vector<T>(all(vec));
}

template<class T1, class T2> ostream &operator<<(ostream &os, const pair<T1, T2> &par)
{
    os << '(' << par.X << ',' << par.Y << ')';
    return os;
}

typedef long long lint;
typedef vector<int> VI;
typedef pair<int, int> PII;

int gcd(int x, int y)
{
    return y ? gcd(y, x % y) : abs(x);
}

template<class T> T sqr(T x)
{
    return x * x;
}

void solve(int test)
{
    int n, r, p, s;
    cin >> n >> r >> p >> s;
    vector<string> a = {"P", "R", "S"};
    REP(i, n)
    	a = {a[0] + a[1], a[0] + a[2], a[1] + a[2]};
    int ans = -1;
    REP (i, sz(a))
    	if (count(all(a[i]), 'P') == p && count(all(a[i]), 'R') == r && count(all(a[i]), 'S') == s)
    		ans = i;
    cout << "Case #" << test << ":";
    cout << fixed;
    cout << setprecision(8);
    cout << " ";
    if (ans == -1)
    	cout << "IMPOSSIBLE";
    else
    	cout << a[ans];
    cout << endl;
}

void pre()
{
}

int main()
{
    if (!freopen("1.in", "r", stdin))
    {
        cerr << "No input file" << endl;
        return 1;
    }
    if (!freopen("1.out", "w", stdout))
    {
        cerr << "Error creating output file" << endl;
        return 1;
    }
	ios::sync_with_stdio(false);
    pre();
    int n;
    cin >> n;
    string tmp;
    getline(cin, tmp);
    for (int i = 1; i <= n; ++i)
    {
        solve(i);
    }
    return 0;
}
