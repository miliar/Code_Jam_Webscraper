#include <cstdio>
#include <cassert>
#include <algorithm>
using namespace std;

int T;
const int MAXT = 100;
const int MAXS = 1005;
int Smax;
int S[MAXS+1];

bool works(int f) {
    int standing = f;
    int s = 0;
    while(s <= Smax) {
        if (standing < s) {
            return false;
        }
        standing += S[s];
        s++;
    }
    return true;
}

int main() {
    scanf("%d",&T);
    for(int t = 1; t <= T; t++) {
        scanf("%d ", &Smax);
        char c;
        for(int s = 0; s <= Smax; s++) {
            scanf("%c", &c);
            S[s] = c - '0';
        }
        scanf("%c", &c);
        assert(c == '\n');
        int ans;
        for(ans = 0; ans <= MAXS; ans++) {
            if (works(ans)) {
                break;
            }
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}

