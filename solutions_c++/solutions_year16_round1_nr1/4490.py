#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <climits>
#include <complex>
#include <fstream>
#include <cassert>
#include <cstdio>
#include <bitset>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <ctime>
#include <set>
#include <map>
#include <cmath>

using namespace std;

const int maxn = 1111;
char s[maxn];
deque<char> dq;

int main() {
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int _ = 1; _ <= T; _++) {
        scanf("%s", s);
        dq.clear();
        for(int i = 0; s[i]; i++) {
            if(dq.front() > s[i]) {
                dq.push_back(s[i]);
            }
            else {
                dq.push_front(s[i]);
            }
        }
        printf("Case #%d: ", _);
        while(!dq.empty()) {
            printf("%c", dq.front());
            dq.pop_front();
        }
        printf("\n");

    }
    return 0;
}