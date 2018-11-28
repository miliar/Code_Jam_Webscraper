#include<algorithm>
#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
char s[1005];
int main() {
    int T ,cas;
    cas = 1;
    freopen("B-large.in","r",stdin);
    freopen("a.out","w",stdout);
    cin >> T;
    while(T--) {
        scanf("%s", s);
        int len = strlen(s);
        int ans = 0;
        for(int i=len-1; i>=0; --i) {
            if(s[i] == '-') {
                ans++;
                for(int j=0; j<=i; ++j) {
                    if(s[j] == '+') s[j] = '-';
                    else s[j] = '+';
                }
            }
        }
        printf("Case #%d: ", cas++);
        cout << ans << endl;
    }
    return 0;
}
