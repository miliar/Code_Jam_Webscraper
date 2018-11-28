#include <iostream>
#include <string>
#include <cstring>
#include <fstream>
#include <complex>
#include <limits>
#include <list>
#include <stack>
#include <numeric>
#include <queue>
#include <algorithm>
#include <functional>
#include <stack>
#include <bitset>
#include <map>
#include <set>
#include <map>
#include <list>
#include <math.h>
#include <set>
#include <stdio.h>
#include <ctype.h>
#include <vector>
#include <sstream>

using namespace std;


vector<string> getLineFields(istream& stream) {
    string line;
    getline(stream, line);
    stringstream str;
    str << line;
    vector<string> fields;
    string temp;
    while(str>>temp)
    {
        fields.push_back(temp);
    }
    return fields;
}

void play(const vector<int>& o, vector<int>& r, int p1, int pl, const set<int>& ind) {
    if (pl - p1 == 1) {
        int t = *ind.begin();
        r[o[t]] = p1;
        return;
    }
    set<int> w;
    set<int> l;
    int team = -1;
    for (set<int>::iterator it = ind.begin(); it != ind.end(); it++) {
        if (team == -1) team = *it;
        else {
            int team2 = *it;
            if (o[team] < o[team2]) {
                w.insert(team);
                l.insert(team2);
            } else {
                w.insert(team2);
                l.insert(team);
            }
            team = -1;
        }
    }
    play(o, r, p1, (p1 + pl) >> 1, w);
    play(o, r, (p1 + pl) >> 1, pl, l);
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        long long n, p;
        cin >> n >> p;
        vector<pair<long long, long long> > by(n + 1);
        vector<pair<long long, long long> > bz(n + 1);
        by[0] = make_pair(1, 0);
        bz[0] = make_pair(1, 0);
        for (long long i = 1; i <= n; ++i) {
            by[i] = make_pair(by[i-1].first + (1ll << (n - i)) , (1ll << (i + 1)) - 2);
            bz[i] = make_pair(1ll << i, bz[i-1].second + (1ll << (n - i)));
        }
        by[n].second = (1ll << n) - 1;
        long long y = 0;
        long long z = 0;
        for (int i = 0; i <= n; ++i) {
            if (by[i].first <= p)
                y = by[i].second;
            if (bz[i].first <= p)
                z = bz[i].second;
        }
        cout << "Case #" << t << ": " << y << " " << z << endl;
    }
}
