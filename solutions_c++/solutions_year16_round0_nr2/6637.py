#include <bits/stdc++.h>
using namespace std;

#define eprintf(...) fprintf(stderr,__VA_ARGS__)

const int N=100010;
const int INF=1e9;
const int Mod=1e9+7;

int main() {
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int tc; scanf("%d",&tc);
    for(int t=1;t<=tc;t++) {
        char s[111];
        scanf("%s",s);
        int n=strlen(s);
        bool inv=false;
        int cnt=0;
        for(int i=n-1;i>=0;i--) {
            if(!inv) {
                if(s[i]=='-') cnt++,inv=true;
            } else {
                if(s[i]=='+') cnt++,inv=false;
            }
        }
        printf("Case #%d: %d\n",t,cnt);
    }
    return 0;
}
