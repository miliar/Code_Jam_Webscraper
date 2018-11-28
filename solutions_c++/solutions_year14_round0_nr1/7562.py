#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <cstdlib>
#include <ctype.h>
#include <cstring>
#include <string>
#include <ctime>
#include <cassert>
#include <utility>

using namespace std;

int v[16];

void initializare() {
    for(int i = 0; i < 16; i++) {
        v[i] = 0;
    }
}

int main() {
//	freopen("date.in", "r", stdin);
//	freopen("date.out","w", stdout);
    int t, ans1, ans2, init[4][4], sec[4][4];

    cin >> t;
    for(int ti = 1; ti <= t; ti++) {
        // citirea datelor de intrare
        initializare();
        cin >> ans1;
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++) {
                cin >> init[i][j];
                v[init[i][j]-1] = v[init[i][j]-1] * 10 + i;
            }
        cin >> ans2;
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++) {
                cin >> sec[i][j];
                v[sec[i][j]-1] = v[sec[i][j]-1] * 10 + i;
            }

        int posAsk = ((ans1 - 1) * 10) + (ans2 - 1);
        int cnt = 0, x;
        for(int i = 0; i < 16; i++) {
            if(v[i] == posAsk) {
                x = i + 1;
                cnt++;
            }
        }
        if(cnt == 1) {
            printf("Case #%d: %d\n", ti, x);
        }
        else if(cnt > 1) {
            printf("Case #%d: Bad magician!\n", ti);
        } else {
            printf("Case #%d: Volunteer cheated!\n", ti);
        }
    }

	return 0;
}
