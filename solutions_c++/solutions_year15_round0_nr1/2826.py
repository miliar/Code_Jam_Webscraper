#include <bits/stdc++.h>

const int N = 1000 + 5;
int n;
char str[N];

int main(int argc,char **args) {
    if (argc > 1) {
        freopen(args[1],"r",stdin);
        freopen("data.out","w",stdout);
    }
    int cas,ca = 0;
    scanf("%d",&cas);
    while (cas--) {
        scanf("%d%s",&n,str);
        int answer = 0;
        int sum = 0;
        for (int i = 0; i <= n; ++ i) {
            int c = str[i] - '0';
            if (c == 0) continue;
            if (sum < i) {
                answer += i - sum;
                sum = i;
            }
            sum += c;
        }
        printf("Case #%d: %d\n",++ca,answer);
    }
}
