//
// upanddown.cpp
//
// Siwakorn Srisakaokul - ping128
// Written on Saturday, 31 May 2014.
//

#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <cmath>
#include <algorithm>
#include <map>
#include <ctype.h>
#include <string.h>

#include <assert.h>

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;
typedef pair<PII, int> PII2;

#define MAXN 1005

int in[MAXN];
int N;
int temp[MAXN];

int fenwick[MAXN];
int N2;
vector<int> v;

int gett(int x) {
    int ret = 0;
    for (int i = x; i; i -= (i & (-i)))
        ret += fenwick[i];
    return ret;
}

void update(int x, int val) {
    for (int i = x; i <= N2; i += (i & (-i)))
        fenwick[i] += val;
}

int inversion() {
    int ret = 0;
    N2 = v.size();
    if (N2 <= 1) return 0;
    for (int i = 0; i < MAXN; i++) fenwick[i] = 0;
    map<int, int> M;
    for (int i = 0; i < N2; i++) M[v[i]] = 1;
    int cc = 0;
    for (auto it = M.begin(); it != M.end(); it++) {
        cc++;
        it->second = cc;
    }

    for (int i = 0; i < N2; i++) {
        ret += i - gett(M[v[i]]);
        update(M[v[i]], 1);
    }
    return ret;
}
int xxx[MAXN];

void solve() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> in[i];
    }

    int ans = 0;
    int left = 0, right = N - 1;
    while (left < right) {

        int minn = 1000000000;
        int ind;
        for (int i = left; i <= right; i++) {
            if (in[i] < minn) {
                minn = in[i];
                ind = i;
            }
        }

        if (ind - left < right - ind) {
            while (ind != left) {
                swap(in[ind], in[ind - 1]);
                ind--;
                ans++;
            }
            left++;
        } else {
            while (ind != right) {
                swap(in[ind], in[ind + 1]);
                ind++;
                ans++;
            }
            right--;
        }
    }
    cout << ans << endl;
}

int main() {
    int test;
    scanf("%d", &test);
    for (int tt = 0; tt < test; tt++) {
        printf("Case #%d: ", tt + 1);
        solve();
    }
    return 0;
}
