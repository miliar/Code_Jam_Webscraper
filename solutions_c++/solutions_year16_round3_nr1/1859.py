#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

#define FIN freopen("A-large.in", "r", stdin)
#define FOUT freopen("A-large.out", "w", stdout)
//#define FIN freopen("in.ads", "r", stdin)
//#define FOUT freopen("A-small-attempt0.out", "w", stdout)

const int N = 27;

void work() {
    int n;
    pair<int, char> a[N];
    scanf("%d", &n);
    int sum = 0;
    for(int i = 0; i < n; ++i) {
        scanf("%d", &a[i].first);
        a[i].second = 'A' + i;
        sum += a[i].first;
    }
    vector<string> ans;
    while(sum != 0) {
        sort(a, a + n);
        int r = a[n - 1].first;
        int rr = a[n - 2].first;
        string chose = "";
        if(r == 1 && sum != 2) {
            chose = string(1, a[n - 1].second);
            a[n - 1].first -= 1;
        }
        else if(r >= rr + 1) {
            if(r >= 2) {
                chose = string(2, a[n - 1].second);
                a[n - 1].first -= 2;
            }
            else {
                chose = string(1, a[n - 1].second);
                a[n - 1].first -= 1;
            }
        }
        else {
            chose = string(1, a[n - 1].second) + string(1, a[n - 2].second);
            a[n - 1].first -= 1;
            a[n - 2].first -= 1;
        }
        sum -= int(chose.size());
        ans.push_back(chose);
    }
    for(int i = 0; i < (int)ans.size(); ++i) {
        printf(" %s", ans[i].c_str());
    }
}

int main() {
    FIN;
    FOUT;
    int T, ncase = 0;
    scanf("%d", &T);
    while(T--) {
        printf("Case #%d:", ++ncase);
        work();
        puts("");
    }
    return 0;
}
