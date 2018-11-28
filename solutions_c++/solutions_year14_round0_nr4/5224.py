#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;

vector<double> v, w, e;

const int N = 100010;

int n, ans;
int u[N];
double a[N], b[N];

int judge() {
    int now = 0;
    for(int i = 0; i < v.size(); i++) {
        for(int j = 0; j < w.size(); j++) {
            if(w[j] > v[i]) {
                w.erase(w.begin() + j);
                now++;
                break;
            }
        }
    }
    return now;
}


int judge1() {
    int now = 0;
    for(int i = 0; i < w.size(); i++) {
        for(int j = 0; j < v.size(); j++) {
            if(v[j] > w[i]) {
                v.erase(v.begin() + j);
                now++;
                break;
            }
        }
    }
    return now;
}

void dfs(int x) {
//for(int i = 0; i < n; i++) printf("%lf ", a[i]);
//puts("");
//for(int i = 0; i < n; i++) printf("%lf ", b[i]);
//puts("");
    v.clear();
    for(int i = 0; i < n; i++) {
        v.push_back(a[i]);
    }
    w = e;
    ans = judge();
}

int main() {
    freopen("D-small-attempt3.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int _, cnt = 1;
    scanf("%d", &_);
    while(_--) {
        scanf("%d", &n);
        for(int i = 0; i < n; i++) scanf("%lf", &a[i]);
        for(int i = 0; i < n; i++) scanf("%lf", &b[i]);
        sort(b, b + n);
        e.clear();
        for(int i = 0; i < n; i++) e.push_back(b[i]);
        ans = 0;
        sort(a, a + n);
        dfs(0);
        int p = n - ans;
        w = e;
        printf("Case #%d: %d %d\n",cnt++, judge1(), p);
    }

    return 0;
}
/*
4
1
0.5
0.6
2
0.7 0.2
0.8 0.3
3
0.5 0.1 0.9
0.6 0.4 0.3
9
0.186 0.389 0.907 0.832 0.959 0.557 0.300 0.992 0.899
0.916 0.728 0.271 0.520 0.700 0.521 0.215 0.341 0.458
*/

