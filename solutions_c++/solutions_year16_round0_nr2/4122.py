#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

char buf[256];
string s;

int solve(int x) {
    char c = s[x];
    int i = x;
    while ( i < s.size() && s[i] == c ) i++;
    if ( i == s.size() ) {
        return c == '-' ? 1 : 0;
    } else {
        return 1 + solve(i);
    }
}

int main() {
    int T;
    scanf("%d", &T);
    for ( int t = 1; t <= T; t++ ) {
        scanf("%s", buf);
        s = buf;
        printf("Case #%d: %d\n", t, solve(0));
    }
    return 0;
}
