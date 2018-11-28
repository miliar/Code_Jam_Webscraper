#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
//#include <memory>
//#include <thread>
using namespace std;


#define INF 1e+9
#define mp make_pair
#define lint long long
#define pii pair<int, int>

vector<pair<char, int> > map(char * s) {
    vector<pair<char, int> > ans;
    for (int i = 0; s[i] != '\0'; i++) {
        if (ans.empty() || ans[ans.size() - 1].first != s[i]) {
            ans.push_back(mp(s[i], 1));
        } else {
            ans[ans.size() - 1].second++;
        }
    }
    return ans;
}

char buffer[200];
int opt[200];
int tmp[200];

vector<pair<char, int> > maps[200];

int main() {
    ios_base::sync_with_stdio(false);
    int t; scanf("%d\n", &t);
    for (int i = 0; i < t; i++) {
        int n; scanf("%d\n", &n);
        for (int i = 0; i < n; i++) {
            gets(buffer);
            maps[i] = map(buffer);
        }
        bool fail = false;
        for (int i = 0; i < n; i++) {
            if (maps[i].size() != maps[0].size()) fail = true; 
        }
        if (fail) {
            printf("Case #%d: Fegla Won\n", i + 1);
            continue;
        }
        for (int i = 0; i < maps[0].size(); i++) {
            memset(tmp, 0, sizeof tmp);
            for (int j = 0; j < n; j++) {
                if (maps[j][i].first != maps[0][i].first) {
                    fail = true;
                    break;
                }
                tmp[maps[j][i].second]++;
            }
            if (fail) break;
            int ii = -1, sum = 0;;
            while (sum <= n/2) {
                sum += tmp[++ii];
            }
            opt[i] = ii;
        }
        if (fail) {
            printf("Case #%d: Fegla Won\n", i + 1);
            continue;
        }
        long long sum = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < maps[i].size(); j++) {
                sum += abs(maps[i][j].second - opt[j]);
            }
        }
        printf("Case #%d: %lld\n", i + 1, sum);
    }
}
