#include <algorithm>
#include <stdio.h>

using namespace std;

FILE* fin;
FILE* fout;
int R;
int C;

int m[8][8];
int ct[8][8];
bool got[32];
bool visited[8][8];
int minX;

void print(int mines) {
    printf("    else if (R==%d && C==%d && M==%d) {\n", R, C, mines);
    bool printedC = false;
    for (int r=0; r<R; r++) {
        printf("        fprintf(fout, \"");
        for (int c=0; c<C; c++) {
            if (m[r][c])
                printf("*");
            else if (!printedC && ct[r][c] == minX) {
                printf("c");
                printedC = true;
            } else
                printf(".");
        }
        printf("\\n\");\n");
    }
    printf("    }\n");
}

int dfs(int r, int c)
{
    int ret = 1;
    visited[r][c] = true;
    if (ct[r][c] == 0) {
        for (int dr=-1; dr<=1; dr++) {
            for (int dc=-1; dc<=1; dc++) {
                int rr = r+dr;
                int cc = c+dc;
                if (rr>=0 && rr<R && cc>=0 && cc<C && !m[rr][cc] && !visited[rr][cc]) {
                    ret += dfs(rr, cc);
                }
            }
        }
    }
    return ret;
}

bool check() {
    for (int r=0; r<R; r++) {
        for (int c=0; c<C; c++) {
            if (m[r][c]) {
                ct[r][c] = -1;
                continue;
            }
            ct[r][c] = 0;
            for (int dr=-1; dr<=1; dr++) {
                for (int dc=-1; dc<=1; dc++) {
                    if (dr==0 && dc==0) continue;
                    int rr = r+dr;
                    int cc = c+dc;
                    if (rr>=0 && rr<R && cc>=0 && cc<C)
                        ct[r][c] += m[rr][cc];
                }
            }
        }
    }
    int numdots = 0;
    minX = 10;
    int minR = -1;
    int minC = -1;
    for (int r=0; r<R; r++) {
        for (int c=0; c<C; c++) {
            if (m[r][c]==0) {
                numdots++;
                if (ct[r][c] < minX) {
                    minX = ct[r][c];
                    minR = r;
                    minC = c;
                }
            }
        }
    }
    if (numdots==0) return true;
    for (int r=0; r<R; r++)
        for (int c=0; c<C; c++)
            visited[r][c] = false;
    return dfs(minR, minC) == numdots;
}
void rec(int k, int mines)
{
    if (k==R*C) {
        if (!got[mines] && check()) {
            print(mines);
            got[mines] = true;
        }
    } else {
        m[k/C][k%C] = 0;
        rec(k+1, mines);
        m[k/C][k%C] = 1;
        rec(k+1, mines+1);
    }
}

int magic(int R, int C, int M)
{
    if (R==1 && C==1 && M==0) {
        fprintf(fout, "c\n");
    }
    else if (R==1 && C==1 && M==1) {
        fprintf(fout, "*\n");
    }
    else if (R==1 && C==2 && M==0) {
        fprintf(fout, "c.\n");
    }
    else if (R==1 && C==2 && M==1) {
        fprintf(fout, "c*\n");
    }
    else if (R==1 && C==2 && M==2) {
        fprintf(fout, "**\n");
    }
    else if (R==1 && C==3 && M==0) {
        fprintf(fout, "c..\n");
    }
    else if (R==1 && C==3 && M==1) {
        fprintf(fout, "c.*\n");
    }
    else if (R==1 && C==3 && M==2) {
        fprintf(fout, "c**\n");
    }
    else if (R==1 && C==3 && M==3) {
        fprintf(fout, "***\n");
    }
    else if (R==1 && C==4 && M==0) {
        fprintf(fout, "c...\n");
    }
    else if (R==1 && C==4 && M==1) {
        fprintf(fout, "c..*\n");
    }
    else if (R==1 && C==4 && M==2) {
        fprintf(fout, "c.**\n");
    }
    else if (R==1 && C==4 && M==3) {
        fprintf(fout, "c***\n");
    }
    else if (R==1 && C==4 && M==4) {
        fprintf(fout, "****\n");
    }
    else if (R==1 && C==5 && M==0) {
        fprintf(fout, "c....\n");
    }
    else if (R==1 && C==5 && M==1) {
        fprintf(fout, "c...*\n");
    }
    else if (R==1 && C==5 && M==2) {
        fprintf(fout, "c..**\n");
    }
    else if (R==1 && C==5 && M==3) {
        fprintf(fout, "c.***\n");
    }
    else if (R==1 && C==5 && M==4) {
        fprintf(fout, "c****\n");
    }
    else if (R==1 && C==5 && M==5) {
        fprintf(fout, "*****\n");
    }
    else if (R==2 && C==1 && M==0) {
        fprintf(fout, "c\n");
        fprintf(fout, ".\n");
    }
    else if (R==2 && C==1 && M==1) {
        fprintf(fout, "c\n");
        fprintf(fout, "*\n");
    }
    else if (R==2 && C==1 && M==2) {
        fprintf(fout, "*\n");
        fprintf(fout, "*\n");
    }
    else if (R==2 && C==2 && M==0) {
        fprintf(fout, "c.\n");
        fprintf(fout, "..\n");
    }
    else if (R==2 && C==2 && M==3) {
        fprintf(fout, "c*\n");
        fprintf(fout, "**\n");
    }
    else if (R==2 && C==2 && M==4) {
        fprintf(fout, "**\n");
        fprintf(fout, "**\n");
    }
    else if (R==2 && C==3 && M==0) {
        fprintf(fout, "c..\n");
        fprintf(fout, "...\n");
    }
    else if (R==2 && C==3 && M==2) {
        fprintf(fout, "c.*\n");
        fprintf(fout, "..*\n");
    }
    else if (R==2 && C==3 && M==5) {
        fprintf(fout, "c**\n");
        fprintf(fout, "***\n");
    }
    else if (R==2 && C==3 && M==6) {
        fprintf(fout, "***\n");
        fprintf(fout, "***\n");
    }
    else if (R==2 && C==4 && M==0) {
        fprintf(fout, "c...\n");
        fprintf(fout, "....\n");
    }
    else if (R==2 && C==4 && M==2) {
        fprintf(fout, "c..*\n");
        fprintf(fout, "...*\n");
    }
    else if (R==2 && C==4 && M==4) {
        fprintf(fout, "c.**\n");
        fprintf(fout, "..**\n");
    }
    else if (R==2 && C==4 && M==7) {
        fprintf(fout, "c***\n");
        fprintf(fout, "****\n");
    }
    else if (R==2 && C==4 && M==8) {
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
    }
    else if (R==2 && C==5 && M==0) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
    }
    else if (R==2 && C==5 && M==2) {
        fprintf(fout, "c...*\n");
        fprintf(fout, "....*\n");
    }
    else if (R==2 && C==5 && M==4) {
        fprintf(fout, "c..**\n");
        fprintf(fout, "...**\n");
    }
    else if (R==2 && C==5 && M==6) {
        fprintf(fout, "c.***\n");
        fprintf(fout, "..***\n");
    }
    else if (R==2 && C==5 && M==9) {
        fprintf(fout, "c****\n");
        fprintf(fout, "*****\n");
    }
    else if (R==2 && C==5 && M==10) {
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
    }
    else if (R==3 && C==1 && M==0) {
        fprintf(fout, "c\n");
        fprintf(fout, ".\n");
        fprintf(fout, ".\n");
    }
    else if (R==3 && C==1 && M==1) {
        fprintf(fout, "c\n");
        fprintf(fout, ".\n");
        fprintf(fout, "*\n");
    }
    else if (R==3 && C==1 && M==2) {
        fprintf(fout, "c\n");
        fprintf(fout, "*\n");
        fprintf(fout, "*\n");
    }
    else if (R==3 && C==1 && M==3) {
        fprintf(fout, "*\n");
        fprintf(fout, "*\n");
        fprintf(fout, "*\n");
    }
    else if (R==3 && C==2 && M==0) {
        fprintf(fout, "c.\n");
        fprintf(fout, "..\n");
        fprintf(fout, "..\n");
    }
    else if (R==3 && C==2 && M==2) {
        fprintf(fout, "c.\n");
        fprintf(fout, "..\n");
        fprintf(fout, "**\n");
    }
    else if (R==3 && C==2 && M==5) {
        fprintf(fout, "c*\n");
        fprintf(fout, "**\n");
        fprintf(fout, "**\n");
    }
    else if (R==3 && C==2 && M==6) {
        fprintf(fout, "**\n");
        fprintf(fout, "**\n");
        fprintf(fout, "**\n");
    }
    else if (R==3 && C==3 && M==0) {
        fprintf(fout, "c..\n");
        fprintf(fout, "...\n");
        fprintf(fout, "...\n");
    }
    else if (R==3 && C==3 && M==1) {
        fprintf(fout, "c..\n");
        fprintf(fout, "...\n");
        fprintf(fout, "..*\n");
    }
    else if (R==3 && C==3 && M==3) {
        fprintf(fout, "c..\n");
        fprintf(fout, "...\n");
        fprintf(fout, "***\n");
    }
    else if (R==3 && C==3 && M==5) {
        fprintf(fout, "c.*\n");
        fprintf(fout, "..*\n");
        fprintf(fout, "***\n");
    }
    else if (R==3 && C==3 && M==8) {
        fprintf(fout, "c**\n");
        fprintf(fout, "***\n");
        fprintf(fout, "***\n");
    }
    else if (R==3 && C==3 && M==9) {
        fprintf(fout, "***\n");
        fprintf(fout, "***\n");
        fprintf(fout, "***\n");
    }
    else if (R==3 && C==4 && M==0) {
        fprintf(fout, "c...\n");
        fprintf(fout, "....\n");
        fprintf(fout, "....\n");
    }
    else if (R==3 && C==4 && M==1) {
        fprintf(fout, "c...\n");
        fprintf(fout, "....\n");
        fprintf(fout, "...*\n");
    }
    else if (R==3 && C==4 && M==2) {
        fprintf(fout, "c...\n");
        fprintf(fout, "....\n");
        fprintf(fout, "..**\n");
    }
    else if (R==3 && C==4 && M==4) {
        fprintf(fout, "c...\n");
        fprintf(fout, "....\n");
        fprintf(fout, "****\n");
    }
    else if (R==3 && C==4 && M==3) {
        fprintf(fout, "c..*\n");
        fprintf(fout, "...*\n");
        fprintf(fout, "...*\n");
    }
    else if (R==3 && C==4 && M==6) {
        fprintf(fout, "c..*\n");
        fprintf(fout, "...*\n");
        fprintf(fout, "****\n");
    }
    else if (R==3 && C==4 && M==8) {
        fprintf(fout, "c.**\n");
        fprintf(fout, "..**\n");
        fprintf(fout, "****\n");
    }
    else if (R==3 && C==4 && M==11) {
        fprintf(fout, "c***\n");
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
    }
    else if (R==3 && C==4 && M==12) {
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
    }
    else if (R==3 && C==5 && M==0) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, ".....\n");
    }
    else if (R==3 && C==5 && M==1) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "....*\n");
    }
    else if (R==3 && C==5 && M==2) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "...**\n");
    }
    else if (R==3 && C==5 && M==3) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "..***\n");
    }
    else if (R==3 && C==5 && M==5) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "*****\n");
    }
    else if (R==3 && C==5 && M==4) {
        fprintf(fout, "c...*\n");
        fprintf(fout, "....*\n");
        fprintf(fout, "...**\n");
    }
    else if (R==3 && C==5 && M==7) {
        fprintf(fout, "c...*\n");
        fprintf(fout, "....*\n");
        fprintf(fout, "*****\n");
    }
    else if (R==3 && C==5 && M==6) {
        fprintf(fout, "c..**\n");
        fprintf(fout, "...**\n");
        fprintf(fout, "...**\n");
    }
    else if (R==3 && C==5 && M==9) {
        fprintf(fout, "c..**\n");
        fprintf(fout, "...**\n");
        fprintf(fout, "*****\n");
    }
    else if (R==3 && C==5 && M==11) {
        fprintf(fout, "c.***\n");
        fprintf(fout, "..***\n");
        fprintf(fout, "*****\n");
    }
    else if (R==3 && C==5 && M==14) {
        fprintf(fout, "c****\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
    }
    else if (R==3 && C==5 && M==15) {
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
    }
    else if (R==4 && C==1 && M==0) {
        fprintf(fout, "c\n");
        fprintf(fout, ".\n");
        fprintf(fout, ".\n");
        fprintf(fout, ".\n");
    }
    else if (R==4 && C==1 && M==1) {
        fprintf(fout, "c\n");
        fprintf(fout, ".\n");
        fprintf(fout, ".\n");
        fprintf(fout, "*\n");
    }
    else if (R==4 && C==1 && M==2) {
        fprintf(fout, "c\n");
        fprintf(fout, ".\n");
        fprintf(fout, "*\n");
        fprintf(fout, "*\n");
    }
    else if (R==4 && C==1 && M==3) {
        fprintf(fout, "c\n");
        fprintf(fout, "*\n");
        fprintf(fout, "*\n");
        fprintf(fout, "*\n");
    }
    else if (R==4 && C==1 && M==4) {
        fprintf(fout, "*\n");
        fprintf(fout, "*\n");
        fprintf(fout, "*\n");
        fprintf(fout, "*\n");
    }
    else if (R==4 && C==2 && M==0) {
        fprintf(fout, "c.\n");
        fprintf(fout, "..\n");
        fprintf(fout, "..\n");
        fprintf(fout, "..\n");
    }
    else if (R==4 && C==2 && M==2) {
        fprintf(fout, "c.\n");
        fprintf(fout, "..\n");
        fprintf(fout, "..\n");
        fprintf(fout, "**\n");
    }
    else if (R==4 && C==2 && M==4) {
        fprintf(fout, "c.\n");
        fprintf(fout, "..\n");
        fprintf(fout, "**\n");
        fprintf(fout, "**\n");
    }
    else if (R==4 && C==2 && M==7) {
        fprintf(fout, "c*\n");
        fprintf(fout, "**\n");
        fprintf(fout, "**\n");
        fprintf(fout, "**\n");
    }
    else if (R==4 && C==2 && M==8) {
        fprintf(fout, "**\n");
        fprintf(fout, "**\n");
        fprintf(fout, "**\n");
        fprintf(fout, "**\n");
    }
    else if (R==4 && C==3 && M==0) {
        fprintf(fout, "c..\n");
        fprintf(fout, "...\n");
        fprintf(fout, "...\n");
        fprintf(fout, "...\n");
    }
    else if (R==4 && C==3 && M==1) {
        fprintf(fout, "c..\n");
        fprintf(fout, "...\n");
        fprintf(fout, "...\n");
        fprintf(fout, "..*\n");
    }
    else if (R==4 && C==3 && M==3) {
        fprintf(fout, "c..\n");
        fprintf(fout, "...\n");
        fprintf(fout, "...\n");
        fprintf(fout, "***\n");
    }
    else if (R==4 && C==3 && M==2) {
        fprintf(fout, "c..\n");
        fprintf(fout, "...\n");
        fprintf(fout, "..*\n");
        fprintf(fout, "..*\n");
    }
    else if (R==4 && C==3 && M==4) {
        fprintf(fout, "c..\n");
        fprintf(fout, "...\n");
        fprintf(fout, "..*\n");
        fprintf(fout, "***\n");
    }
    else if (R==4 && C==3 && M==6) {
        fprintf(fout, "c..\n");
        fprintf(fout, "...\n");
        fprintf(fout, "***\n");
        fprintf(fout, "***\n");
    }
    else if (R==4 && C==3 && M==8) {
        fprintf(fout, "c.*\n");
        fprintf(fout, "..*\n");
        fprintf(fout, "***\n");
        fprintf(fout, "***\n");
    }
    else if (R==4 && C==3 && M==11) {
        fprintf(fout, "c**\n");
        fprintf(fout, "***\n");
        fprintf(fout, "***\n");
        fprintf(fout, "***\n");
    }
    else if (R==4 && C==3 && M==12) {
        fprintf(fout, "***\n");
        fprintf(fout, "***\n");
        fprintf(fout, "***\n");
        fprintf(fout, "***\n");
    }
    else if (R==4 && C==4 && M==0) {
        fprintf(fout, "c...\n");
        fprintf(fout, "....\n");
        fprintf(fout, "....\n");
        fprintf(fout, "....\n");
    }
    else if (R==4 && C==4 && M==1) {
        fprintf(fout, "c...\n");
        fprintf(fout, "....\n");
        fprintf(fout, "....\n");
        fprintf(fout, "...*\n");
    }
    else if (R==4 && C==4 && M==2) {
        fprintf(fout, "c...\n");
        fprintf(fout, "....\n");
        fprintf(fout, "....\n");
        fprintf(fout, "..**\n");
    }
    else if (R==4 && C==4 && M==4) {
        fprintf(fout, "c...\n");
        fprintf(fout, "....\n");
        fprintf(fout, "....\n");
        fprintf(fout, "****\n");
    }
    else if (R==4 && C==4 && M==3) {
        fprintf(fout, "c...\n");
        fprintf(fout, "....\n");
        fprintf(fout, "...*\n");
        fprintf(fout, "..**\n");
    }
    else if (R==4 && C==4 && M==5) {
        fprintf(fout, "c...\n");
        fprintf(fout, "....\n");
        fprintf(fout, "...*\n");
        fprintf(fout, "****\n");
    }
    else if (R==4 && C==4 && M==6) {
        fprintf(fout, "c...\n");
        fprintf(fout, "....\n");
        fprintf(fout, "..**\n");
        fprintf(fout, "****\n");
    }
    else if (R==4 && C==4 && M==8) {
        fprintf(fout, "c...\n");
        fprintf(fout, "....\n");
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
    }
    else if (R==4 && C==4 && M==7) {
        fprintf(fout, "c..*\n");
        fprintf(fout, "...*\n");
        fprintf(fout, "...*\n");
        fprintf(fout, "****\n");
    }
    else if (R==4 && C==4 && M==10) {
        fprintf(fout, "c..*\n");
        fprintf(fout, "...*\n");
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
    }
    else if (R==4 && C==4 && M==12) {
        fprintf(fout, "c.**\n");
        fprintf(fout, "..**\n");
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
    }
    else if (R==4 && C==4 && M==15) {
        fprintf(fout, "c***\n");
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
    }
    else if (R==4 && C==4 && M==16) {
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
    }
    else if (R==4 && C==5 && M==0) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, ".....\n");
    }
    else if (R==4 && C==5 && M==1) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "....*\n");
    }
    else if (R==4 && C==5 && M==2) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "...**\n");
    }
    else if (R==4 && C==5 && M==3) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "..***\n");
    }
    else if (R==4 && C==5 && M==5) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "*****\n");
    }
    else if (R==4 && C==5 && M==4) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "....*\n");
        fprintf(fout, "..***\n");
    }
    else if (R==4 && C==5 && M==6) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "....*\n");
        fprintf(fout, "*****\n");
    }
    else if (R==4 && C==5 && M==7) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "...**\n");
        fprintf(fout, "*****\n");
    }
    else if (R==4 && C==5 && M==8) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "..***\n");
        fprintf(fout, "*****\n");
    }
    else if (R==4 && C==5 && M==10) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
    }
    else if (R==4 && C==5 && M==9) {
        fprintf(fout, "c...*\n");
        fprintf(fout, "....*\n");
        fprintf(fout, "...**\n");
        fprintf(fout, "*****\n");
    }
    else if (R==4 && C==5 && M==12) {
        fprintf(fout, "c...*\n");
        fprintf(fout, "....*\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
    }
    else if (R==4 && C==5 && M==11) {
        fprintf(fout, "c..**\n");
        fprintf(fout, "...**\n");
        fprintf(fout, "...**\n");
        fprintf(fout, "*****\n");
    }
    else if (R==4 && C==5 && M==14) {
        fprintf(fout, "c..**\n");
        fprintf(fout, "...**\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
    }
    else if (R==4 && C==5 && M==16) {
        fprintf(fout, "c.***\n");
        fprintf(fout, "..***\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
    }
    else if (R==4 && C==5 && M==19) {
        fprintf(fout, "c****\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
    }
    else if (R==4 && C==5 && M==20) {
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
    }
    else if (R==5 && C==1 && M==0) {
        fprintf(fout, "c\n");
        fprintf(fout, ".\n");
        fprintf(fout, ".\n");
        fprintf(fout, ".\n");
        fprintf(fout, ".\n");
    }
    else if (R==5 && C==1 && M==1) {
        fprintf(fout, "c\n");
        fprintf(fout, ".\n");
        fprintf(fout, ".\n");
        fprintf(fout, ".\n");
        fprintf(fout, "*\n");
    }
    else if (R==5 && C==1 && M==2) {
        fprintf(fout, "c\n");
        fprintf(fout, ".\n");
        fprintf(fout, ".\n");
        fprintf(fout, "*\n");
        fprintf(fout, "*\n");
    }
    else if (R==5 && C==1 && M==3) {
        fprintf(fout, "c\n");
        fprintf(fout, ".\n");
        fprintf(fout, "*\n");
        fprintf(fout, "*\n");
        fprintf(fout, "*\n");
    }
    else if (R==5 && C==1 && M==4) {
        fprintf(fout, "c\n");
        fprintf(fout, "*\n");
        fprintf(fout, "*\n");
        fprintf(fout, "*\n");
        fprintf(fout, "*\n");
    }
    else if (R==5 && C==1 && M==5) {
        fprintf(fout, "*\n");
        fprintf(fout, "*\n");
        fprintf(fout, "*\n");
        fprintf(fout, "*\n");
        fprintf(fout, "*\n");
    }
    else if (R==5 && C==2 && M==0) {
        fprintf(fout, "c.\n");
        fprintf(fout, "..\n");
        fprintf(fout, "..\n");
        fprintf(fout, "..\n");
        fprintf(fout, "..\n");
    }
    else if (R==5 && C==2 && M==2) {
        fprintf(fout, "c.\n");
        fprintf(fout, "..\n");
        fprintf(fout, "..\n");
        fprintf(fout, "..\n");
        fprintf(fout, "**\n");
    }
    else if (R==5 && C==2 && M==4) {
        fprintf(fout, "c.\n");
        fprintf(fout, "..\n");
        fprintf(fout, "..\n");
        fprintf(fout, "**\n");
        fprintf(fout, "**\n");
    }
    else if (R==5 && C==2 && M==6) {
        fprintf(fout, "c.\n");
        fprintf(fout, "..\n");
        fprintf(fout, "**\n");
        fprintf(fout, "**\n");
        fprintf(fout, "**\n");
    }
    else if (R==5 && C==2 && M==9) {
        fprintf(fout, "c*\n");
        fprintf(fout, "**\n");
        fprintf(fout, "**\n");
        fprintf(fout, "**\n");
        fprintf(fout, "**\n");
    }
    else if (R==5 && C==2 && M==10) {
        fprintf(fout, "**\n");
        fprintf(fout, "**\n");
        fprintf(fout, "**\n");
        fprintf(fout, "**\n");
        fprintf(fout, "**\n");
    }
    else if (R==5 && C==3 && M==0) {
        fprintf(fout, "c..\n");
        fprintf(fout, "...\n");
        fprintf(fout, "...\n");
        fprintf(fout, "...\n");
        fprintf(fout, "...\n");
    }
    else if (R==5 && C==3 && M==1) {
        fprintf(fout, "c..\n");
        fprintf(fout, "...\n");
        fprintf(fout, "...\n");
        fprintf(fout, "...\n");
        fprintf(fout, "..*\n");
    }
    else if (R==5 && C==3 && M==3) {
        fprintf(fout, "c..\n");
        fprintf(fout, "...\n");
        fprintf(fout, "...\n");
        fprintf(fout, "...\n");
        fprintf(fout, "***\n");
    }
    else if (R==5 && C==3 && M==2) {
        fprintf(fout, "c..\n");
        fprintf(fout, "...\n");
        fprintf(fout, "...\n");
        fprintf(fout, "..*\n");
        fprintf(fout, "..*\n");
    }
    else if (R==5 && C==3 && M==4) {
        fprintf(fout, "c..\n");
        fprintf(fout, "...\n");
        fprintf(fout, "...\n");
        fprintf(fout, "..*\n");
        fprintf(fout, "***\n");
    }
    else if (R==5 && C==3 && M==6) {
        fprintf(fout, "c..\n");
        fprintf(fout, "...\n");
        fprintf(fout, "...\n");
        fprintf(fout, "***\n");
        fprintf(fout, "***\n");
    }
    else if (R==5 && C==3 && M==5) {
        fprintf(fout, "c..\n");
        fprintf(fout, "...\n");
        fprintf(fout, "..*\n");
        fprintf(fout, "..*\n");
        fprintf(fout, "***\n");
    }
    else if (R==5 && C==3 && M==7) {
        fprintf(fout, "c..\n");
        fprintf(fout, "...\n");
        fprintf(fout, "..*\n");
        fprintf(fout, "***\n");
        fprintf(fout, "***\n");
    }
    else if (R==5 && C==3 && M==9) {
        fprintf(fout, "c..\n");
        fprintf(fout, "...\n");
        fprintf(fout, "***\n");
        fprintf(fout, "***\n");
        fprintf(fout, "***\n");
    }
    else if (R==5 && C==3 && M==11) {
        fprintf(fout, "c.*\n");
        fprintf(fout, "..*\n");
        fprintf(fout, "***\n");
        fprintf(fout, "***\n");
        fprintf(fout, "***\n");
    }
    else if (R==5 && C==3 && M==14) {
        fprintf(fout, "c**\n");
        fprintf(fout, "***\n");
        fprintf(fout, "***\n");
        fprintf(fout, "***\n");
        fprintf(fout, "***\n");
    }
    else if (R==5 && C==3 && M==15) {
        fprintf(fout, "***\n");
        fprintf(fout, "***\n");
        fprintf(fout, "***\n");
        fprintf(fout, "***\n");
        fprintf(fout, "***\n");
    }
    else if (R==5 && C==4 && M==0) {
        fprintf(fout, "c...\n");
        fprintf(fout, "....\n");
        fprintf(fout, "....\n");
        fprintf(fout, "....\n");
        fprintf(fout, "....\n");
    }
    else if (R==5 && C==4 && M==1) {
        fprintf(fout, "c...\n");
        fprintf(fout, "....\n");
        fprintf(fout, "....\n");
        fprintf(fout, "....\n");
        fprintf(fout, "...*\n");
    }
    else if (R==5 && C==4 && M==2) {
        fprintf(fout, "c...\n");
        fprintf(fout, "....\n");
        fprintf(fout, "....\n");
        fprintf(fout, "....\n");
        fprintf(fout, "..**\n");
    }
    else if (R==5 && C==4 && M==4) {
        fprintf(fout, "c...\n");
        fprintf(fout, "....\n");
        fprintf(fout, "....\n");
        fprintf(fout, "....\n");
        fprintf(fout, "****\n");
    }
    else if (R==5 && C==4 && M==3) {
        fprintf(fout, "c...\n");
        fprintf(fout, "....\n");
        fprintf(fout, "....\n");
        fprintf(fout, "...*\n");
        fprintf(fout, "..**\n");
    }
    else if (R==5 && C==4 && M==5) {
        fprintf(fout, "c...\n");
        fprintf(fout, "....\n");
        fprintf(fout, "....\n");
        fprintf(fout, "...*\n");
        fprintf(fout, "****\n");
    }
    else if (R==5 && C==4 && M==6) {
        fprintf(fout, "c...\n");
        fprintf(fout, "....\n");
        fprintf(fout, "....\n");
        fprintf(fout, "..**\n");
        fprintf(fout, "****\n");
    }
    else if (R==5 && C==4 && M==8) {
        fprintf(fout, "c...\n");
        fprintf(fout, "....\n");
        fprintf(fout, "....\n");
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
    }
    else if (R==5 && C==4 && M==7) {
        fprintf(fout, "c...\n");
        fprintf(fout, "....\n");
        fprintf(fout, "...*\n");
        fprintf(fout, "..**\n");
        fprintf(fout, "****\n");
    }
    else if (R==5 && C==4 && M==9) {
        fprintf(fout, "c...\n");
        fprintf(fout, "....\n");
        fprintf(fout, "...*\n");
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
    }
    else if (R==5 && C==4 && M==10) {
        fprintf(fout, "c...\n");
        fprintf(fout, "....\n");
        fprintf(fout, "..**\n");
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
    }
    else if (R==5 && C==4 && M==12) {
        fprintf(fout, "c...\n");
        fprintf(fout, "....\n");
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
    }
    else if (R==5 && C==4 && M==11) {
        fprintf(fout, "c..*\n");
        fprintf(fout, "...*\n");
        fprintf(fout, "...*\n");
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
    }
    else if (R==5 && C==4 && M==14) {
        fprintf(fout, "c..*\n");
        fprintf(fout, "...*\n");
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
    }
    else if (R==5 && C==4 && M==16) {
        fprintf(fout, "c.**\n");
        fprintf(fout, "..**\n");
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
    }
    else if (R==5 && C==4 && M==19) {
        fprintf(fout, "c***\n");
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
    }
    else if (R==5 && C==4 && M==20) {
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
        fprintf(fout, "****\n");
    }
    else if (R==5 && C==5 && M==0) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, ".....\n");
    }
    else if (R==5 && C==5 && M==1) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "....*\n");
    }
    else if (R==5 && C==5 && M==2) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "...**\n");
    }
    else if (R==5 && C==5 && M==3) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "..***\n");
    }
    else if (R==5 && C==5 && M==5) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "*****\n");
    }
    else if (R==5 && C==5 && M==4) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "....*\n");
        fprintf(fout, "..***\n");
    }
    else if (R==5 && C==5 && M==6) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "....*\n");
        fprintf(fout, "*****\n");
    }
    else if (R==5 && C==5 && M==7) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "...**\n");
        fprintf(fout, "*****\n");
    }
    else if (R==5 && C==5 && M==8) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "..***\n");
        fprintf(fout, "*****\n");
    }
    else if (R==5 && C==5 && M==10) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
    }
    else if (R==5 && C==5 && M==9) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "....*\n");
        fprintf(fout, "..***\n");
        fprintf(fout, "*****\n");
    }
    else if (R==5 && C==5 && M==11) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "....*\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
    }
    else if (R==5 && C==5 && M==12) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "...**\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
    }
    else if (R==5 && C==5 && M==13) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "..***\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
    }
    else if (R==5 && C==5 && M==15) {
        fprintf(fout, "c....\n");
        fprintf(fout, ".....\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
    }
    else if (R==5 && C==5 && M==14) {
        fprintf(fout, "c...*\n");
        fprintf(fout, "....*\n");
        fprintf(fout, "...**\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
    }
    else if (R==5 && C==5 && M==17) {
        fprintf(fout, "c...*\n");
        fprintf(fout, "....*\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
    }
    else if (R==5 && C==5 && M==16) {
        fprintf(fout, "c..**\n");
        fprintf(fout, "...**\n");
        fprintf(fout, "...**\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
    }
    else if (R==5 && C==5 && M==19) {
        fprintf(fout, "c..**\n");
        fprintf(fout, "...**\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
    }
    else if (R==5 && C==5 && M==21) {
        fprintf(fout, "c.***\n");
        fprintf(fout, "..***\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
    }
    else if (R==5 && C==5 && M==24) {
        fprintf(fout, "c****\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
    }
    else if (R==5 && C==5 && M==25) {
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
        fprintf(fout, "*****\n");
    } else
        fprintf(fout, "Impossible\n");
}

int mainMagic()
{
    for (R=1; R<=5; R++) {
        for (C=1; C<=5; C++) {
            for (int i=0; i<=R*C; i++) got[i] = false;
            rec(0, 0);
        }
    }
}

int main()
{
    fin = fopen("C-small-attempt0.in", "r");
    fout = fopen("c-out.txt", "w");
    int T;
    fscanf(fin, "%d", &T);
    for (int i=1; i<=T; i++) {
        int R, C, M;
        fscanf(fin, "%d %d %d", &R, &C, &M);
        fprintf(fout, "Case #%d:\n", i);
        magic(R, C, M);
    }
    return 0;
}
