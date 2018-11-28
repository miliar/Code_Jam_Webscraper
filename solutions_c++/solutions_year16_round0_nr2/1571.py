#include <cstdio>
#include <cassert>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <cstring>
#include <cstdlib>
#include <cmath>
#define For(i, n) for (int i = 0; i < (int) n; ++i)
#define SIZE(x) ((int) (x).size())
#define mp(a, b) make_pair(a, b)
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

#ifndef DG
#define DG 0
#endif
#define LOG(...) (DG ? fprintf(stderr, __VA_ARGS__) : 0)

int main(){
    int t;
    cin >> t;
    For(cases, t) {
        string s;
        cin >> s;
        s.push_back('+');
        char lastchar = s[0];
        int changes = 0;
        For(i, SIZE(s)) {
            if (lastchar != s [i]) changes ++;
            lastchar = s [i];
        }
        printf("Case #%d: %d\n", cases + 1, changes);
    }

}
