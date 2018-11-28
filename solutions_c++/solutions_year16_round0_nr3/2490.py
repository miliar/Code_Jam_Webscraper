/* ***************************
Author: Abhay Mangal (abhay26)
*************************** */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <numeric>
#include <utility>
#include <bitset>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
using namespace std;
 #define tr(container, it) \
    for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define maX(a,b) (a) > (b) ? (a) : (b)
#define pii pair< int, int >
#define pip pair< int, pii >
#define pll pair < ll, ll >
#define pill pair< int, pll >
#define FOR(i,n) for(int i=0; i<(int)n ;i++)
#define REP(i,a,n) for(int i=a;i<(int)n;i++)
#define pb push_back
#define mp make_pair
typedef long long ll;
ll mpow(ll x, ll n){
    if(n == 0)
        return 1;
    ll ans = 1;
    for(int i=0;i<n;i++)
    {
        ans = ans*x;
    }
    return ans;
}
bool isprime(ll num) {
    if (num <= 3) {
        return num > 1;
    } else if (num % 2 == 0 || num % 3 == 0) {
        return false;
    } else {
        for (int i = 5; i * i <= num; i += 6) {
            if (num % i == 0 || num % (i + 2) == 0) {
                return false;
            }
        }
        return true;
    }
}
ll factor(ll num){
    for(ll i=2;i<=sqrt(num);i++)
    {
        if(num % i == 0)
            return i;
    }
    return -1;
}
int main()
{
    int J = 90;
    int n = 16;
    printf("Case #1:\n");
    int tmp = 0;
    tmp |= 1<<0;
    tmp |= 1<<(n-1);
    int cnt = 0;
    for(ll i=0;i<(1<<(n-2));i++)
    {
      //  cout << i << endl;
        string s = "";
            for(ll j=0;j<(n-2);j++)
            {
                if((i & (1<<j)) != 0)
                {
                    s = "1"+s;
                }
                else
                    s = "0"+s;
            }
            s = "1"+s+"1";
        int flag = 1;
        for(ll k = 2;k<=10;k++)
        {
            ll x = mpow(k,0) + mpow(k,(n-1));
            for(ll j=0;j<(n-2);j++)
            {
                if((i & (1<<j)) != 0)
                    x += mpow(k,j+1);
            }
           // cout << s << " " << k << " " << x << " " << mpow(k,0) + mpow(k,(n-2)) <<endl;
            if(isprime(x)){
                flag = 0;
                break;
            }
        }
        if(flag)
        {
            cnt++;
            string s = "";
            for(int j=0;j<(n-2);j++)
            {
                if((i & (1<<j)) != 0)
                {
                    s = "1"+s;
                }
                else
                    s = "0"+s;
            }
            s = "1"+s+"1";
            cout << s << " ";
            for(ll k = 2;k<=10;k++)
            {
                ll x = mpow(k,0) + mpow(k,(n-1));

                for(ll j=0;j<(n-2);j++)
                {
                    if((i & (1<<j)) != 0)
                        x += mpow(k,j+1);
                }
               // cout << i << " " << k << " " << x << endl;
                cout << factor(x) << " ";
            }
            cout << endl;
            if(cnt >= J)
                break;
        }
    }
    return 0;
}
