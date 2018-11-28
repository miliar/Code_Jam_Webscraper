//
//  main.cpp
//  contest
//
//  Created by user on 25/12/14.
//  Copyright (c) 2014 user. All rights reserved.
//

#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define ford(i, n) for (int i = (int)(n) - 1; i >= 0; --i)
#define pb push_back
#define mp make_pair


typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<pii> vp;

const double PI = 3.141592653589793238;
bool DBG = false;

template<typename T, typename S>
std::ostream& operator << (std::ostream& os, const std::pair<T, S>& p) {
    os << "(" << p.first << ", " << p.second << ")";
    return os;
}

template<typename T>
std::ostream& operator << (std::ostream& os, const std::vector<T>& vector) {
    for (size_t i = 0; i < vector.size(); ++i) {
        os << vector[i] << " ";
    }
    return os;
}


string solve(int x, int r, int c) {
    string gab = "GABRIEL";
    string ric = "RICHARD";
    int s = r * c;
    
    if (x == 1) {
        return gab;
    } else if (x == 2) {
        if (s % 2 == 0) {
            return gab;
        } else {
            return ric;
        }
    } else if (x == 3) {
        if (s <= 3 ||
            s % 3 != 0) {
            return ric;
        } else {
            return gab;
        }
    } else if (x == 4) {
        if (s % 4 != 0 ||
            s < 12) {
            return ric;
        } else {
            return gab;
        }
    }
    return "FAIL";
}

int main() {
    std::ios_base::sync_with_stdio(false);
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    forn(i, T) {
        int x, r, c;
        cin >> x >> r >> c;
        cout << "case #" << i + 1 << ": " << solve(x, r, c) << endl;
    }
    return 0;
}
