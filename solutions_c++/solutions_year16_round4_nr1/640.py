#include <iostream>
#include <cstdio>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
#include <unordered_map>
#include <unordered_set>
#include <cstring>


#define puba push_back
#define mapa make_pair
#define ff first
#define ss second
#define pii piar < int, int >


using namespace std;


typedef long long LL;

int num[3];
vector < int > path;


bool check(vector < int > path) {
    int sz = path.size();
    if (sz == 1) return true;
    vector < int > cans (sz / 2);

    for (int i = 0; i < sz / 2; ++i) {
        int ff = path[i * 2];
        int ss = path[i * 2 + 1];
        if (ff == ss) return false;
        if (ff > ss) swap(ff, ss);
        int ans = 0;
        if (ff == 0 && ss == 1) {
            ans = 0;   
        }
        if (ff == 0 && ss == 2) {
            ans = 2;
        }
        if (ff == 1 && ss == 2) {
            ans = 1;
        }

        cans[i] = ans;
    }
    return check(cans);
}


bool dfs(int s) {
    if (s == 0) {
        if (check(path)) {
            return true;
        }
        return false;
    }

    for (int i = 0; i < 3; ++i) { 
        if (num[i] > 0) {
            --num[i];
            path.puba(i);
            if (dfs(s - 1)) return true;
            ++num[i];
            path.pop_back();
        }
    }
    return false;
}

char cc[3] = { 'P', 'R', 'S' };

int main() {
    int t;
    cin >> t;
    for (int q = 0; q < t; ++q) {
        cout << "Case #" << q + 1 << ": ";
        int n, r, p, s;
        cin >> n >> r >> p >> s;

        num[0] = p;
        num[1] = r;
        num[2] = s;
        path.clear();
        if (dfs(p + r + s)) {
            for (int i = 0; i < p + r + s; ++i) {
                cout << cc[path[i]];
            }
            cout << endl;
        }
        else {
           cout << "IMPOSSIBLE" << endl; 
        }
    }
    return 0;
}