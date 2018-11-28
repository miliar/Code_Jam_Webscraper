#include <stdio.h>
#include <algorithm>
#include <string.h>
using namespace std;
#define MIN(a, b) (((a)<(b))?(a):(b))
#define UP (1<<0)
#define RIGHT (1<<1)
#define DOWN (1<<2)
#define LEFT (1<<3)
int dRow[] = {-1, 0, 1, 0};
int dCol[] = {0, 1, 0, -1};
int dirs[] = {UP, RIGHT, DOWN, LEFT};
int A[101][101];
int invalid[101][101];
int R, C;
char buffer[102];

int get_arrow(char c){
    switch(c){
        case '^':
            return UP;
        case '>':
            return RIGHT;
        case 'v':
            return DOWN;
        case '<':
            return LEFT;
    }
    return 0;
}

int solve(){
    memset(invalid, 0, sizeof(invalid));
    for(int i=0;i<R;++i){
        int first=-1;
        int last=-1;
        for(int j=0;j<C;++j){
            if(A[i][j]!=0){
                if(first==-1){
                    first = j;
                }
                last = j;
            }
        }
        if(first != -1){
            invalid[i][first] |= LEFT;
        }
        if(last != -1){
            invalid[i][last] |= RIGHT;
        }
    }
    
    for(int j=0;j<C;++j){
        int first=-1;
        int last=-1;
        for(int i=0;i<R;++i){
            if(A[i][j]!=0){
                if(first==-1){
                    first = i;
                }
                last = i;
            }
        }
        if(first != -1){
            invalid[first][j] |= UP;
        }
        if(last != -1){
            invalid[last][j] |= DOWN;
        }
    }
    
    int sol=0;
    const int ALL = UP|RIGHT|DOWN|LEFT;
    for(int i=0;i<R; ++i){
        for(int j=0;j<C;++j){
            if(invalid[i][j]==ALL){
                return -1;
            }
            if(invalid[i][j]&A[i][j]){
                ++sol;
            }
        }
    }
    return sol;
}

int main(){
    int T;
    scanf("%d", &T);
    for(int c=1;c<=T;++c){
        scanf("%d%d", &R, &C);
        for(int i=0;i<R;++i){
            scanf("%s", buffer);
            for(int j=0;j<C;++j){
                A[i][j] = get_arrow(buffer[j]);
            }
        }
        int sol = solve();
        if(sol == -1){
            printf("Case #%d: IMPOSSIBLE\n", c);
        }else{
            printf("Case #%d: %d\n", c, sol);
        }
        
    }
    return 0;
}
