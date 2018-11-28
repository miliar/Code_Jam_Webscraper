#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

int T;
char tmp[6], S[1002];

int solve() {
    int n = strlen(S);
    int res = 0, stand = 0;
    for(int i = 0; i < n; i++) {
        if(S[i] == '0') continue;
        if(i > stand) res += i - stand, stand += i - stand + S[i] - '0';
        else stand += S[i] - '0';
        //cout << stand << endl;
    }
    return res;
}

int main () {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    scanf(" %d ", &T);
    for(int i = 1; i <= T; i++) {
        scanf("%s", &tmp);
        scanf("%s", &S);
        printf("Case #%d: %d\n", i, solve());
    }
    return 0;
}
