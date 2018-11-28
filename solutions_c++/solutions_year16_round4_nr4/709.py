#include <cstring>
#include <cmath>
#include <cstdio>
#include <algorithm>
#include <iostream>
#include <ctime>
#include <vector>
#include <map>
#include <set>

using namespace std;

#define pb push_back
#define sz(a) (int)a.size()
#define fs first
#define sc second

typedef long long ll;
typedef pair<int,int> ii;

int n;
string s[30];

bool Is(int mask, int idx) {
    return (1<<idx)&mask;
}

bool dfs(int idx, int mask, int all, vector <int> & A) {
    if (idx==sz(A)) return 1;
    int x = A[idx];
    bool check = false;
    for (int i = 0; i < n; ++i)
        if (!Is(all,i)) {
            if (Is(mask,x*n+i)||s[x][i]=='1') {
                check = true;
                if (!dfs(idx+1,mask,(1<<i)|all, A)) return 0;
            }
        }
    return check;
}

int get(int mask) {
    int res = 0;
    for (int i = 0; i < n*n; ++i) {
        if (!Is(mask,i)) continue;
        res += s[i/n][i%n] == '0';
    }
    return res;
}


bool kiemtra(int mask) {
    vector <int> A;
    for (int i = 0; i < n; ++i) A.pb(i);
    do {
        if (!dfs(0,mask,0,A)) return 0;
    } while (next_permutation(A.begin(),A.end()));
    return 1;
}

int solve() {
    int p = (1<<(n*n)), res = 1000000000;
    for (int i = 0; i < p; ++i)
        if (kiemtra(i)) res = min(res,get(i));
    return res;
}

int main() {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t; scanf("%d\n",&t); int tmp = t;
    while (t--) {
        scanf("%d\n",&n);
        for (int i = 0; i < n; ++i) cin >> s[i];
        printf("Case #%d: %d\n",tmp-t,solve());
    }
    return 0;
}
