#include <stdio.h>
#include <string>
#include <set>
#include <queue>
#include <algorithm>
using namespace std;

int T, t, i, j, k;
set<string> was;
char s[1000];
queue<pair<string, int> > q;
string ss;

int main() {
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        was.clear();
        while (!q.empty()) q.pop();

        printf("Case #%d: ", t);
        scanf("%s", s);
        was.insert(s);
        q.push(make_pair(s, 0));
        for (;;) {
            ss = q.front().first;
            i = q.front().second;
//            printf("%s %d\n", ss.c_str(), i);
            q.pop();
            for (j = 0; j < (int) ss.size(); j++) if (ss[j] == '-') break;
            if (j == (int) ss.size()) {
                printf("%d\n", i);
                break;
            }
            for (j = 0; j < (int) ss.size(); j++) {
                reverse(ss.begin(), ss.begin() + j + 1);
                for (k = 0; k <= j; k++) {
                    if (ss[k] == '+') ss[k] = '-';
                    else ss[k] = '+';
                }
                if (was.insert(ss).second) q.push(make_pair(ss, i+1));
                for (k = 0; k <= j; k++) {
                    if (ss[k] == '+') ss[k] = '-';
                    else ss[k] = '+';
                }
                reverse(ss.begin(), ss.begin() + j + 1);
            }
        }
    }
    return 0;
}
