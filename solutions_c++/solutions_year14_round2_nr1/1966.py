/*
 *ID:   Cowboy
 *TASK:
 *Judge:
 */
#include <bits/stdc++.h>
#define INF 0x7fffffff
#define PI 2*acos(0.0)
using namespace std;

#define PB(t) push_back(t)
#define ALL(t) t.begin(),t.end()
#define MP(x, y) make_pair((x), (y))
#define Fill(a,c) memset(&a, c, sizeof(a))

int main( ){
    freopen("A-small.in","r",stdin);
    freopen("solution.out","w",stdout);
    int T, k = 0, N, win;
    long long res;
    for( cin>>T; k<T; k++){

        cin>>N;
        vector< string >pal(N);

        for( int i = 0 ; i < N ; i++) {
            cin>>pal[i];
            pal[i]+="#";
        }
        res = 0;
        win = 1;
        int ent;
        for(int i=0, j=0; win && i<pal[0].size()  && j<pal[1].size(); ){
            ent = 0;
            if( pal[0][i]==pal[1][j] ){
                i++;
                j++;
                ent = 1;
            } else if( i-1>=0 && pal[0][i-1]==pal[1][j] ){
                res++;
                j++;
                ent = 1;
            } else if( j-1>=0 && pal[0][i]==pal[1][j-1] ){
                res++;
                i++;
                ent = 1;
            }
//            if( i>= pal[0].size() && j<pal[1].size() ){
//                i--;
//            }
//            if( j>= pal[1].size() && i<pal[0].size() ){
//                j--;
//            }
            if( !ent )
                win = 0 ;
        }

        printf("Case #%d: ", k+1);
        if( !win ){
            printf("Fegla Won\n");
        }else{
            printf("%d\n", res);
        }
    }

return 0;
}
