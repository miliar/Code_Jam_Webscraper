#include <bits/stdc++.h>

#define LL long long
#define INF 0x3f3f3f3f
#define eps 1e-8

using namespace std;

char s[105];
int main(){
#ifndef ONLINE_JUDGE
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif // ONLINE_JUDGE
    int T;
    scanf("%d", &T);
    int cas = 0;
    while(T--){
        scanf("%s", s + 1);
        bool jian = false, jia = false;
        int p = 1, len = strlen(s + 1);
        int ans = 0;
        while(p <= len){
            while(p <= len && s[p + 1] == s[p]){
                ++p;
            }
            if(s[p] == '-'){
                if(jia){
                    ans += 2;
                    jia = false;
                }
                else{
                    ++ans;
                }
            }
            if(s[p] == '+'){
                jia = true;
            }
            ++p;
        }
        printf("Case #%d: %d\n", ++cas, ans);

    }
}
