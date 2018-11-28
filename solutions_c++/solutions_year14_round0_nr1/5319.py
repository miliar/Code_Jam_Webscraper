#include <cassert>
#include <cstring>
#include <cstdio>
#include <iostream>
#include <map>
using namespace std;

int T, x;
int r;
map<int, int> pos;

int main() {
    int i, j, k;
    cin>>T;
    for (int t = 1; t <= T; ++t) {
        pos.clear();
        cin>>r;
        for (i = 1; i <= 4; ++i) {
            for (j = 1; j <= 4; ++j) {
                cin>>x;
                if (i==r) pos[x] = 0;
            }
        }

        cin>>r;
        for (i = 1; i <= 4; ++i) {
            for (j = 1; j <= 4; ++j) {
                cin>>x;
                if (pos.find(x) != pos.end()) {
                    pos[x] = i;
                }
            }
        }

        int cnt = 0;
        int ans = 0;
        for (map<int, int>::iterator it = pos.begin(); it != pos.end(); ++it) {
            if (it->second == r) {
                ans = it->first;
                cnt++;
            }
        }
                
        printf("Case #%d: ", t);
        if (cnt == 0) {
            puts("Volunteer cheated!");
        } else if (cnt > 1) {
            puts("Bad magician!");
        } else {
            assert(ans!=0);
            printf("%d\n", ans);
        }
    }
    return 0;
}
