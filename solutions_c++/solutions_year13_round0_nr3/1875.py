#include <vector> // headers {{{
#include <list>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <fstream>
#include <ctime>

#define DEBUG(x) cout << #x << ": " << x << "\n"
using namespace std; // }}}

typedef long long lint;

vector<lint> v, v1;

int f(lint x)
{
    return upper_bound(v.begin(), v.end(), x) - v.begin();
}

int result(lint A, lint B)
{
    return f(B) - f(A - 1);
}

bool test(lint x)
{
    lint y = 0, z = x;
    while (z) {
        y = y * 10 + z % 10;
        z/= 10;
    }

    return y == x;
}

int main()
{
    time_t start, end;
    time(&start);
    
    ifstream cin("test.in");
    ofstream cout("test.out");
    //cout.precision(6);
    //cout.setf(ios::fixed,ios::floatfield);

    set<lint> s, s1;
    for (lint i = 1; i < 1e4; ++i) {
        lint x1 = i, x2 = i / 10, y = i;
        while (y) {
            x1 = x1 * 10 + y % 10;
            x2 = x2 * 10 + y % 10;
            y/= 10;
        }
        lint y1 = x1 * x1;
        lint y2 = x2 * x2;
        if (test(y1)) {
            s.insert(y1);
            s1.insert(x1);
        }
        if (test(y2)) {
            s.insert(y2);
            s1.insert(x2);
        }
    }
    v = vector<lint>(s.begin(), s.end());
    v1 = vector<lint>(s1.begin(), s1.end());
    /*cout << v.size() << endl;
    for (int i = 0; i < v.size(); ++i) {
        if (v[i] != v1[i] * v1[i])
            cout << "Error!" << endl;
        cout << v[i] << " " << v1[i] << endl;
    }
    cout << endl;*/

    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        lint A, B;
        cin >> A >> B;
        cout << "Case #" << i << ": " << result(A, B) << endl;
        time(&end);
        ::cout << i << " " << difftime(end, start) << endl;
    }

    return 0;
}
