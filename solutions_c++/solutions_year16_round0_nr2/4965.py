#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string.h>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for (int ca = 1; ca <= t; ca++) {
        char str[110];
        scanf("%s",str);
        int len = strlen(str);
        int ans = 0;
        int flag = 0;
        for(int i = 1; i < len; i++) {
            if(str[i] != str[i-1]){
                if ((str[i] == '+') && !flag) {
                    ans += 1;
                    flag = 1;
                } else if(str[i] == '-'){
                    ans += 2;
                    flag = 1;
                }
            }
        }
        if(!flag && str[0] == '-')ans++;
        printf("Case #%d: %d\n",ca,ans);
    }
    return 0;
}
