#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
#include <string>
#include <set>
#include <map>
using namespace std;
int b[55][55];
int dy[]={-1,-1,-1,0,1,1,1,0};
int dx[]={-1,0,1,1,1,0,-1,-1};
int R,C,M;
void go(int y,int x) {
    int cnt=0;
    for ( int i = 0 ; i < 8 ; i++ ) {
        int ny = y+dy[i],nx = x+dx[i];
        if ( ny < 0 || nx < 0 || ny >= R || nx >= C ) continue;
        cnt += (b[ny][nx]==1);
    }
    if ( cnt == 0 ) {
        for ( int i = 0 ; i < 8 ; i++ ) {
            int ny = y+dy[i],nx = x+dx[i];
            if ( ny < 0 || nx < 0 || ny >= R || nx >= C ) continue;
            if ( b[ny][nx] == 0 ) {
                b[ny][nx] = 2;   
                go(ny,nx);
            }
        }
    }
}
int main() {
    int tc;
    scanf("%d",&tc);
    for ( int _case = 1 ; _case <= tc ; _case ++ ) {
        printf("Case #%d:\n",_case);
        scanf("%d%d%d",&R,&C,&M);
        int a[51*51]={};
        for ( int i = 0 ; i < M ; i++ ) 
            a[R*C-i-1] = 1;
        a[0] = -1;
        do{
            int py,px;
            for ( int i = 0 ; i < R ; i++ ) 
                for ( int j = 0 ; j < C ; j++ ) {
                    b[i][j] = a[i*C+j];
                    if ( b[i][j] == -1 ) 
                        py = i,px = j;
                }
            go(py,px);
            bool ok = true;
            for ( int i = 0 ; i < R ; i++ ) 
                for ( int j = 0 ; j < C ; j++ ) 
                    if ( b[i][j] == 0 ) ok = false;
            if ( ok ) {
                for ( int i = 0 ; i < R ; i++ ) {
                    for ( int j = 0 ; j < C ; j++ ) 
                        printf("%c",a[i*C+j]==0?'.':a[i*C+j]==1?'*':'C');
                    puts("");
                }
                goto YES;
            }
        }while(next_permutation(a,a+R*C));
        printf("Impossible\n");
YES:;
    }
    return 0;
}
