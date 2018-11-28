#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int main(){
    int T, n;
    char inp[100000];
    scanf("%d", &T);
    int f = 0;
    while(T--){
        scanf("%d %s", &n, inp);
        int ans = 0, now = 0;
        for(int i=0;i<=n;i++){
            if(now < i){
                ans += i - now;
                now = i;
            }
            now += inp[i] - '0';
        }

        printf("Case #%d: %d\n", ++f, ans);
    }

    

    return 0;
}
