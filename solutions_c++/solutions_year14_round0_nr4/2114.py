#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <algorithm>
#include <iostream>
using namespace std;

#define foreach(it, s) for (__typeof(s.begin()) it = s.begin(); it != s.end(); ++it)
#define X first
#define Y second

const int MAX_N = 100001;
const int MAX_M = 100001;
const int MOD = 1e9 + 7.5;
const double EPS = 1e-8;

int n;
double a[MAX_N], b[MAX_N];
bool used[MAX_N];

void init(){
    cin >> n;
    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) cin >> b[i];
}

void solve(int ca){
    sort(a, a + n);
    sort(b, b + n);
    int x = 0, y = 0;
    memset(used, 0, sizeof(used));
    for (int i = 0; i < n; i++){
        bool flag = false;
        for (int j = 0; j < n; j++) if (!used[j] && b[j] > a[i]){
            flag = true;
            used[j] = true;
            break;
        }
        if (!flag){
            for (int j = 0; j < n; j++) if (!used[j]){
                used[j] = true;
                break;
            }
            ++x;
        }
    }

    int i = 0, j = 0, las = n - 1;
    for (int i = 0, j = 0; i < n; i++){
        if (a[i] > b[j]){
            ++y;
            ++j;
        }
    }
    printf("Case #%d: %d %d\n", ca, y, x);
}

int main(){
    int ca;
    cin >> ca;
    for (int i = 0; i < ca; i++){
        init();
        solve(i + 1);
    }
    return 0;
}
