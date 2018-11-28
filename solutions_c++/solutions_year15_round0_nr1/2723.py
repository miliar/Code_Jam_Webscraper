# include <iostream>
# include <cstdio>
# include <cstring>

using namespace std;

int sm;
char s[1200];
int c[1200];

bool check() {
    int s = 0;
    for(int i = 0; i <= sm; ++i) {
        if(s < i) return false;
        s += c[i];
    }
    return true;
}

int main() {
    int T; cin >> T;
    for(int k = 1; k <= T; ++k) {
        int ans = 0;
        scanf("%d%s", &sm, s);
        for(int i = 0; i <= sm; ++i) c[i] = s[i] - '0';
        while(!check()) { 
            c[0] += 1; ans += 1;
        }
        printf("Case #%d: %d\n", k, ans);
    }
}

