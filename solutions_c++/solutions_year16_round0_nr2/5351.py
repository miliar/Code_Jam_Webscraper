#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

char s[150];
int main()
{
    #ifdef LOCAL
//    freopen("in.txt", "r", stdin);
//    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    #endif // LOCAL
    int T;
    T = 100;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++) {
        printf("Case #%d: ", cas);
        scanf("%s", s);
        int n = strlen(s), res = 0;
        for(int i = 0, j; i < n; ) {
            if(s[i] == '+') {
                i++;
                continue;
            }
            j = i;
            while(s[j] == '-') j++;
            if(!i)  res ++;
            else    res += 2;
            i = j;
        }
        printf("%d\n", res);
    }
    return 0;
}
