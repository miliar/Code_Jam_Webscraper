#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>

#define FOR(i,a,n) for(int i=a;i<n;i++)
#define REP(i,n) FOR(i,0,n)
#define DBGV(_v) { REP(_i, _v.sz) { cout << _v[_i] << "\t";} cout << endl;}
#define sz size()
#define MAX 100000

using namespace std;

set <int> squares;

bool ispali(int n) {
    string s, t;
    ostringstream ost;
    ost << n;  
    ost.flush();
    s =  ost.str();
    t = s;
    reverse(s.begin(), s.end());
    return t == s;
}


int main() {
    FOR(i, 1, MAX) {
        squares.insert(i*i);
    }
    int kase = 0;
    cin >> kase;
    for(int kase_cnt = 1; kase_cnt <= kase; kase_cnt++) {
        int a, b, res = 0;
        cin >> a >> b;
        cout << "Case #" << kase_cnt << ": ";
        FOR(i, a, b+1) {
            if (ispali(i) && squares.find(i) != squares.end()) {
                int sq = sqrt(i);
                if (ispali(sq)) {
                    //cout << i << endl;
                    res++;
                }
            }
        }
        cout << res << endl;
    }
}
