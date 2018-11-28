#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <ctype.h>
#include <deque>
#include <queue>
#include <cstring>
#include <set>
#include <list>
#include <map>
#include <unordered_map>
#include <stdio.h>

using namespace std;

typedef long long ll;
typedef std::vector<int> vi;
typedef std::vector<bool> vb;
typedef std::vector<string> vs;
typedef std::vector<long double> vd;
typedef std::vector<long long> vll;
typedef std::vector<std::vector<int> > vvi;
typedef vector<vvi> vvvi;
typedef vector<vll> vvll;
typedef std::vector<std::pair<int, int> > vpi;
typedef vector<vpi> vvpi;
typedef std::pair<int, int> pi;
typedef std::pair<ll, ll> pll;
typedef std::vector<pll> vpll;

const long long mod = 1000000007;

#define all(c) (c).begin(),(c).end()
#define sz(c) (int)(c).size()
#define forn(i, a, b) for(int i = a; i < b; i++)

#define pb push_back
#define mp make_pair

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
    int t;
    cin>>t;
    forn(iaff,0,t) {
        cout<<"Case #"<<iaff+1<<": ";
        int n,k;
        cin>>n>>k;
        vd p(n);
        forn(i,0,n) cin>>p[i];
        sort(all(p));
        long double ans = 0;
        forn(i, 0, k+1) {
            vd prob;
            forn(j,0,i) prob.pb(p[j]);
            forn(j, n-k+i, n) prob.pb(p[j]);
            vd d(k+1, 0);
            d[0] = 1;
            forn(s, 0,k) {
                vd d2(k+1, 0);
                forn(j,0,k-1) d2[j+1] = d[j]*prob[s];
                forn(j,0,k) d2[j] += d[j] * (1-prob[s]);
                d = d2;
            }
            ans = max(ans, d[k/2]);
        }
        printf("%.10lf\n", (double)ans);
    }
    
}


