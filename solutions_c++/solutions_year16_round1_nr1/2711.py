#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;

char s[1024];

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T; scanf("%d", &T);

    for(int ncase=1; ncase<=T; ncase++) {
        scanf("%s", s);
        int len = strlen(s);
        deque<char> q; q.push_back(s[0]);
        for(int i=1; i<len; i++) {
            if (q.front() > s[i]) q.push_back(s[i]);
            else q.push_front(s[i]);
        }

        printf("Case #%d: ", ncase);
        while(!q.empty()) {
            printf("%c", q.front());
            q.pop_front();
        }
        printf("\n");
    }

    return 0;
}
