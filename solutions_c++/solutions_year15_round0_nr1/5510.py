#include <bits/stdc++.h>

using namespace std;
const int MAXN = 1000;

int t, n;
char word[MAXN + 5];

int main() {
    scanf("%d", &t);
    for(int i = 1; i <= t; ++i) {
        scanf("%d", &n);
        for(int j = 0; j <= MAXN; ++j) word[j] = 0;
        scanf("%s", word);
        int act = 0, res = 0;
        for(int j = 0; j <= n; ++j) {
            int num = word[j] - '0';
            int tmp = j - act;
            if(act < j) {
                res += tmp;
                act += tmp;
            }
            act += num;
        }
        printf("Case #%d: %d\n", i, res);
    } 
    return 0;
}
