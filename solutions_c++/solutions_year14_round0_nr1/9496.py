#include <cstdio>
#include <iostream>
#include <map>
#include <vector>
#include <queue>
#include <cstring>
using namespace std;

int n;
int f[4][4];
vector<int> v1, v2;
int main() {
    freopen("D:\\data.in", "r", stdin);
    freopen("D:\\data.out", "w", stdout);
    int cas, t = 0;
    cin >> cas;
    while (cas--) {
        int pos;
        cin >> pos;
        pos--;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                cin >> f[i][j];
        v1.clear();
        for (int i = 0; i < 4; i++)
            v1.push_back(f[pos][i]);
        cin >> pos;
        pos--;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                cin >> f[i][j];
        v2.clear();
        for (int i = 0; i < 4; i++) {
            bool flag = false;
            for (int j = 0; j < v1.size(); j++)
                if (v1[j] == f[pos][i]) {
                    flag = true;
                    break;
                }
            if (flag)v2.push_back(f[pos][i]);
        }
        if (v2.size() == 1)printf("Case #%d: %d\n", ++t, v2[0]);
        else if (v2.size() == 0)printf("Case #%d: Volunteer cheated!\n", ++t);
        else printf("Case #%d: Bad magician!\n", ++t);
    }
    return 0;
}