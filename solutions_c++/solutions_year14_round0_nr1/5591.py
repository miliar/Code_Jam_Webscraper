#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <math.h>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <string>
#include <string.h>
#include <sstream>
#include <stdlib.h>

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

int main() {
    int _T;
    scanf("%d\n", &_T);

    for (int _ = 1; _ <= _T; _++) {
        printf("Case #%d: ", _);

        int first, second;
        cin >> first;
        map<int, int> f,s;
        for (int i = 1; i <= 4; ++i) {
            for (int j = 1; j <= 4; ++j) {
                int x; cin >> x;
                f[x] = i;
            }
        }
        cin >> second;
        for (int i = 1; i <= 4; ++i) {
            for (int j = 1; j <= 4; ++j) {
                int x; cin >> x;
                s[x] = i;
            }
        }

        int best = -1;
        for (int i = 1; i <= 16; ++i) {
            if (f[i] == first && s[i] == second) {
                if (best == -1) best = i;
                else best = -2;
            }
        }
        if (best == -1) puts("Volunteer cheated!");
        else if (best == -2) puts("Bad magician!");
        else cout << best << endl;
    }
    
    return 0;
}
