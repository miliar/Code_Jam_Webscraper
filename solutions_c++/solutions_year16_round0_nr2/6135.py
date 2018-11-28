#include<bits/stdc++.h>

using namespace std;

char s[507];

int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);

    int tc;cin>>tc;
    for( int cas=1; cas<=tc; cas++ ) {
        scanf("%s",s);
        char ager = 'A';
        int OK = 0;
        int cnt = 0;
        int suru = strlen( s );
        for(int i=suru-1; i>=0; i--) {
            if( s[i]=='-' ) OK = 1;
            if( OK && ager!=s[i] ) cnt++;
            ager = s[i];
        }
        printf("Case #%d: %d\n",cas,cnt);
    }


    return 0;
}
