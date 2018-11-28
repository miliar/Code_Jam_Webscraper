#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
using namespace std;
#define esp 1e-9
typedef long long LL;
const int MOD = 1e9+7;
char s[1010];
char ans[10000];
int main()
{
    int T;
    scanf("%d", &T);
    while (T--) {
        scanf("%s", s);
        int head, tail;
        head = tail = 5000;
        ans[tail++] = s[0];
        for (int i = 1; s[i]; ++i) {
            ans[--head] = s[i];
            ans[tail++] = s[i];
            bool flag = 0;
            for (int j = head; j < tail - 1; ++j)
                if (ans[j] > ans[j+1]) {
                    tail--;
                    flag = 1;
                    break;
                }
                else if (ans[j] < ans[j+1]) {
                    head++;
                    flag = 1;
                    break;
                }
            if (!flag) tail--;
        }
        ans[tail] = '\0';
        static int cas = 1;
        printf("Case #%d: %s\n", cas++, ans + head);
    }
    return 0;
}

