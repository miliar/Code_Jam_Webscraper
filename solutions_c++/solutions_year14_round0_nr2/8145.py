//#include<bits/stdc++.h>
#include <cstdio>
#include <sstream>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <iostream>
#include <fstream>
#include <numeric>
#include <string>
#include <vector>
#include <cstring>
#include <map>
#include <iterator>

#define pb push_back
#define mp make_pair
#define ins insert
#define fi first
#define se second
#define ll long long int
#define sss stringstream
#define oss ostringstream
#define iss istringstream
#define llu long long unsigned

#define _sq(a) (a)*(a)
#define gcd(a,b)    __gcd(a,b)
#define lcm(a,b) ((a)*((b)/gcd(a,b)))
#define mem(a) memset(a, 0, sizeof(a))
#define _set(a) memset(a,-1,sizeof(a))
#define popcount(n) __builtin_popcount(n)
#define popcountl(n) __builtin_popcountll(n)
#define ctz(x) __builtin_ctz(x) //number of trailing zeroes in a digit
#define ctzl(x) __builtin_ctzll(x)
#define clz(x) __builtin_clz(n)
#define clzl(x) __builtin_clzll(x) //number of leading zeroes in a digit
//If Long Long (mask & (1LL << k))
#define check(mask, k) (mask & (1 << k))
#define set1(mask, k) (mask | (1 << k))
#define set0(mask ,k) (mask & (~(1<<k)))
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

using namespace std;
#define pi acos(-1.0)
#define mod 100000007
#define inf 1000000000
#define EPS 1e-9
#define MAX 100005
//int dx[] = {0,0,1,-1};
//int dy[] = {1,-1,0,0};
//int dx[] = {-1,-1,-1,0,0,1,1,1};
//int dy[] = {-1,0,1,-1,1,-1,0,1};
//typedef pair < int, int > pii;
int main()
{
    READ("B-large.in");
    WRITE("outputBlarge.txt");
    //ios_base::sync_with_stdio(false);
    int tcase, ncase;
    double c, f, x, ans, ans1, t, f1;
    scanf("%d", &ncase);
    for(tcase = 1; tcase <= ncase; tcase++)
    {
        scanf("%lf %lf %lf", &c, &f, &x);
        ans = x / 2.0;
        f1 = 2.0;
        t = (c / f1);
        ans1  = t + (x / (f1 + f));
        while(ans >= ans1 + EPS)
        {
            ans = ans1;
            f1 += f;
            t += (c / f1);
            ans1 = t + (x / (f1 + f));
        }
        printf("Case #%d: %.7lf\n", tcase, ans);
    }
    return 0;
}


