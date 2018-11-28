#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <complex>
#include <cstring>
#include <cstdio>

using namespace std;

int T, n;

int a[10][10], b[10][10];
int la[20], lb[20];

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin>>T;
    int cs = 0;
    while (T--) {
        int fst, snd;
        cin>>fst; --fst;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                cin>>a[i][j];
        cin>>snd; --snd;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                cin>>b[i][j];
        memset(la, 0, sizeof(la));
        for (int i = 0; i < 4; i++)
            ++la[a[fst][i]];
        vector<int> ans;
        for (int i = 0; i < 4; i++)
            if (la[b[snd][i]]) ans.push_back(b[snd][i]);
        printf("Case #%d: ", ++cs);
        if (ans.size() == 0) {
            puts("Volunteer cheated!");
        } else if (ans.size() > 1) puts("Bad magician!");
        else printf("%d\n", ans[0]);
    }
    return 0;
}
