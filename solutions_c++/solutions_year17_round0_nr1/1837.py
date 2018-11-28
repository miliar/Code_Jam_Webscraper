#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>
#include <string.h>
#include <climits>

using namespace std;

int ar[1009];
int re[1009];

int main() {
    int ite;
    cin >> ite;
    for(int TT = 1; TT <= ite; TT++) {
        string s;
        int k;
        cin >> s >> k;
        memset(ar, 0, sizeof ar);
        memset(re, 0, sizeof re);
        for(int i=0; i<s.size(); i++ ) {
            if(s[i] == '-') {
                ar[i] = 1;
            }
        }
        bool can = true;
        int res = 0;
        for(int i=0; i<s.size() && can; i++ ) {
            re[i] += ( i > 0 ? re[i-1] : 0);
            ar[i] += re[i];
            if(ar[i] & 1) {
                res += 1;
                re[i] += 1;
                if(i + k > s.size()) {
                    can = false;
                } else {
                    re[i + k] += -1;
                }
            }
        }
        cout << "Case #" << TT <<": ";
        if (can) {
            cout << res << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}

