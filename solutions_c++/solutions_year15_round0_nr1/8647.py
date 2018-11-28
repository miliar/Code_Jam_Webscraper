#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-input.txt", "r", stdin);
    freopen("A-output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int t=1; t<=T; t++){
        int n;
        scanf("%d", &n);
        char s[10000];
        scanf("%s", s);
        int total = 0;
        int output = 0;
        for(int i=0; i<=n; i++){
            if (s[i] == '0') continue;
            if (total < i){
                output += i - total;
                total = i;
            }
            total += s[i] - '0';
        }
        printf("Case #%d: %d\n", t, output);
    }
    return 0;
}
