#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

int T;


void solve(int ca){
    int n;
    char str[1010];
    scanf("%d",&n);
    scanf("%s",str);
    int s = 0;
    int ans = 0;
    for (int i = 0; i <= n; i++){
        if (s < i){
            ans += i - s;
            s = i;
        }
        s += str[i] - '0';
    }
    printf("Case #%d: %d\n",ca,ans);
}

int main(){
    scanf("%d",&T);
    for (int ca = 1; ca <= T; ca++){
        solve(ca);
    }

}
