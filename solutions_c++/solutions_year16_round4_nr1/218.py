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

string build(char win, int n) {
    if(n==0) return string(1, win);
    if(win=='R') {
        string t1 = build('R', n-1);
        string t2 = build('S', n-1);
        if(t1<t2) return t1+t2;
        else return t2+t1;
    }
    if(win=='S') {
        string t1 = build('P', n-1);
        string t2 = build('S', n-1);
        if(t1<t2) return t1+t2;
        else return t2+t1;
    }
    if(win=='P') {
        string t1 = build('R', n-1);
        string t2 = build('P', n-1);
        if(t1<t2) return t1+t2;
        else return t2+t1;
    }
    return "";
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
#endif
//    vi a(3, 0);
//    a[0]=1;
//    forn(i,0,10) {
//        vi b(3);
//        b[0] = a[0] + a[2];
//        b[1] = a[0] + a[1];
//        b[2] = a[1] + a[2];
//        a = b;
//        forn(i,0,3) cout<<a[i]<<" ";
//        cout<<endl;
//    }
//    forn(i,0,3) cout<<a[i]<<" ";
    int t;
    cin>>t;
    forn(afiaf,0,t) {
        cout<<"Case #" << afiaf+1<<": ";
        vi a(3);
        int n;
        cin>>n>>a[0]>>a[1]>>a[2];
        vi b = a;
        sort(all(b));
        if(b[2]-b[0] > 1) cout<<"IMPOSSIBLE\n";
        else {
            forn(st,0,3) {
                vi at(3, 0);
                at[st] = 1;
                forn(i,0,n) {
                    vi b(3);
                    b[0] = at[0] + at[1];
                    b[1] = at[2] + at[1];
                    b[2] = at[0] + at[2];
                    at = b;
                }
                if (at==a) {
                    if(st == 0) cout<<build('R', n);
                    if(st == 1) cout<<build('P', n);
                    if(st == 2) cout<<build('S', n);
                    cout<<"\n";
//                    string d;
//                    if(st == 0) d= "R";
//                    if(st == 1) d= "P";
//                    if(st == 2) d= "S";
//                    forn(i,0,n) {
//                        string nd;
//                        for(auto c : d) {
//                            if(c=='R') nd = nd+"RS";
//                            if(c=='P') nd = nd+"PR";
//                            if(c=='S') nd=nd + "PS";
//                        }
//                        d=nd;
//                    }
//                    vector<string> ans;
//                    forn(i,0,d.size()/2) {
//                        ans.pb("");
//                        ans.back().pb(d[2*i]);
//                        ans.back().pb(d[2*i+1]);
//                    }
//                    sort(all(ans));
//                    for(auto u : ans) cout<<u;
//                    cout<<endl;
//                    break;
                }
                
            }
        }
    }
}


