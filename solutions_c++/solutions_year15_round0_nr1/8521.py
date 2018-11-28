#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
int t,n;
char word[1005];
int main(){
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    int ca = 1;
    scanf("%d", &t);
    while(t--){
        scanf("%d", &n);
        scanf("%s", word);
        int ans = 0;
        int cur = 0;
        for(int i = 0; i <= n; i++){
            if(cur >= i){
                cur += word[i]-'0';
            }else{
                ans += (i-cur);
                cur = i;
                cur += word[i]-'0';
            }
        }
        printf("Case #%d: %d\n", ca++,ans);
    }
    return 0;
}
