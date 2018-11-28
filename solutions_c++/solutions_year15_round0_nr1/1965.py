#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

int main()
{
    int n, i, j, ans, m, temp;
    char s[1001];
    FILE *fp;
    scanf("%d", &n);
    for(j = 1; j <= n; j++){
        ans = 0;
        temp = 0;
        scanf("%d", &m);
        scanf("%s", s);
        temp = s[0] - '0';
        for(i = 1; i <= m; i++){
            if(s[i] == '0'){
                continue;
            }
            else if(temp >= i){
                temp += s[i] - '0';
                continue;
            }
            else{
                ans += i - temp;
                temp = i + s[i] - '0';
            }
        }
        printf("Case #%d: %d\n", j, ans);
    }
}
