#include <bits/stdc++.h>
using namespace std;

const int N=1e3+10;
char s[N];

int main() {
    int n, t, T=1;
    scanf("%d", &t);
    while(t--) {
        int sum=0, ans=0;
        scanf("%d %s", &n, s);
        for(int i=0; i<=n; i++) {
            if(sum<i && s[i]!='0') {
                ans+=i-sum;
                sum+=i-sum;
            }
            sum+=(s[i]-'0');
        }
        printf("Case #%d: %d\n", T++, ans);
    }
    return 0;
}
