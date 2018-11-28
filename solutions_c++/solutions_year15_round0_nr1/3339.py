/*************************************************************************
	> File Name: ./qua_A.cpp
	> Author: 
	> Mail: 
	> Created Time: 2015年04月11日 星期六 20时27分41秒
 ************************************************************************/

#include <cstdio>
#include <iostream>

using namespace std;

const int maxn = 1000 + 20;
char str[maxn];

int main() {
    int T;

    scanf("%d", &T);
    for(int kase = 1; kase <= T; kase++) {
        int n;
        scanf("%d", &n);
        scanf("%s", str);
        int stand = str[0] - '0';
        int need = 0;
        for(int i = 1; i <= n; i++) {
            if(stand < i) {
                need += i - stand;
                stand = i;
            }
            stand += str[i] - '0';
        }
        printf("Case #%d: %d\n", kase, need);
    }

    return 0;
}
