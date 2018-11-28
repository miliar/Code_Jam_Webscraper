#include <bits/stdc++.h>
using namespace std;

char str[103];
int main(){
    freopen("small.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int TC, tc = 1;
    scanf("%d", &TC);
    for(tc = 1; tc <= TC; tc++){
        scanf("%s", str + 1);
        int n = strlen(str+1);
        //printf("%d\n",n);
        for(; n >= 1; n--){
            //printf("%d %c\n", n, str[n]);
            if(str[n] != '+')   break;
            str[n] = '\0';
        }
        ///printf("%d\n", n);
        printf("Case #%d: ", tc);
        if(n == 0){
            printf("%d\n", 0);
            continue;
        }
        int cnt = 1;
        for(int i = 2; i <= n; i++){
            if(str[i] != str[i-1]){
                cnt ++;
            }
        }
        printf("%d\n", cnt);
    }
    return 0;
}
