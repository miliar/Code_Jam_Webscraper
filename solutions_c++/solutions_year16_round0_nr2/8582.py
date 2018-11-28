#include <bits/stdc++.h>
using namespace std;

char s[105];

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large-out","w",stdout);
    int test,no = 0; scanf("%d",&test);
    while(test--){
        scanf("%s",s);
        int sz = strlen(s) - 1;
        int ans = 0, cnt = 0;
        for(int i=sz;i>=0;i--){
            if(i < sz && s[i] == s[i+1]) continue;
            if(cnt&1){
                if(s[i] == '+') cnt++;
            }else{
                if(s[i] == '-') cnt++;
            }
        }
        printf("Case #%d: %d\n",++no,cnt);
    }
    return 0;
}
