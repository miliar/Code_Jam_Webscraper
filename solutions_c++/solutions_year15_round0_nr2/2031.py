#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>

#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

void print(int s, priority_queue<pair<pair<int, int>, int> > qs) {
    cout << s << " :";
    while (qs.size() > 0) {
        cout << " " << qs.top().first.second << "," << qs.top().first.first << "," << qs.top().second;
        qs.pop();
    }
    cout << endl;
}

void clean(priority_queue<pair<pair<int, int>, int> > &qs, vector<int> &cs, vector<int> &vs) {
    while (qs.top().second != cs[qs.top().first.second]) {
        qs.pop();
    }
}

void split(priority_queue<pair<pair<int, int>, int> > &qs, vector<int> &cs, vector<int> &vs) {
    clean(qs, cs, vs);
    int i = qs.top().first.second;
    int n = qs.top().second;
    qs.pop();
    cs[i]++;
    for (int j = 0; j <= n; ++j) {
        qs.push(make_pair(make_pair((vs[i] + j) / (n + 1), i), n + 1));
    }
    clean(qs, cs, vs);
}

int main() {
    ifstream cin("in.txt");
    ofstream cout("out.txt");
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        priority_queue<pair<pair<int, int>, int> > qs;
        vector<int> cs, vs;
        // input
        int l;
        cin >> l;
        for (int j = 0, p; j < l; ++j) {
            cin >> p;
            qs.push(make_pair(make_pair(p, j), 1));
            cs.push_back(1);
            vs.push_back(p);
        }
        //
        int minTime = qs.top().first.first;
        for (int s = 1; qs.top().first.first > 1 && s <= 1000; ++s) {
            split(qs, cs, vs);
            minTime = min(minTime, s + qs.top().first.first);
            //print(s, qs);
        }
        cout << "Case #" << (i + 1) << ": " << minTime << endl;
    }
}
