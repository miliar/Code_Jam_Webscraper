#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define ll long long
#define pb push_back

using namespace std;
const ll maxn = 1000000000+5;
const ll maxm = 1000+5;
const ll maxp = 1000000000+5;

ll get_cost(vector< vector<ll> > v, int n) {
    ll cost = 0;
    for (int i = 0; i < v.size(); i++) {
        int s = v[i][1] - v[i][0];
        cost += (n+n-s+1)*s/2*v[i][2];
    }
    return cost;
}
int main() {
    //ifstream fin  ("A-small.in");
    //ofstream fout ("A-small.out");
    ifstream fin  ("A-small-attempt0.in");
    ofstream fout ("A-small-attempt0.out");
    //ifstream fin  ("A-large-practice.in");
    //ofstream fout ("A-large-practice.out");

    int testcase;
    fin >> testcase;

    for (int case_id = 0; case_id < testcase; case_id++) {
        stringstream ss;
        /*ALG START*/
        ll n, m;
        fin >> n >> m;
        vector< vector<ll> > v;
        for (ll i = 0; i < m; i++) {
            ll o, e, p;
            fin >> o >> e >> p;
            vector<ll> a;
            a.pb(o); a.pb(e); a.pb(p);
            v.pb(a);
        }

        ll hcost = get_cost(v, n);

        ll notcover_cnt = -1;
        //cout << "BEFORE" << endl;
        //for (int i = 0; i < v.size(); i++) {
            //printf("%lld %lld %lld\n", v[i][0], v[i][1], v[i][2]);
        //}
        while ( notcover_cnt != v.size()*v.size() ) {
            notcover_cnt = 0;
            for (int i = 0; i < v.size(); i++) {
                for (int j = 0; j < v.size(); j++) {
                    if (i == j || -1 == v[i][0] || -1 == v[j][0]) {
                        notcover_cnt++;
                        continue;
                    }
                    if (v[i][0] < v[j][0] && v[i][1] > v[j][0] && v[i][1] < v[j][1]) {
                        ll delta_p = v[i][2] - v[j][2];
                        if ( 0 == delta_p ) {
                            ll o1 = v[i][0],
                               e1 = v[j][1],
                               p1 = v[i][2],
                               o2 = v[j][0],
                               e2 = v[i][1],
                               p2 = v[j][2];
                            v[i][0] = o1;
                            v[i][1] = e1;
                            v[i][2] = p1;
                            v[j][0] = o2;
                            v[j][1] = e2;
                            v[j][2] = p2;
                        } else if ( delta_p > 0 ) {
                            ll o1 = v[i][0],
                               e1 = v[j][1],
                               p1 = v[j][2],
                               o2 = v[j][0],
                               e2 = v[i][1],
                               p2 = v[j][2];
                            v[i][2] = v[i][2] - v[j][2];
                            v[j][0] = o1;
                            v[j][1] = e1;
                            v[j][2] = p1;
                            vector<ll> t;
                            t.pb(o2); t.pb(e2); t.pb(p2);
                            v.pb(t);
                        } else {
                            ll o1 = v[j][0],
                               e1 = v[i][1],
                               p1 = v[i][2],
                               o2 = v[i][0],
                               e2 = v[j][1],
                               p2 = v[i][2];
                            v[j][2] = v[j][2] - v[i][2];
                            v[i][0] = o1;
                            v[i][1] = e1;
                            v[i][2] = p1;
                            vector<ll> t;
                            t.pb(o2); t.pb(e2); t.pb(p2);
                            v.pb(t);
                        }
                    }
                    else if (v[i][0] < v[j][0] && v[i][1] == v[j][0] && v[i][1] < v[j][1]) {
                        ll delta_p = v[i][2] - v[j][2];
                        if ( 0 == delta_p ) {
                            ll o1 = v[i][0],
                               e1 = v[j][1],
                               p1 = v[i][2];
                            v[i][0] = o1;
                            v[i][1] = e1;
                            v[i][2] = p1;
                            v[j][0] = -1;
                            v[j][1] = -1;
                            v[j][2] = -1;
                        } else if ( delta_p > 0 ) {
                            ll o1 = v[i][0],
                               e1 = v[j][1],
                               p1 = v[j][2];
                            v[i][2] = v[i][2] - v[j][2];
                            v[j][0] = o1;
                            v[j][1] = e1;
                            v[j][2] = p1;
                        } else {
                            ll o1 = v[i][0],
                               e1 = v[j][1],
                               p1 = v[i][2];
                            v[j][2] = v[j][2] - v[i][2];
                            v[i][0] = o1;
                            v[i][1] = e1;
                            v[i][2] = p1;
                        }
                    }
                    else if (v[j][0] < v[i][0] && v[j][1] > v[i][0] && v[j][1] < v[i][1]) {
                        ll delta_p = v[i][2] - v[j][2];
                        if ( 0 == delta_p ) {
                            ll o1 = v[j][0],
                               e1 = v[i][1],
                               p1 = v[i][2],
                               o2 = v[i][0],
                               e2 = v[j][1],
                               p2 = v[j][2];
                            v[i][0] = o1;
                            v[i][1] = e1;
                            v[i][2] = p1;
                            v[j][0] = o2;
                            v[j][1] = e2;
                            v[j][2] = p2;
                        } else if ( delta_p > 0 ) {
                            ll o1 = v[j][0],
                               e1 = v[i][1],
                               p1 = v[j][2],
                               o2 = v[i][0],
                               e2 = v[j][1],
                               p2 = v[j][2];
                            v[i][2] = v[i][2] - v[j][2];
                            v[j][0] = o1;
                            v[j][1] = e1;
                            v[j][2] = p1;
                            vector<ll> t;
                            t.pb(o2); t.pb(e2); t.pb(p2);
                            v.pb(t);
                        }
                        else {
                            ll o1 = v[i][0],
                               e1 = v[j][1],
                               p1 = v[i][2],
                               o2 = v[j][0],
                               e2 = v[i][1],
                               p2 = v[i][2];
                            v[j][2] = v[j][2] - v[i][2];
                            v[i][0] = o1;
                            v[i][1] = e1;
                            v[i][2] = p1;
                            vector<ll> t;
                            t.pb(o2); t.pb(e2); t.pb(p2);
                            v.pb(t);
                        }
                    }
                    else if (v[j][0] < v[i][0] && v[j][1] == v[i][0] && v[j][1] < v[i][1]) {
                        ll delta_p = v[i][2] - v[j][2];
                        if ( 0 == delta_p ) {
                            ll o1 = v[j][0],
                               e1 = v[i][1],
                               p1 = v[j][2];
                            v[i][0] = o1;
                            v[i][1] = e1;
                            v[i][2] = p1;
                            v[j][0] = -1;
                            v[j][1] = -1;
                            v[j][2] = -1;
                        } else if ( delta_p > 0 ) {
                            ll o1 = v[j][0],
                               e1 = v[i][1],
                               p1 = v[j][2];
                            v[i][2] = v[i][2] - v[j][2];
                            v[j][0] = o1;
                            v[j][1] = e1;
                            v[j][2] = p1;
                        } else {
                            ll o1 = v[j][0],
                               e1 = v[i][1],
                               p1 = v[i][2];
                            v[j][2] = v[j][2] - v[i][2];
                            v[i][0] = o1;
                            v[i][1] = e1;
                            v[i][2] = p1;
                        }
                    }
                    else {
                        notcover_cnt++;
                    }
                }
            }
        }

        //cout << "AFTER " << endl;
        //for (int i = 0; i < v.size(); i++) {
            //printf("%lld %lld %lld\n", v[i][0], v[i][1], v[i][2]);
        //}

        ll lcost = get_cost(v, n);
        //cout << hcost << " " << lcost << endl;

        ss << (hcost - lcost);

        /*ALG END  */
        string ret (ss.str());
        //cout << "Case #" << (case_id+1) << ": " << ret << endl;
        fout << "Case #" << (case_id+1) << ": " << ret << endl;
    }
}
