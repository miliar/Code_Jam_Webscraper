#include <vector>
#include <list>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <string>

#define FOR(i,a,b)  for(int i=(a);i<(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define REP(i,a)    FOR(i,0,a)
#define MP          make_pair
#define PB          push_back
#define ST          first
#define ND          second

using namespace std;

using VI = vector<int>;
using VVI = vector<VI>;
using PII = pair<int, int>;
using VII = vector<PII>;
using LL = long long int;
using ULL = unsigned long long int;

const int MAXN = 105;
const int LET = 'z'-'a'+1;
const LL MOD = 1000000007LL;

int dyn[MAXN][MAXN][MAXN];


void solve() {
    int N;
    cin >> N;
    string s;
    vector<bool> closedColors(LET, false);
    vector<char> begins(N), ends(N);

    REP (i, N) {
        cin >> s;
        begins[i] = s[0];
        ends[i] = s[s.length()-1];

        char prev = s[0];
        bool opening = true;
        FOR (j, 1, s.length()) {
            if (s[j] != prev) {
                if (opening) {
                    opening = false;
                }
                else {
                    closedColors[prev-'a'] = true;
                }
                prev = s[j];
            }
        }
        if (!opening && begins[i] == ends[i]) {
            cout << "0\n"; // TODO
            return;
        }
    }

    VI begCnt(LET, 0), endCnt(LET, 0);
    VI connectors(LET, 0);
    REP (i, N) {
        if (closedColors[begins[i]-'a'] || closedColors[ends[i]-'a']) {
//cout << i << " " << closedColors[begins[i]-'a'] << " " << closedColors[ends[i]-'a'] << "\n";
            cout << "0\n"; // TODO
            return;
        }

        if (begins[i] != ends[i]) {
            ++begCnt[begins[i]-'a'];
            ++endCnt[ends[i]-'a'];
        }
        else {
            ++connectors[begins[i]-'a'];
        }
    }

    REP (i, LET) {
        if (begCnt[i] > 1 || endCnt[i] > 1) {
            cout << "0\n"; // TODO
            return;
        }
    }

    vector<bool> used(N);
    vector<LL> counts;
    LL tmp;
    REP (c, LET) {
        tmp = 1;
        if (begCnt[c] == 1 && endCnt[c] == 0) {
            REP (i, N) {
                if (begins[i] != ends[i] && begins[i] - 'a' == c) {
                    int pos = i;
                    int next;
                    if (connectors[c] != 0) {
                        FOR (j, 1, connectors[c]+1) {
                            tmp *= j;
                            tmp %= MOD;
                        }
                        connectors[c] = 0;
                    }
                    do {
                        used[pos] = true;
                        next = ends[pos] - 'a';
                        if (connectors[next] != 0) {
                            FOR (j, 1, connectors[next]+1) {
                                tmp *= j;
                                tmp %= MOD;
                            }
                            connectors[next] = 0;
                        }
                        REP (ii, N) {
                            if (begins[ii] -'a' == next && begins[ii] != ends[ii]) {
                                pos = ii;
                                break;
                            }
                        }
                    } while (begCnt[next] != 0);
                    counts.PB(tmp);
//cerr << tmp << " x\n";
                    break;
                }
            }
        }
    }

    REP (i, N) {
        if (begins[i] != ends[i] && !used[i]) {
            cout << "0\n"; // TODO
            return;
        }
    }

    REP (i, LET) {
        LL tmp = 1;
        if (connectors[i] > 0) {
            FOR (j, 1, connectors[i]+1) {
                tmp *= j;
                tmp %= MOD;
            }
            counts.PB(tmp);
        }
    }

    LL res = 1;
    REP (i, counts.size()) {
        res *= counts[i];
        res %= MOD;
        res *= i+1;
        res %= MOD;
    }
    cout << res << "\n";
}



int testCases;

int main() {
    cin >> testCases;
    REP(i, testCases) {
        cout << "Case #" << i+1 << ": ";
        solve();
    }
    return 0;
}

