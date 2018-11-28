#include <cstdio>
#include <string>

using namespace std;
char buf[1002];
int main() {
    int C;
    scanf("%d", &C);
    for ( int tt = 1; tt <= C; tt++ ) {
        scanf("%s", buf);
        string s = buf;
        string t;
        for ( int i = 0; i < s.size(); i++ ) {
            char c = s[i];
            if ( t + c > c + t ) {
                t.push_back(c);
            } else {
                t = c + t;
            }
        }
        printf("Case #%d: %s\n", tt, t.c_str());
    }
    return 0;
}
