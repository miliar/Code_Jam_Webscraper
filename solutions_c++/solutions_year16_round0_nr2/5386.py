#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <cstring>
#include <array>

using namespace std;

typedef unsigned long long ll;

char S[101];
int L;
int ans;

inline char flip(char c) {
    return (c=='+')?'-':'+';
}

void flip(int start_idx) {
    int i = 0;
    while (i <= start_idx) {
        char t = S[i];
        S[i] = flip(S[start_idx]);
        S[start_idx] = flip(t);
        i++;
        start_idx--;
    }
    ans++;
}

int main(int argc, const char * argv[]) {
    freopen(argv[1], "r", stdin);
    
    int T; scanf("%d\n",&T);
    for (int t = 1; t<=T; ++t) {
        memset(S, 0, sizeof(S));
        gets(S);
        L = (int)strlen(S);
        ans = 0;
        int i = L-1;
        while(i>=0) {
            while(i>=0 && S[i]=='+') { i--; }
            if (i<0) {
                printf("Case #%d: %d\n", t, ans);
            } else if (S[0]=='-') {
                flip(i);
            } else {
                int j = i-1;
                while(j>0 && S[j]=='-') j--;
                flip(j);
                flip(i);
            }
        }
    }

    return 0;
}
