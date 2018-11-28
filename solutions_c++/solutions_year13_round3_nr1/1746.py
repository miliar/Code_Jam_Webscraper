#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <limits.h>
#include <time.h>
#include <ctype.h>
#include <math.h>
#include <sstream>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <iomanip>
#include <float.h>
#include <fstream>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

typedef pair<int, int> PII;

//#define LARGE

int solve(string name, int n) {
    set<string> ret;
    int cnt = 0;
    int len = name.size();
    for (int i = 0; i < len; i++) {
        for (int j = i; j < len; j++) {
            string sub = name.substr(i, j - i + 1);
            int sublen = sub.size();
           
            for (int start = 0; start < sublen; start++) {
                for (int end = start; end < sublen; end++) {
                    if (end - start + 1 < n) continue;
                    string subsub = sub.substr(start, end - start + 1);
                    bool ok = true;
                    for (int s = 0; s < subsub.length(); s++) {
                        if (subsub[s] == 'a' || subsub[s] == 'i' || subsub[s] == 'u' || subsub[s] == 'e' || subsub[s] == 'o') {
                            ok = false;
                            break;
                        }
                    }
                    if (ok) {
                        cnt++;
                        goto proc;
                    }
                }
            }
proc:;
        }
    }
    return cnt;//ret.size();
}

int main() {

#ifndef LARGE
    ifstream in("A-small-attempt0.in");
    ofstream out("A-small-attempt0.out");
#else
    ifstream in("A-large-attempt.in");
    ofstream out("A-large-attempt.out");
#endif

    int T; in >> T;
    for (int t = 0; t < T; t++) {
        string name; in >> name;
        int n; in >> n;
        out << "Case #" << t + 1 << ": " << solve(name, n) << endl;
    }
    return 0;
}
