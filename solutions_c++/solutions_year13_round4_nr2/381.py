#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

#define PRIME_MAX 100000L

using namespace std;
typedef unsigned int ui;
typedef long long ll;
typedef unsigned long long ull;

int abs(int i)
{
    if(i<0) return -i;
    else return i;
}

ll pow2[51];

ll bestInHalf(ll i)
{
    return (i+1)/2;
}
ll worstInHalf(ll i)
{
    return (i-1)/2;
}
ll best(ll i, ll n)
{
    if(n==0)
        return 0;
    if(i == pow2[n]-1)
        return pow2[n]-1;
    return best(bestInHalf(i), n-1);
}
ll worst(ll i, ll n)
{
    if(n==0)
        return 0;
    if(i==0)
        return 0;
    return pow2[n-1] + worst(worstInHalf(i), n-1);
}

int main()
{
    pow2[0] = 1;
    for(int i=1; i<=50; i++)
    {
        pow2[i] = 2*pow2[i-1];
    }
    int T;
    cin >> T;
    for(int i=1; i<=T; i++)
    {
        ll n, p;
        cin >> n >> p;
        ll minP, maxP;
        // Guaranteed
        ll a, b;
        a = 0; b = pow2[n];
        while(a+1<b)
        {
            //cout << "Binary1" << endl;
            ll w = worst((a+b)/2, n);
            if(w < p)
                a = (a+b)/2;
            else
                b = (a+b)/2;
        }
        minP = a;
        //cout << minP << endl;
        // Hoping
        a = 0; b = pow2[n];
        while(a+1<b)
        {
            //cout << "Binary2" << endl;
            ll bP = best((a+b)/2, n);
            if(bP < p)
                a = (a+b)/2;
            else
                b = (a+b)/2;
        }
        maxP = a;
        printf("Case #%d: %lld %lld\n", i, minP, maxP);
    }
}
