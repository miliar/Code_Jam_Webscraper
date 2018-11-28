#include <cstdio>

int board[5][5];
int R, C, M;
int placingMines;
int found;

bool seen[5][5];

bool isMine(int r, int c) {
    if (r < 0 || r >= R)
        return 0;
    if (c < 0 || c >= C)
        return 0;
    if (placingMines && !board[r][c])
        return 0;
    if (!placingMines && board[r][c])
        return 0;
    return 1;
}

bool isZero(int r, int c) {
    int dx[] = {-1, -1, -1, 0, 1, 1, 1, 0};
    int dy[] = {-1, 0, 1, 1, 1, 0, -1, -1};
    
    if (isMine(r, c))
        return 0;
    
    int i;
    for (i = 0; i < 8; i++)
        if (isMine(r+dx[i], c+dy[i]))
            return 0;
    return 1;
}

void floodfill(int r, int c) {
    if (r < 0 || r >= R)
        return;
    if (c < 0 || c >= C)
        return;
    
    if (seen[r][c])
        return;
    if (isMine(r, c))
        return;
    seen[r][c] = 1;
    
    if (!isZero(r, c))
        return;
    
    int dx[] = {-1, -1, -1, 0, 1, 1, 1, 0};
    int dy[] = {-1, 0, 1, 1, 1, 0, -1, -1};
    int i;
    for (i = 0; i< 8; i++)
        floodfill(r+dx[i], c+dy[i]);
}

bool works() {
    //find a zero
    
    int i, j, k, l;
    for (i = 0; i < R; i++) {
        for (j = 0; j < C; j++) {
            if (isZero(i, j))
                break;
        }
        if (j != C)
            break;
    }
    if (i == R)
        return 0;
    
    for (k = 0; k < R; k++)
        for (l = 0; l < C; l++)
            seen[k][l] = 0;
    
    floodfill(i, j);
    
    for (i = 0; i < R; i++)
        for (j = 0; j < C; j++)
            if (!isMine(i, j) && !seen[i][j])
                return 0;
    return 1;
    
}

void place(int where, int toPlace) {
    if (found)
        return;

    if (toPlace == 0) {
        if (works())
            found = 1;
        return;
    }
    if (R*C-where < toPlace)
        return;
    board[where/C][where%C] = 1;
    place(where+1, toPlace-1);
    if (found)
        return;
    board[where/C][where%C] = 0;
    place(where+1, toPlace);
}

int main() {
    int T, TT;
    scanf("%d", &TT);
    
    for (T = 1; T <= TT; T++) {
        printf("Case #%d: \n", T);
        fprintf(stderr, "Case #%d: ", T);
        
        scanf("%d%d%d", &R, &C, &M);
        
        int i, j;
        for (i = 0; i< R; i++)
            for (j = 0; j < C; j++)
                board[i][j] = 0;
        
        //are there empty spaces
        if (M == R * C) {
            printf("Impossible\n");
            continue;
        }
        
        //one empty space
        if (M == R * C - 1) {
            for (i = 0; i < R; i++) {
                for (j = 0; j < C; j++) {
                    if (i == 0 && j == 0)
                        printf("c");
                    else
                        printf("*");
                }
                printf("\n");
            }
            continue;
        }    
            
        found = 0;    
            
        if (M <= 12) {
            placingMines = 1;
            place(0, M);
        } else {
            placingMines = 0;
            place(0, R*C-M);
        }
        
        if (found == 1) {
            int cd = 0;
            for (i = 0; i < R; i++) {
                for (j = 0; j < C; j++) {
                    if (isMine(i, j)) {
                        printf("*");
                    } else if (isZero(i, j) && !cd) {
                        printf("c");
                        cd = 1;
                    } else {
                        printf(".");
                    }
                }
                printf("\n");
            }
        } else {
            printf("Impossible\n");
        }
        
            
    }
}