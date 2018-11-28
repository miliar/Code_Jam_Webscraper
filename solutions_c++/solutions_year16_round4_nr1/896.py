#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>
using namespace std;

typedef long long ll;
#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define tr(i,c)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define found(s,e)  ((s).find(e)!=(s).end())

// #include "cout.h"

int winner[3][3] = { { -1, 0, 2 }, { 0, -1, 1 }, { 2, 1, -1 } };

// 0 -> 01, 02
// 1 -> 01, 12
// 2 -> 02, 12

string to_str(vector<int>& t){
    stringstream ss;
    for (int i=0; i<t.size(); ++i) {
        ss << ("PRS"[t[i]]);
    }
    return ss.str();
}

string solve_l(int N, int P, int R, int S) {
    string s = "X";
    rep(seed, 3) {
        vector<int> p(1, seed), q;
        rep(i, N) {
#if DEBUG
            cout << i << ") " << p << endl;
#endif
            q.clear();
            rep(j, p.size()) {
                switch (p[j]){
                    case 0: q.pb(0); q.pb(1); break;
                    case 1: q.pb(1); q.pb(2); break;
                    case 2: q.pb(0); q.pb(2); break;
                }
            }
            int QS = q.size();
            for (int span=2; span<QS; span*=2) {
                rep(j, QS/span/2) {
                    // compare
                    int base = span*(2*j);
                    bool do_swap = false;
                    rep(k, span) {
                        int a = q[base + k];
                        int b = q[base + span + k];
                        if (a < b) break; // ok
                        if (a > b) { do_swap = true; break; }
                    }
                    if (do_swap) {
                        #if DEBUG
                        cout << "  : " << q << " -> ";
#endif
                        rep(k, span) {
                            swap(q[base+k], q[base+span+k]);
                        }
                        #if DEBUG
                        cout << q << endl;
#endif
                    }
                }
            }

            // cout << p.size() << " " << q.size() << endl;
            swap(p, q);
        }
#if DEBUG
        printf("N=%d, seed=%d", N, seed); cout << p << endl;
#endif
        vector<int> st(3, 0);
        rep(i, p.size()){
            st[p[i]]++;
        }
        // cout << st << endl;
        if (st[0] == P && st[1] == R && st[2] == S) {
//            cout << "OUI ";
            string s1 = to_str(p);
            if (s1 < s) s = s1;
            // cout << to_str(p) << endl;
        } else {
//            cout << "NON ";
        }
    }

    if (s == "X") return "IMPOSSIBLE";
    else return s;
}

/*
string solve_l(int N, int R, int P, int S) {
    // assert(1 <= N && N <= 3);
    return patterns(N, P, R, S);
    return "IMPOSSIBLE";
}
*/

int main(){
  int _T; cin>>_T; // 1-100
  rep(_t,_T){
  int N, // 1-3, 1-12
      R,P,S; // 0..2^N
      cin >> N >> R >> P >> S;

 answer:
    cout << "Case #" << (1+_t) << ": ";
    cout << solve_l(N,P,R,S) << endl;
  }
}
