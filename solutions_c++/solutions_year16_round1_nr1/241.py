#include <cstdio>
#include <cstring>
#include <algorithm>
#include <list>
using namespace std;

char s[1010], ans[1010];

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%s", s);
        list<char> l;
        l.push_back(s[0]);
        for (int i = 1; s[i]; i++) {
            if (s[i] >= l.front())
                l.push_front(s[i]);
            else
                l.push_back(s[i]);
        }
        printf("Case #%d: ", t);
        for (auto it = l.begin(); it != l.end(); it++)
            putchar(*it);
        puts("");
    }
}
