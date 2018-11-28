#include <bits/stdc++.h>
using namespace std;

const int MAX = 1111;
int test, n, k, res;
char s[MAX];

int main(){
    //freopen("in.txt", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &test);
    for (int tt = 1; tt <= test; ++tt){
        scanf("%s %d", s, &k);
        n = strlen(s);
        res = 0;
        for (int i = 0; i < n; ++i)
        if (s[i] == '-')
        if (i + k - 1 >= n){
            res = -1;
            break;
        }
        else{
            ++res;
            for (int j = i; j < i + k; ++j)
                s[j] = (s[j] == '-' ? '+' : '-');
        }
        if (res == -1)
            printf("Case #%d: IMPOSSIBLE\n", tt);
        else
            printf("Case #%d: %d\n", tt, res);
    }
    return 0;
}
