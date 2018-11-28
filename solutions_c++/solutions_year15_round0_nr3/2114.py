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

int mult(int a, int b) {
    if ( a == 1 && b == 1) return 1;
    if ( a == 1 && b == 2) return 2;
    if ( a == 1 && b == 3) return 3;
    if ( a == 1 && b == 4) return 4;
    if ( a == 2 && b == 1) return 2;
    if ( a == 2 && b == 2) return -1;
    if ( a == 2 && b == 3) return 4;
    if ( a == 2 && b == 4) return -3;
    if ( a == 3 && b == 1) return 3;
    if ( a == 3 && b == 2) return -4;
    if ( a == 3 && b == 3) return -1;
    if ( a == 3 && b == 4) return 2;
    if ( a == 4 && b == 1) return 4;
    if ( a == 4 && b == 2) return 3;
    if ( a == 4 && b == 3) return -2;
    if ( a == 4 && b == 4) return -1;
    //cout<<"Warning"<<endl;
    return 0;
}

map<pair<int,int>, int> h;

int calc(vector<int> &v, int l, int r) {
    auto p = make_pair(l,r);
    if (h.count(p)) return h[p];
    int res = v[l];
    //cout<<res<<endl;
    FOR(i,l+1,r+1) {
        int m = 1;
        if (res<0) m = -1;
        res = m * mult(abs(res), v[i]);
        //cout<<res<<endl;
    }
    h[p] = res;
    return res;
}

int main(int argc, char const *argv[]) {

    #ifndef ONLINE_JUDGE
    freopen("input.txt","r", stdin);
    freopen("output_c_small.txt","w",stdout);
    #endif

    int T; cin>>T;

    REP(t,T) {
        h.clear();
        int x,l; string s;
        cin>>x>>l>>s;
        vector<int> v;
        REP(i,l) {
            REP(j, s.size()) {
                if (s[j] == 'i') v.push_back(2);
                if (s[j] == 'j') v.push_back(3);
                if (s[j] == 'k') v.push_back(4);
            }
        }
        int n = v.size();
        if (n<3) {
            cout<<"Case #"<<t+1<<": NO"<<endl;
            continue;
        }
        int found = false;
        // REP(i,n) {
        //     cout<<v[i]<< " ";
        // }
        //cout<<endl;
        // int res1 = calc(v,0, 2);
        // int res2 = calc(v,3, 5);
        // int res3 = calc(v,6, 11);
        // cout<<res1<<" "<<res2<<" "<<res3<<endl;
        vector<int> p1(n), p2(n);
        int v1 = 1 , v2 =1;
        REP(i,n) {
            int m = 1;
            if (v1<0) m = -1;
            v1 = m * mult(abs(v1), v[i]);
            p1[i] = v1;
            //cout<<i<<" "<<v1<<endl;
        }
        // REP(i,p1.size()) {
        //     cout<<p1[i]<< " ";
        // }
        // cout<<endl;
        FORD(i,n-1, 0) {
            int m = 1;
            if (v2<0) m = -1;
            v2 = m * mult(v[i] , abs(v2));
            p2[i] = v2;
            //cout<<i<<" "<<v1<<endl;
        }
        // REP(i,p2.size()) {
        //     cout<<p2[i]<< " ";
        // }
        // cout<<endl;
        FOR(i,1,n) {
            int c = 1;
            FOR(j, i, n-1) {
                int m = 1;
                if (c<0) m = -1;
                c = m * mult(abs(c), v[j]);
                //cout<<i<<" "<<j<<" "<<c<<endl;
                if (c == 3 && p1[i-1] == 2 && p2[j+1] == 4) {
                    found = true;
                    break;
                }
            }
            if (found) break;
        }
        if (found) cout<<"Case #"<<t+1<<": YES"<<endl;
        else cout<<"Case #"<<t+1<<": NO"<<endl;
    }

    return 0;
}