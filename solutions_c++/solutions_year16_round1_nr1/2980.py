#include <stdio.h>
#include <deque>

const int N = 1010;

int main()
{
    int t;
    scanf("%d", &t);
    char s[N];
    for (int cases = 1; cases <= t; cases++) {
        scanf("%s", s);
        std::deque<char> ans;
        ans.push_back(s[0]);
        for (int i = 1; s[i]; i++) {
            if (s[i] >= ans.front()) {
                ans.push_front(s[i]);
            } else {
                ans.push_back(s[i]);
            }
        }
        printf("Case #%d: ", cases);
        for (size_t i = 0; i < ans.size(); i++) {
            printf("%c", ans[i]);
        }
        printf("\n");
    }
    return 0;
}
