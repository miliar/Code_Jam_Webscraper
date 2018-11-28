#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <string>
#include <set>
#include <map>
#include <unordered_map>
#include <queue>
#include <deque>
#include <stack>
#include <list>
#include <bitset>
#include <utility>
#include <functional>
#include <string>
#include <algorithm>

#include <cstring>
#include <cstdio>
#include <memory.h>
#include <ctime>
#include <cassert>
#include <cmath>
#include <iomanip>

#define eps e-8

using namespace std;
#define forn(i,n) for(int i = 0; i < int(n); i++)
#define ll long long int
//#define INF 1000000000
int M = 100000000;
ll ar[100000000];
int cnt = 0;

void print(ll x, vector<ll>& v) {
    cnt++;
    string res;
    while(x!=0) {
        if(x&1)
            res+='1';
        else
            res+='0';
        x = x>>1;
    }
    reverse(res.begin(), res.end());
    cout<<res<<res;
    for(int b = 2; b<=10; ++b)
        cout<<" "<<v[b];
    cout<<endl;
}

ll isPrime(ll n) {
    if(n<M && ar[n]!=-2)
    {
        ll p = ar[n];
        return p;
    }

    for(ll i=2;i*i<=n;i++)
        if(n%i==0)
        {
            if(n<M)
                ar[n] = i;
            return i;
        }
    if(n<M)
        ar[n] = -1;
    return -1;
}

bool check(ll x, vector<ll>& out) {
    for(int b = 2; b<=10; ++b) {
        ll real = 0;
        ll cx = x;
        ll st = 1;
        while(cx!=0) {
            if(cx&1) {
                real += st;
            }
            st*=b;
            cx = cx>>1;
        }
        ll res = isPrime(real);
        if(res!=-1)
            out[b]=res;
        else
            return false;
    }
    return true;
}

void solve() {
    cout<<"Case #1:"<<endl;
    for(int i=0; i<M; ++i)
        ar[i]=-2;
    int k = 16;
    vector<ll> v(11);
    for(ll x = 1+(1<<(k-1)); x < (1<<k); x+=2) {
        if(check(x, v))
            print(x, v);
        if(cnt==500) {
            return;
        }
    }
    cout<<cnt<<endl;
}

int main()
{
    /*ll t =1000000000000111L;
    cout<<t<<" "<<t%11<<endl;
    cout<<t%7<<endl;
    ll p = numeric_limits<ll>::max();
    cout<<p<<endl;*/
    cin.sync_with_stdio(false);
    cout.sync_with_stdio(false);
#ifdef diametralis
    freopen("/Users/diametralis/Documents/projects/IO/input.txt", "rt", stdin);
    freopen("/Users/diametralis/Documents/projects/IO/output.txt", "wt", stdout);
#endif
    solve();
#ifdef diametralis
    cerr << "Time == " << clock() << endl;
#endif
}