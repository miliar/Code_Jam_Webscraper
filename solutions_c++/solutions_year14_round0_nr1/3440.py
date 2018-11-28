#include <cstdio>
#include <cstring>

using namespace std;

int main(void){
    
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    
    bool choose[17];
    int cas, c=0, first, second, answer, only;
    int first_board[5][4], second_board[5][4];
    
    scanf("%d", &cas);
    while( cas-- ){
        scanf("%d", &first);
        for(int i=1; i<=4; ++i)
        for(int j=0; j<4; ++j)
            scanf("%d", &first_board[i][j]);
        
        scanf("%d", &second);
        for(int i=1; i<=4; ++i)
        for(int j=0; j<4; ++j)
            scanf("%d", &second_board[i][j]);
        
        memset(choose, 0, sizeof(choose));
        for(int i=0; i<4; ++i)
            choose[first_board[first][i]] = true;
        only = 0;
        for(int i=0; i<4; ++i)
        if( choose[second_board[second][i]] ){
            ++only;
            answer = second_board[second][i];
        }
        
        if( only==1 )       printf("Case #%d: %d\n", ++c, answer);
        else if( only>1 )   printf("Case #%d: Bad magician!\n", ++c);
        else                printf("Case #%d: Volunteer cheated!\n", ++c);
    }
    
    return 0;
}
