#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <memory.h>
#include <numeric>
#include <assert.h>

using namespace std;

#define pb push_back
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++) 
#define REP(i,n) FOR(i,0,n)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define CL(a,v) memset((a),(v),sizeof(a))
#define mp make_pair
#define X first
#define Y second 
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c)) 

typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> VI; 



void print_v(vector<string> v) {
    REP(i,v.size()) cout<<v[i]<<" ";
    cout<<endl; 
}


ll gcd (ll a, ll b) {
    while (b) {
        a %= b;
        swap (a, b);
    }
    return a;
}

ll is2pow(ll b) {
    while(b) {
        if (b==1) return true;
        if (b%2 == 1) return false;
        b = b/2;
    }
    return true;
}

ll calc(string s) {
    REP(i, s.size()) {
        if (s[i] == '/') s[i] = ' ';
    }
    ll a, b;
    istringstream iss(s);
    iss>>a>>b;
    ll c = gcd(a,b);
    a = a/c; 
    b = b/c;
    if (a == 0) return -1;
    if (is2pow(b) == false) return -1;
    //cout<<a<<' '<<b<<endl;

    int res = 0; 
    while(b) {
        res ++ ;
        if (res>40) return -1; 
        b = b/2;
        if (a>=b) return res;
    }
    return -1;
}


int main()
{
    
#ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif

    int T; cin>>T;
    int n, l;

    REP(t,T) {
        string s;
        cin>>s;

        ll res = calc(s);

        cout<<"Case #"<<t+1;
        if (res>-1) {
            cout<<": "<<res<<endl;
        } else {
            cout<<": impossible"<<endl;
        }
    }
    return 0;
}
