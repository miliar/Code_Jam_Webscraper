#define _USE_MATH_DEFINES 
#define _CRT_SECURE_NO_DEPRECATE 
#include <iostream> 
#include <cstdio> 
#include <cstdlib> 
#include <vector> 
#include <sstream> 
#include <string> 
#include <map> 
#include <set> 
#include <algorithm> 
#include <iomanip> 
#include <functional> 
#include <bitset> 
#include <cassert> 
#include <cmath> 
#include <ctime> 
#include <queue> 
#include <list> 
#include <memory.h> 
#include <complex> 
#include <numeric> 
using namespace std; 
#pragma comment(linker, "/STACK:1024000000") 
#define mp make_pair 
#define pb push_back 
#define all(C) (C).begin(), (C).end() 
#define sz(C) (int)(C).size() 
#define PRIME 1103 
#define INF (1 << 29) 
#define MOD 1000000007 
#define FAIL ++*(int*)0 
#define EPS 1e-5 
template<class T> T sqr(T a) {return a * a;} 
typedef long long int64; 
typedef unsigned long long uint64; 
typedef pair<int, int> pii; 
typedef pair<int, pii> piii; 
typedef vector<int> vi; 
typedef vector<int64> vi64; 
typedef vector<pii> vpii; 
typedef vector<vector<int> > vvi; 
typedef vector<vvi> vvvi; 
typedef vector<vector<pair<int, int > > > vvpii; 
typedef vector<vector<vector<pair<int, int > > > > vvvpii; 
typedef complex<long double> cd; 
#define TASK "test" 
//---------------------------------------------------------- 

int q;
string s[100];
int dp[1000][1000];
int n, m;

int f(int i, int j)
{
    if(i == n && j == m)
        return 0;

    if(i == n && s[0][i - 1] == s[1][j])
        return f(i, j + 1) + 1;
    if(j == m && s[1][j - 1] == s[0][i])
        return f(i + 1, j) + 1;

    if(i == n || j == m)
        return INF;

    if(dp[i][j] != -1)
        return dp[i][j];

    int res = INF;

    if(s[0][i] == s[1][j])
        res = min(res, f(i + 1, j + 1));

    if(s[0][i] != s[1][j] && s[1][j - 1] == s[0][i])
        res = min(res, f(i + 1, j) + 1);

    if(s[0][i] != s[1][j] && s[0][i - 1] == s[1][j])
        res = min(res, f(i, j + 1) + 1);

    return dp[i][j] = res;       
}

void solve()
{
    cin >> q;

    bool ok = 1;
    for(int i = 0; i < q; ++i)
    {
        cin >> s[i];
        if(i && s[i][0] != s[i - 1][0])
            ok = 0;
    }

    if(!ok)
    {
        puts("Fegla Won");
        return;
    }
    memset(dp, -1, sizeof dp);

    n = s[0].length();
    m = s[1].length();
    int res = f(1, 1);
    if(res >= INF)
        puts("Fegla Won");
    else 
        cout << res << endl;

    // int res = 0;
    // int i = 0, j = 0;

    // while(i < s[0].length() && j < s[1].length())
    // {
    //     if(s[0][i] == s[1][j])
    //     {
    //         ++i; ++j;
    //         continue;
    //     }

    //     if(s[0][i] == s[1][j - 1])
    //     {
    //         ++res;
    //         ++i;
    //     }
    //     else if(s[0][i - 1] == s[1][j])
    //     {
    //         ++res;
    //         ++j;
    //     }
    //     else break;
    // }

    // if(i == s[0].length() && j == s[1].length())
    // {
    //     cout << res << endl;
    //     return;
    // }

    // while(i != s[0].length() || j != s[1].length())
    // {
    //     if(i != s[0].length())
    //     {
    //         if(s[0][i] != s[1][j - 1])
    //             break;
    //         ++i;
    //         ++res;
    //     }

    //     if(j != s[1].length())
    //     {
    //         if(s[1][j] != s[0][i - 1])
    //             break;
    //         ++i;
    //         ++res;
    //     }
    // }

    // if(i != s[0].length() || j != s[1].length())
    // {
    //     puts("Fegla Won");
    //     return;
    // }

    // cout << res << endl;
}

int main ()
{
    freopen("input.txt", "r", stdin); 
    freopen("output.txt", "w", stdout);

    int test;
    scanf("%d", &test);
    for(int i = 0; i < test; ++i)
    {
        printf("Case #%d: ", i + 1); 
        solve();
        
    }

    return 0;
}
