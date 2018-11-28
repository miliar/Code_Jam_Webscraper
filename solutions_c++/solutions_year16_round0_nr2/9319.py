#include <bits/stdc++.h>
using namespace std;
char s[105];
int N,T;
void flip(int x) {
    for (int i=0; i<=x; i++){
        if (s[i] == '-') s[i] = '+';
        else s[i] = '-';
    }
    reverse(s,s+x+1);
}
int main(){
    scanf("%d",&T);
    for (int tt=1; tt<=T; tt++){
        scanf(" %s",s);
        N = strlen(s);
        int ans=0,b = N-1;
        while (b >= 0){
            while (b >= 0 && s[b] == '+') b--;
            if (b < 0) break;
            if (s[0] == '-') {
                flip(b);
            } else {
                int f = 0;
                while (f < N && s[f] == '+') f++;
                flip(f-1);
            }
            ans++;
        }
        printf("Case #%d: %d\n",tt,ans);
    }
}
