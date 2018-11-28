#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <stack>
#include <sstream>

#define mp make_pair

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

//int bubble(vector<int> &v, int from, int to) {
//    int i, j;
//    int res=0;
//    int num = to-from;
//    for(i=1; i<num; ++i) {
//        for(j=from; j<to-i; ++j) {
//            if (v[j] > v[j+1]) {
//                swap(v[j], v[j+1]);
//                ++res;
//            }
//        }
//    }
//    return res;
//}
//
//int calc(vector<int> v, int m, int pos) {
//    int res=0;
//    while(pos > m) {
//        swap(v[pos], v[pos-1]);
//        ++res;
//        --pos;
//    }
//    while(pos < m) {
//        swap(v[pos], v[pos+1]);
//        ++res;
//        ++pos;
//    }
//    res += bubble(v, 0, m);
//    for(int i=m+1; i<v.size(); ++i) {
//        v[i] = -v[i];
//    }
//    res += bubble(v, m+1, v.size());
//    return res;
//}

int findMin(vector<int> &v, int from, int to) {
    int res=from;
    for(int i=from+1; i<=to; ++i) {
        if (v[i] < v[res]) res = i;
    }
    return res;
}
int solve(vector<int> &v) {
    int n = v.size();
    int from, to;
    int res=0;
    from = 0;
    to = n-1;
    int t;
    while(from != to) {
        t = findMin(v, from, to);
        if (t-from < to-t) {
            for(int i=t; i>from; --i) {
                swap(v[i], v[i-1]);
                ++res;
            }
            ++from;
        } else {
            for(int i=t; i<to; ++i) {
                swap(v[i], v[i+1]);
                ++res;
            }
            --to;
        }
    }
    return res;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int i, j;
    int T, NT, n;
    vector<int> v;
    int res;
    cin>>NT;
    for(T = 1; T <= NT; ++T) {
        v.clear();
        cin>>n;
        v.resize(n);
        int pos=0;
        for(i=0; i<n; ++i) {
            cin>>v[i];
            if (v[i] > v[pos]) pos = i;
        }
        res=solve(v);
//        for(i=0; i<n; ++i) {
//            res = min(res, calc(v, i, pos));
//        }
        printf("Case #%d: %d\n", T, res);
    }
    return 0;
}
