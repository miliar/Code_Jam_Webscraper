#include <bits/stdc++.h>

using namespace std;

const int N = 16, J = 50;
set<pair< vector<int>, vector<int> > > cool;

long long div(long long x) {
    for (long long i = 2; i*i <= x && i <= 1000000; i++) {
        if (x % i == 0) {
            return i;
        }
    }
    return -1;
}

pair<bool, vector<int> > check(const vector<int> &who) {
    vector<int> res;
    for (int i = 2; i <= 10; i++) {
        long long val = 0;
        for (int j = 0; j < who.size(); j++) {
            val = val*i + who[j];
        }
        long long p = div(val);
        if (p == -1) {
            return make_pair(false, res);
        }
        res.push_back(p);
    }
    return make_pair(true, res);
}

void solve(int test) {
    printf("Case #%d:\n", test);
    int it = 0;
    while (cool.size() < J) {
        vector<int> cur;
        cur.push_back(1);
        for (int i = 1; i <= N - 2; i++) {
            cur.push_back( rand() % 2 );
        }
        cur.push_back(1);
        pair<bool, vector<int> > now = check(cur);
        if (now.first) {
            cool.insert( make_pair(cur, now.second) );
        }
    }

    for (auto it = cool.begin(); it != cool.end(); ++it) {
        for (int i = 0; i < (*it).first.size(); i++) {
            cout << (*it).first[i];
        }
        cout << " ";
        for (int i = 0; i < (*it).second.size(); i++) {
            cout << (*it).second[i] << " ";
        }
        cout << endl;
    }
}

int main() {
    //freopen("A-large.in", "r", stdin);
    freopen("C-small.out", "w", stdout);
    int test = 1;
    //cin >> test;
    //test = 1E6;
    for (int i = 1; i <= test; i++) {
        solve(i);
    }
    return 0;
}
