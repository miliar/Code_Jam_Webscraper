#include <algorithm>
#include <assert.h>
#include <climits> 
#include <cmath>
#include <cstdio>
#include <fstream>
#include <iostream>
#include <map>
#include <memory.h>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>

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


ll solve1(ll r, ll c , ll n) {
    
    n -= r*c/2;

    if (n<=0) return 0;

    if (r*c%2 && n == 1) return 0;

    if (r*c%2 == 0) {
        return 2*(n-1) + 1;
    }
    if (n<=2) return n;
    return 2*(n-2) + 2; 
}

ll solve2(ll r, ll c , ll n) {
    return 0;
}

ll solve3(ll r, ll c , ll n) {
    ll cost = 0;
    ll p1 = r*c/2+1;
    n -= p1;
    if (n>=0) {
        ll cc = 0;
        cc = min((r/2 + c/2)*2, n);
        cost += cc*3;
        n -=cc;
        if (n>=0) {
            cost += n * 4;
        }
    }
    return cost;
}

ll solve(ll r, ll c , ll n) {
    if (r==1 || c==1) {
        return solve1(r,c,n);
    }   
    // if (r==2 || c==2) {
    //     return solve2(r,c,n);
    // }
    ll res2 = r*c*4;
    if (r*c%2) res2 = solve3( r,  c ,  n);
    ll cost = 0;
    ll p1 = r*c/2;
    if (r*c%2 && (n-p1)==1) p1 ++ ;
    n -= p1;
    //cout<<"p1: "<<p1<<endl;
    if (n>=0) {
        ll cc = 0;
        ll red = 0;
        if (r*c%2 == 0) {
            cc = min(n, 2LL);

        } else {
            cc = min(n, 4LL);
        }
        red = cc;
        //cout<<"cc2: "<<cc<<endl;
        cost += cc*2;
        //cout<<"cost: "<<cost<<endl;
        n -= cc;
        if (n>=0) {
            if (r%2 == 0 && c%2 == 0) {
                cc = min((r/2 + c/2)*2 -2-red, n);
            }
            else {
                if (r*c%2 ==0) {
                    cc = min((r/2 + c/2)*2 -1-red, n);
                } else {
                    cc = min((r/2 + c/2)*2-red, n);
                }
            }
            
            cost += cc*3;
            n -=cc;
        }
        //cout<<"cc3: "<<cc<<endl;
        //cout<<"cost: "<<cost<<endl;
        if (n>=0) {
            cost += n * 4;
        }
        //cout<<"cc4: "<<n<<endl;
        //cout<<"cost: "<<cost<<endl;
    }
    return min(res2, cost);
}


vector<int> v;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

bool ok(int x, int y, int r, int c) {
    if (x <r && x>=0 && y<c && y>=0 && v[x*c+y] == 1) return true;
    return false;
}
int brute(int r, int c, int n) {
    v.clear();   
    REP(i,r*c-n) v.push_back(0);
    REP(i, n) v.push_back(1);
    int res = r*c*4;
    do {
        int t = 0;
        // REP(i,v.size()) {
        //     cout<<v[i]<<" ";
        // }
        // cout<<endl;
        
        REP(x,r) {
            REP(y,c) {

                int tt= 0;
                if (v[x*c+y]) {
                    REP(i,4) {
                        int nx = x + dx[i];
                        int ny = y + dy[i];
                        if (ok(nx,ny,r,c)) tt++;
                    }
                }
                //cout<<x<<" "<<y<<" "<<v[x*c+y]<<" "<<tt<<endl;
                t+=tt;
            }
        }
        //cout<<t<<endl;
        res = min(res, t);
    } while(next_permutation(v.begin(), v.end()));
    return res/2;
}

int main(int argc, char const *argv[]) {

    freopen("input.txt","r", stdin);
    freopen("b_large.txt","w",stdout);

    int T; cin>>T;

    REP(t,T) {
        ll r,c,n; cin>>r>>c>>n;
        ll res1 = solve(r,c,n);
        //ll res2 = brute(r,c,n);
        // if (res1!=res2) {
        //     cout<<"Mismatch: "<< res1<<" "<<res2<<endl;
        //     cout<<r<<" "<<c<<" "<<n<<endl;
        // }
        cout<<"Case #"<<t+1<<": "<<res1<<endl;
    }

    return 0;
}