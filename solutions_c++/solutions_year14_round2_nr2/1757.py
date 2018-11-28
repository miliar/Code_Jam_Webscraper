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
#define INF 1e20 
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

int64 solve()
{
    int a, b, k;
    scanf("%d%d%d", &a, &b, &k);

    int64 res = 0;
    for(int i = 0; i < a; ++i)
    {
        for(int j = 0; j < b; ++j)
        {
            if((i & j) < k)
                ++res;
        }
    }

    return res;
}

int main ()
{
    freopen("input.txt", "r", stdin); 
    freopen("output.txt", "w", stdout);

    int test;
    scanf("%d", &test);
    for(int i = 0; i < test; ++i)
    {
        int64 res = solve();
        printf("Case #%d: %lld\n", i + 1, res); 
    }

    return 0;
}
