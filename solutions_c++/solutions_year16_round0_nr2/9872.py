#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.txt","w",stdout);

    int t;
    char str[110];
    scanf("%d",&t);
    for(int T=1;T<=t;T++) {
        int size = 0, ans = 0;
        scanf("%s",str);
        string st = str;
        st += '+';
        //printf("%s\n",st.c_str());
        for(int i=1;i<st.size();i++) {
            if(st[i] != st[i-1]) {
                size = 0;
                ans++;
            }
        }
        printf("Case #%d: %d\n",T,ans);
    }
    return 0;
}
