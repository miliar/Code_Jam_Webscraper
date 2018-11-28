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

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int i, j;
    int n, T, NT, x;
    cin>>NT;
    vector<int> v;
    for(T=1; T <= NT; ++T) {
        cin>>n>>x;
        v.clear();
        v.resize(n);
        for(i=0; i<n; ++i) {
            cin>>v[i];
        }
        sort(v.begin(), v.end());
        int idx = 0;
        int res=0;
        for(i = n-1; i>=idx; --i) {
            ++res;
            if (i == idx) {
                break;
            }
            if (v[i] + v[idx] <= x) {
                ++idx;
            }
        }
        printf("Case #%d: %d\n", T, res);
    }
    return 0;
}
