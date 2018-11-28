/* 
 * File:   main.cpp
 * Author: waleed
 *
 * Created on April 13, 2013, 2:33 AM
 */

#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>
#include <fstream>
#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define pi acos(-1.0)
#define N 1000000
#define LL int int

#define For(i, a, b) for( int i = (a); i < (b); i++ )
#define Fors(i, sz) for( size_t i = 0; i < sz.size (); i++ )
#define Fore(it, x) for(typeof (x.begin()) it = x.begin(); it != x.end (); it++)
#define Set(a, s) memset(a, s, sizeof (a))
#define Read(r) freopen(r, "r", stdin)
#define Write(w) freopen(w, "w", stdout)

#define isOn(S, j) (S & (1 << j))
#define setBit(S, j) (S |= (1 << j))
#define clearBit(S, j) (S &= ~(1 << j))
#define toggleBit(S, j) (S ^= (1 << j))
#define lowBit(S) (S & (-S))
#define setAll(S, n) (S = (1 << n) - 1)

using namespace std;

bool palin(int n) {
    int l = ceil(log10(n + 1));
    stack<int> s;
    while (ceil(log10(n + 1)) > l / 2) {
        s.push(n % 10);
        n /= 10;
    }
    if (l % 2) s.pop();
    for (int i = 0; i < s.size(); i++) {
        if (s.top() != n % 10) {
            return false;
        }
    }
    return true;
}

int main(int argc, char** argv) {
    fstream cin("in.in", ios::in);
    fstream cout("out.out", ios::out);
    vector<long> fair;
    for (long i = 1; i * i <= 1000; i++) {
        if (palin(i) && palin(i * i)) {
            fair.push_back(i * i);
        }
    }
    int cas;

    cin >> cas;
    for (int cs = 1; cs <= cas; cs++) {
        long a, b;
        cin >> a >> b;
        int st = INF_MAX, end = INF_MAX;
        for (int i = 0; i < fair.size(); i++) {
            if (fair[i] >= a && st == INF_MAX)st = i;
            if (fair[i] > b) {
                end = i;
                break;
            }
        }

        if (st == INF_MAX) st = fair.size();
        if (end == INF_MAX) end = fair.size();
        cout << "Case #" << cs << ": " << (end - st) << endl;
    }

    return 0;
}
