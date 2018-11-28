#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

int go[4][4] = {{1, 2, 3, 4}, {2, -1, 4, -3}, {3,-4, -1, 2}, {4, 3, -2, -1}};

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int test = 1; test <= T; ++test) {
        int L, X;
        scanf("%d%d", &L, &X);
        string s;
        cin >> s;
        int cur = 1;
        int cnt = 0;
        for (int i = 0; i < X; ++i) {
            for(int j = 0; j < L; ++j) {
                int c = s[j] - 'i' + 2;
              //  cerr << cur << " " << cnt << "  " << c << endl;
              
                if (cur < 0) {
                    cur = -1* go[-cur - 1][c - 1];
                } else {
                    cur = go[cur - 1][c - 1];
                }
                if (cur == 2 && cnt == 0){
                    ++cnt;
                    cur = 1;
                }
                if (cur == 3 && cnt == 1){
                    ++cnt;
                    cur = 1;
                }
                 if (cur == 4 && cnt == 2){
                    ++cnt;
                    cur = 1;
                }
            }
        }
        //cerr << "-----" << endl;
        if (cnt == 3 && cur == 1)  {
            printf("Case #%d: YES\n", test);
        } else {
            printf("Case #%d: NO\n", test);
        }
    }
}