#include <bits/stdc++.h>
#define rep(i,a,b) for (int i=(a); i<=(b); i++)
using namespace std;
const int MAX_N = 7 + 1000;
const int INF = 7 + 1000000000;
///----------------------------------------------
char str[MAX_N];
int dig[MAX_N];
int main() {

    freopen ( "xx.in"  , "r" , stdin  );
    freopen ( "xx.out" , "w" , stdout );

    int tcase;
    int icase=0;
    for (scanf("%d",&tcase); ++icase<=tcase; ) {

        ///init

        ///read
        scanf(" %s",str); int len=strlen(str);
        int k; scanf("%d",&k);
        rep(i,0,len-1) dig[i]=str[i]=='+';

        ///work
        int ans=0;
        rep(i,0,len-1-k+1) if (!dig[i]) {
            ans++; rep(j,0,k-1) dig[i+j]^=1;
        }
        rep(i,len-k+1,len-1) if (!dig[i]) {
            ans=INF; break;
        }

        ///print
        printf("Case #%d: ",icase);
        if (ans==INF) printf("IMPOSSIBLE\n");
            else printf("%d\n",ans);

    }
}







