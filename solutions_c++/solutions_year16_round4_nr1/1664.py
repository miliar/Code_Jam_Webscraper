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
int cnt =0;

struct st {
    int p = 0, r=0, s = 0;
    int size () {
        return p+r+s;
    }
    bool bad() {
        return p<0 || r<0 || s<0;
    }
};

void solve() {
    int t;
    cin>>t;
    forn(i, t) {
        cnt=0;
        cout<<"Case #"<<i+1<<":"<<" ";
        int n;
        st str;
        cin>>n>>str.r>>str.p>>str.s;
        if (n==1) {
            if(str.p==2 || str.r==2 || str.s==2) {
                cout<<"IMPOSSIBLE"<<endl;
                continue;
            } else {
                if(str.p>0) cout<<"P";
                if(str.r>0) cout<<"R";
                if(str.s>0) cout<<"S";
                cout<<endl;
            }
            continue;
        }
        bool ok = true;
        bool first = true;
        bool stop = false;
        st res;
        while (true) {
            st nstr;
            while(str.size()>0) {
                if (str.size() == 2) {
                    if(str.p==2 || str.r==2 || str.s==2) {
                        ok = false;
                    } else {
                        ok = true;
                    }
                    stop = true;
                    break;
                }
                if(str.p>= str.r && str.p>= str.s) {
                    nstr.r++;
                    str.p-=2;
                    str.s--;
                    str.r--;
                } else if(str.r>= str.p && str.r>= str.s) {
                    nstr.s++;
                    str.r-=2;
                    str.s--;
                    str.p--;
                } else {
                    nstr.p++;
                    str.s-=2;
                    str.r--;
                    str.p--;
                }
                if (str.bad()) {
                    ok = false;
                    stop = true;
                    break;
                }
            }
            str = nstr;
            if (first) {
                first = false;
                res = str;
            }
            if(stop || nstr.size() == 1) {
                break;
            }
        }
        if (!ok) {
            cout<<"IMPOSSIBLE"<<endl;
            continue;
        }
        forn(i, res.r) {
            cout<<"PRPS";
        }
        forn(i, res.s) {
            cout<<"PRRS";
        }
        forn(i, res.p) {
            cout<<"PSRS";
        }
        
        
        cout<<endl;
    }
    
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