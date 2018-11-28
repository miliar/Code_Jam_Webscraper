#include <stdio.h>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

int T, t, i, j, k, n;
char s[1003];
string res;

int main() {
    scanf("%d", &T);
    for (t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        scanf("%s", s);
        n = strlen(s);
        res = "";
        res += s[0];
        for (i = 1; i < n; i++) {
            if (res[0] <= s[i]) res = s[i] + res;
            else res += s[i];
        }
        printf("%s\n", res.c_str());
    }
    return 0;
}
