/*
----------------------------------------------------------------------------------------------
------------------------------------SOURAV MANDAL----------------------------------------------
---------------------------COMPUTER SCIENCE AND ENGINEERING------------------------------------
------------------------NATIONAL INSTITUTE OF TECHNOLOGY,RAIPUR--------------------------------
-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------
----PLEASE ENSURE THIS CODE IS NOT COPIED BECAUSE IT MAY LEAD TO BOTH'S DISQUALIFICATION-------
-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------
*/
#include<stdio.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include<string>
#include<cassert>
#include <stdint.h>
#include <math.h>
using namespace std;
#define FOR(i, a, b) for(long long int i = (a); i < (b); ++i)
#define RFOR(i, b, a) for(long long int i = (b) - 1; i >= (a); --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)
#define FILL(A,value) memset(A,value,sizeof(A))

#define ALL(V) V.begin(), V.end()
#define SZ(V) (int)V.size()
#define PB push_back
#define MP make_pair
#define Pi 3.14159265358979
#include <stdio.h>
#include <stdlib.h>
#define LL_MAX 200000000000
#define MOD 1000000007
#define INF 1000000000
#define EPS 1e-14
#define PI 3.14159265358979

#define ll long long int
#define llu long long unsigned
#define ld long

#define mp make_pair
#define pb push_back
#define maX(a,b) ( (a) > (b) ? (a) : (b))
#define miN(a,b) ( (a) < (b) ? (a) : (b))
#define minelt(A) *min_element(b2e(A))
#define maxelt(A) *max_element(b2e(A))

typedef vector<vector<int> > vvi;
typedef vector <ll> vi;
typedef pair <ll, ll> pii;
typedef vector<bool> vb;
typedef vector<vector<bool> > vvb;
typedef vector<string> vs;

//int dx[] = {-1,0,1,0}, dy[] = {0,1,0,-1};
//int dx[] = {1,1,1,0,0,-1,-1,-1}, dy[] = {1,0,-1,1,-1,1,0,-1};
//ll gcd(ll a, ll b) {if (a == 0 || b == 0) return max(a,b); if (b % a == 0) return a; return gcd(b%a, a);}
ll gcd(ll a, ll b){while(b) b ^= a ^= b ^= a %= b;return a;}
#define gc getchar

void fastscan(ll &x)
{
    register ll c = gc();
    x = 0;
    for(;(c<48 || c>57);c = gc());
    for(;c>47 && c<58;c = gc())
     {x = (x<<1) + (x<<3) + c - 48;}
}

int main()
{
freopen( "input.in", "r", stdin );
freopen( "output.out", "w", stdout );

ll tests;
fastscan(tests);
FOR(j,0,tests)
{
    ll n;
    fastscan(n);
    string a;
    cin>>a;
    ll ans = 0;
    ll q = 0;
    q = q+(a[0]-'0');
    //printf("q:%d\n",q);
    FOR(i,1,n+1)
    {
        ll  x = a[i]-'0';
        if(q<i&&x!=0)
        {
            ans += (i-q);
           // printf("ans:%d\n",ans);
            q = q+ans;
          // printf("if q:%d\n",q);
        }

       q = q+x;
      // printf("q+x:%d\n",q);
    }
    printf("Case #%lld: %lld\n",j+1,ans);
}
return 0;
}
