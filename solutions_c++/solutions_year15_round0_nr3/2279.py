#pragma comment(linker, "/STACK:6400000000000")

#define _USE_MATH_DEFINES

#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <stack>
#include <cstring>
#include <iomanip>
#include <ctime>
#include <stack>
#include <bitset>
using namespace std;

typedef long long ll;
typedef long double ld;

const ld EPS = 1e-12;
const int INF = (int)(2e9 + 0.5);
const int MAXN = 10005;

inline int parse(const char & s) {
    if(s == 'i') return 2;
    if(s == 'j') return 3;
    if(s == 'k') return 4;
    return 0;
}

inline int multiply(const int & f, const int & s) {
    int result = 0;

    if(f == 1) result = s;

    if(f == 2 && s == 1) result = 2;
    if(f == 2 && s == 2) result = 5;
    if(f == 2 && s == 3) result = 4;
    if(f == 2 && s == 4) result = 7;
    if(f == 2 && s == 5) result = 6;
    if(f == 2 && s == 6) result = 1;
    if(f == 2 && s == 7) result = 8;
    if(f == 2 && s == 8) result = 3;


    if(f == 3 && s == 1) result = 3;
    if(f == 3 && s == 2) result = 8;
    if(f == 3 && s == 3) result = 5;
    if(f == 3 && s == 4) result = 2;
    if(f == 3 && s == 5) result = 7;
    if(f == 3 && s == 6) result = 4;
    if(f == 3 && s == 7) result = 1;
    if(f == 3 && s == 8) result = 6;


    if(f == 4 && s == 1) result = 4;
    if(f == 4 && s == 2) result = 3;
    if(f == 4 && s == 3) result = 6;
    if(f == 4 && s == 4) result = 5;
    if(f == 4 && s == 5) result = 8;
    if(f == 4 && s == 6) result = 7;
    if(f == 4 && s == 7) result = 2;
    if(f == 4 && s == 8) result = 1;


    if(f == 5 && s == 1) result = 5;
    if(f == 5 && s == 2) result = 6;
    if(f == 5 && s == 3) result = 7;
    if(f == 5 && s == 4) result = 8;
    if(f == 5 && s == 5) result = 1;
    if(f == 5 && s == 6) result = 2;
    if(f == 5 && s == 7) result = 3;
    if(f == 5 && s == 8) result = 4;


    if(f == 6 && s == 1) result = 6;
    if(f == 6 && s == 2) result = 1;
    if(f == 6 && s == 3) result = 8;
    if(f == 6 && s == 4) result = 3;
    if(f == 6 && s == 5) result = 2;
    if(f == 6 && s == 6) result = 5;
    if(f == 6 && s == 7) result = 4;
    if(f == 6 && s == 8) result = 7;


    if(f == 7 && s == 1) result = 7;
    if(f == 7 && s == 2) result = 4;
    if(f == 7 && s == 3) result = 1;
    if(f == 7 && s == 4) result = 6;
    if(f == 7 && s == 5) result = 3;
    if(f == 7 && s == 6) result = 8;
    if(f == 7 && s == 7) result = 5;
    if(f == 7 && s == 8) result = 2;


    if(f == 8 && s == 1) result = 8;
    if(f == 8 && s == 2) result = 7;
    if(f == 8 && s == 3) result = 2;
    if(f == 8 && s == 4) result = 1;
    if(f == 8 && s == 5) result = 4;
    if(f == 8 && s == 6) result = 3;
    if(f == 8 && s == 7) result = 6;
    if(f == 8 && s == 8) result = 5;

    return result;
}

int t[4 * MAXN];
string s, ss;

void build(int v, int left, int right) {
    if(left == right)
        t[v] = parse(ss[left]);
    else {
        int mid = (left + right) >> 1;
        build(v * 2, left, mid);
        build(v * 2 + 1, mid + 1, right);
        t[v] = multiply(t[v * 2], t[v * 2 + 1]);
    }
}

int get(int v, int from, int to, int left, int right) {
    if(from <= left && right <= to)
        return t[v];
    int mid = (left + right) >> 1;
    if(to <= mid)
        return get(v * 2, from, to, left, mid);
    if(from > mid)
        return get(v * 2 + 1, from, to, mid + 1, right);
    return multiply(get(v * 2, from, to, left, mid), get(v * 2 + 1, from, to, mid + 1, right));
}

int tt, l, x;

int main() {
    freopen("INPUT.TXT", "r", stdin);
    freopen("OUTPUT.TXT", "w", stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> tt;
    for(int q = 1; q <= tt; ++q) {
        cin >> l >> x >> s;
        ss = "";
        for(int i = 0; i < x; ss += s, ++i);
        build(1, 0, (int)ss.size() - 1);
        set<int> pos;
        for(int i = 0; i < (int)ss.size(); ++i) {
            int value = get(1, i, (int)ss.size() - 1, 0, (int)ss.size() - 1);
            if(value == 4)
                pos.insert(i);
        }
        int left = 1;
        bool been = false;
        for(int i = 0; i < (int)ss.size(); ++i) {
            left = multiply(left, parse(ss[i]));
            if(pos.find(i) != pos.end())
                pos.erase(i);
            if(left == 2) {
                for(set<int>::iterator it = pos.begin(); it != pos.end(); ++it) {
                    int v = (*it) - 1;
                    if(i < v) {
                        int value = get(1, i + 1, v, 0, (int)ss.size() - 1);
                        if(value == 3) {
                            been = true;
                            break;
                        }
                    }
                }
            }
            if(been)
                break;
        }
        cout << "Case #" << q << ": " << (been ? "YES" : "NO") << "\n";
    }
    return 0;
}


/*
int main() {
    freopen("INPUT.TXT", "w", stdout);
    cout << 100 << endl;
    for(int i = 0; i < 100; ++i) {
        cout << 1 << " " << 10000 << endl;
        cout << "a" << endl;
    }
    return 0;
}*/
