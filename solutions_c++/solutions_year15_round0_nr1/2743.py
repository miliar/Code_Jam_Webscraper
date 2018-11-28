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

ll solve(ll s, string val);

int main() {
    //ifstream fin  ("A-small.in");
    //ofstream fout ("A-small.out");
    ifstream fin  ("A-small-attempt0.in");
    ofstream fout ("A-small-attempt0.out");
    //ifstream fin  ("A-large.in");
    //ofstream fout ("A-large.out");

    int testcase;
    fin >> testcase;

    for (int case_id = 0; case_id < testcase; case_id++) {
        /*ALG START*/
        ll s;
        string val;
        fin >> s >> val;
        ll ret = solve(s, val);
        /*ALG END  */
        fout << "Case #" << (case_id+1) << ": " << ret << endl;
    }
}

ll solve(ll s, string val) {
    vector<ll> aud;
    for (int i = 0; i < val.size(); ++i) {
        aud.push_back(val[i] - '0');
    }
    ll ret = 0;
    ll current = 0;
    for (int i = 0; i < aud.size(); ++i) {
        if (i == 0 || current >= i || aud[i] == 0) {
            current += aud[i];
        } else {
            ret += i - current;
            current += ret + aud[i];
        }
    }
    return ret;
}
