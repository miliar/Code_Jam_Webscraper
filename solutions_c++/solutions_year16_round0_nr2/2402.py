/*
* @Author: Comzyh
* @Date:   2016-04-09 21:06:30
* @Last Modified by:   Comzyh
* @Last Modified time: 2016-04-09 21:41:45
*/

#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int T;
char str[109];
int main()
{
    scanf("%d", &T);
    for (int TT = 1; TT <= T; TT++)
    {
        scanf("%s", str);
        int len = strlen(str);
        int ans = 0;
        for (int i = 1; i < len; i++)
            ans += str[i] != str[i - 1];
        ans += str[len - 1] == '-';
        printf("Case #%d: %d\n", TT, ans);
    }
    return 0;
}