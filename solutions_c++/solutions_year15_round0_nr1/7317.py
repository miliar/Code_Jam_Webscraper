#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <bitset>
#include <string>
#include <map>
#include <queue>
using namespace std;

int T, smax, ans, cursum, tmp;
char ctmp;

int main()
{
//    freopen("input.txt", "r", stdin);
    scanf("%d", &T);
    for (int c = 1; c <= T; c++) {
        scanf("%d", &smax);
        cursum = 0; ans = 0;
        for (int i = 0; i <= smax; i++) {
            scanf(" %c", &ctmp);
            tmp = ctmp - '0';
            if (cursum >= i || tmp == 0) {
                cursum += tmp;
            }
            else {
                ans += i-cursum;
                cursum = i+tmp;
            }
        }
        printf("Case #%d: %d\n", c, ans);
    }
    exit(0);
    return 0;
}