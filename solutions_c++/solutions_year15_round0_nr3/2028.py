#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <algorithm>
#include <map>
#include <cmath>
#include <set>
#include <iomanip>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

#define fi first
#define se second
#define mp make_pair
#define pb push_back

const int INF = 1 << 30;
const double EPS = 1e-8;

int sign(int x)
{
    if(x > 0) return 1;
    return (x ? -1 : 0);
}

void solve(int num)
{
    ll l, x;
    cin >> l >> x;
    string ss, s;
    cin >> ss;
    //x = min(x,42LL);
    for(int i=0; i<x; i++) s += ss;
    int n = s.length();
    for(int i=0; i<n; i++) s[i] -= 'i'-2;
    vector<vi> d = {{0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
    map<int,ll> first_pref;
    int first_i = x*l+1, last_k = -1;
    for(int twice=0; twice<2; twice++)
    {
        int cur = 1, sgn = 1;
        for(int i=0; i<n; i++)
        {
            if(twice) cur = sgn*d[s[i]][cur];
            else cur = sgn*d[cur][s[i]];
            if(!first_pref.count(cur)) first_pref[cur] = i;
            sgn = sign(cur);
            cur = abs(cur);
        }
        if(!twice)
        {
            if(first_pref.count(2)) first_i = first_pref[2];
            first_pref.clear();
        }
        reverse(s.begin(), s.end());
    }
    if(first_pref.count(4)) last_k =  n-1-first_pref[4];

    int oks = 0;
    if(first_i+1 < last_k)
    {
        int cur = 1, sgn = 1;
        for(int i=first_i+1; i<last_k; i++)
        {
            cur = sgn*d[cur][s[i]];
            sgn = sign(cur);
            cur = abs(cur);
        }
        if(sgn*cur == 3) oks = 1;
    }


    cout<<"Case #"<<num<<": "<< (oks ? "YES\n" : "NO\n");

}

int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    cin>>t;
    for(int i=1; i<=t; i++)
    {
        solve(i);
    }
}

