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
typedef std::vector<double> vd;
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
        int n;
        vi d2 = {1,2,4,8,16};
bool valid(vi ab) {
    vi u;
    forn(i,0,n) u.pb(i);
    do{
        if(ab[u[0]] == 0) return false;
        forn(a0, 0, n) {
            if(n<=1) continue;
            if(!(ab[u[0]] & d2[a0])) continue;
            if(ab[u[1]] == d2[a0]) return false;
            forn(a1,0,n) {
                if(a1==a0) continue;
                if(n<=2) continue;
                if(!(ab[u[1]] & d2[a1])) continue;
                if(ab[u[2]] == (d2[a0]|d2[a1])) return false;
                forn(a2,0,n) {
                    if(a2==a1) continue;
                    if(a2==a0) continue;
                    if(n<=3) continue;
                    if(!(ab[u[2]] & d2[a2])) continue;
                    if(ab[u[3]] == (d2[a0]|d2[a1]|d2[a2])) return false;
                }
            }
        }
    } while(next_permutation(all(u)));
    return true;
}


int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
    int t;
    cin>>t;
    forn(lk, 0 ,t) {
        cout<<"Case #" << lk+1 << ": ";

        cin>>n;

        vi n1 = {0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1};
        vector<string> pr;
        forn(i,0,16) {
            pr.pb(string());
            int l = i;
            forn(j,0,4) pr.back().pb('0' + l%2);
            l/=2;
        }
        vi ab(n,0);
        forn(i,0,n) {
            string s;
            cin>>s;
            forn(j,0,n) if(s[j] == '1') ab[i] |= d2[j];
        }
        int ans = 16;
        vi t(4);
        for(t[0] = 0; t[0]<d2[n]; t[0]++)
        for(t[1] = 0; t[1]<d2[n]; t[1]++)
        for(t[2] = 0; t[2]<d2[n]; t[2]++)
        for(t[3] = 0; t[3]<d2[n]; t[3]++) {
            bool f = true;
            vi ab2(4, 0);
            forn(i,0,n) ab2[i] = ab[i]|t[i];
            
            if(valid(ab2)) ans = min(ans, n1[t[0]]+n1[t[1]]+n1[t[2]]+n1[t[3]]);
            if(ans == 2) {
                int x = 149 -14;
            }
        }
        cout<<ans<<endl;
    }
    
}


