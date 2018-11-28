#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cstring>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <sstream>
#include <complex>
#include <cassert>

using namespace std;
typedef long long ll;
typedef vector<int> VI;
typedef pair<int, int> PII;

#define REP(i,s,t) for(int i=(s);i<(t);i++)
#define FILL(x,v) memset(x,v,sizeof(x));

string line;

int checkPos(string &s, char sign) {
    int cc = 0;
    for (auto&& c : s)
        if (c == sign) cc++;
    return cc;
}

void flip(string &s, int len) {
    reverse(s.begin(), s.begin()+len);
    for (auto&& it = s.begin(); it != s.begin() + len; it++) {
        if (*it == '+') *it = '-';
        else *it = '+';
    }
}

int main() {

    int T;
    scanf("%d", &T);
    REP(cas, 1, T+1) {
        int ans = 0;
        cin >> line;
        int len = line.size();
        int curLen = 1;
        char curSign = *line.begin();
        while (curLen <= len) {
            if (line.front() != curSign) { flip(line, curLen-1); ans++; }
            curSign = *(line.begin()+curLen);
            curLen++;
        }
        if (line.front() != '+') { flip(line, len); ans++; }
        printf("Case #%d: %d\n", cas, ans);
    }

    return 0;
}
