#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<stdlib.h>
using namespace std;

int main(){
    int T, n, m, s[101][101], t[101][101];
    scanf("%d",&T);
    for(int tt=1; tt<=T; tt++){
        scanf("%d%d",&n,&m);
        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++) scanf("%d",&s[i][j]);
        }

        bool same = false;
        while( true ){
            int v = s[0][0], minv = s[0][0], row_minv = s[0][0], col_minv = s[0][0];
            same = true;
            for(int i=0; i<n; i++){
                for(int j=0; j<m; j++){
                    if( minv>s[i][j] ) minv = s[i][j];
                    if( s[i][j]!=v ) same = false;
                }
            }
            if( same ) break;

            for(int i=0; i<n; i++) if( row_minv>s[i][0] ) row_minv = s[i][0];
            for(int j=0; j<m; j++) if( col_minv>s[0][j] ) col_minv = s[0][j];
            //cout<<minv<<" "<<row_minv<<" "<<col_minv<<endl;
            //scanf("%d",&T);

            bool go = false;
            if( row_minv==minv || col_minv==minv ){
                memset( t, 0, sizeof(t) );
                for(int i=0; i<n; i++){
                    if( s[i][0]==minv ){
                        bool ok = true;
                        for(int j=0; j<m; j++) if( s[i][j]!=minv ) ok = false;
                        if( ok ){
                            go = true;
                            for(int j=0; j<m; j++) t[i][j] = 1;
                        }
                    }
                }
                for(int j=0; j<m; j++){
                    if( s[0][j]==minv ){
                        bool ok = true;
                        for(int i=0; i<n; i++) if( s[i][j]!=minv ) ok = false;
                        if( ok ){
                            go = true;
                            for(int i=0; i<n; i++) t[i][j] = 1;
                        }
                    }
                }
                
                if( !go ) goto end;
                for(int i=0; i<n; i++) for(int j=0; j<m; j++) s[i][j] += t[i][j];
            }else break;

            /*for(int i=0; i<n; i++){
                for(int j=0; j<m; j++) printf(" %d",s[i][j]); printf("\n");
            }*/
        }
        end:
        if( same ) printf("Case #%d: YES\n",tt);
        else printf("Case #%d: NO\n",tt);
    }
    return 0;
}

