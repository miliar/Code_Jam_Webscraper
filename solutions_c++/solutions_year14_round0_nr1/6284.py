#include <cstdio>
#include <cstdlib>

const int N = 5;
int board1[N][N], board2[N][N];

void input(int b[][N])
{
    scanf("%d", &b[0][0]);

    for(int i = 1; i < N; i++)
        for(int j = 1; j < N; j++)
            scanf("%d", &b[i][j]);
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;

    scanf("%d", &T);
    for(int cse = 1; cse <= T; cse++){
        input(board1);
        input(board2);
        int cnt = 0;
        int ans;
        for(int i = 1; i < N; i++)
        for(int j = 1; j < N; j++){
            if(board1[board1[0][0]][i] == board2[board2[0][0]][j]){
                cnt++;
                ans = board1[board1[0][0]][i];
            }
        }
        if(cnt == 1)
            printf("Case #%d: %d\n", cse, ans);
        else if(cnt > 1 )
            printf("Case #%d: Bad magician!\n", cse);
        else
            printf("Case #%d: Volunteer cheated!\n", cse);
    }
    return 0;
}
