#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 1100;

char s[MAXN];
int n, ans, m, t;

int main(){
    scanf("%d", &t);
    for (int k = 1; k <= t; ++k){
        scanf("%d%s", &m, s);
        ++m;

        ans = s[0] - '0';
        int calc = 0;
        for (int i = 1; i < m; ++i){
            if (i > ans){
                calc += i - ans;
                ans = i;
            }
            ans += (s[i] - '0');
        }
        printf("Case #%d: %d\n", k, calc);
    }
    return 0;
}
