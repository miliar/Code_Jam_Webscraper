#include"bits/stdc++.h"
using namespace std;
char a[1050];
int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int n, k;
    cin >> n;
    for(int i = 1; i <= n; i ++){
        cin >> a >> k;
        int len = strlen(a);
        int cnt = 0;
        for(int j = 0; j <= len - k; j ++){
            if(a[j] == '-'){
                cnt ++;
                for(int p = j; p < j + k; p ++){
                    if(a[p] == '-') a[p] = '+';
                    else a[p] = '-';
                }
            }
        }
        for(int i = 0; i < len; i ++){
            if(a[i] == '-'){
                cnt = -1;
            }
        }
        if(cnt == -1){
            printf("Case #%d: IMPOSSIBLE\n", i);
        }
        else{
            printf("Case #%d: %d\n", i, cnt);
        }
    }
    return 0;
}
