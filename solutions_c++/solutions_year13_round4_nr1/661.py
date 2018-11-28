#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <sstream>
#include <cstring>
#include <queue>
#include <vector>
#include <deque>
#include <stack>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>
using namespace std;
const int pp = 1000002013;
int m, n, o[1010], e[1010], p[1010];
int get(int a, int b, int c) {
    long long tmp = (b-a);
    tmp = (tmp*n+(tmp-1)*tmp/2)%pp;
    int ret = tmp*c%pp;
    return ret;
}
struct aa{
    int a, b, c;
    bool operator < (const aa &other) const {
        if (a == other.a)
            return b > other.b;
        return a < other.a;
    }
}b[2020];
int main() {
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; ++tt) {
        cout << "Case #" << tt << ": ";
        cin >> n >> m;
        long long a1 = 0;
        for (int i = 0; i < m; ++i) {
            cin >> o[i] >> e[i] >> p[i];
            a1 = (a1+get(o[i], e[i], p[i]))%pp;
            b[i].a = o[i];
            b[i].b = 1;
            b[i].c = p[i];
            b[m+i].a = e[i];
            b[m+i].b = -1;
            b[m+i].c = p[i];
        }
        sort(o, o+m);
        sort(e, e+m);
        sort(b, b+2*m);
        stack<aa> s;
        long long a2 = 0;
        for (int i = 0; i < 2*m; ++i) {
            if (b[i].b == 1) {
                aa tmp;
                tmp.a = b[i].a;
                tmp.c = b[i].c;
                s.push(tmp);
            } else {
                int now = b[i].c;
                while (now > 0) {
                    aa tmp = s.top();
                    s.pop();
                    if (now >= tmp.c) {
                        now -= tmp.c;
                        a2 = (a2+get(tmp.a, b[i].a, tmp.c))%pp;
                    } else {
                        tmp.c -= now;
                        a2 = (a2+get(tmp.a, b[i].a, now))%pp;
                        now = 0;
                        s.push(tmp);
                    }
                }
            }
        }
        cout << (a2-a1+pp)%pp << endl;
    }
    return 0;
}
