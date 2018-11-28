#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>

using namespace std;
int N, M;
int gg[1000][1000],ok;

//chack step Large
bool check (int patternL, int x, int y)
{
        int checkCol = 0, checkRow = 0;
        for(int col = 0 ; col < M ; col++)
        {
                if(gg[x][col] <= patternL) checkCol++;
                else break;
        }
        for(int row = 0 ; row < N ; row++)
        {
                if(gg[row][y] <= patternL) checkRow++;
                else break;
        }
        if(checkCol == M || checkRow == N) return true;
        else return false;
}
int main()
{
        FILE * pFile;
        pFile = fopen ("bLarge.out","w");
        int casegcj, count = 0;
        scanf("%d", &casegcj);
        while(casegcj--)
        {
                scanf("%d%d", &N, &M);

                for(int i = 0 ; i < N ; i++)
                {
                        for(int j = 0 ; j < M ; j++)
                        {
                                scanf("%d", &gg[i][j]);
                        }
                }
                ok = 1;
                for(int i = 0 ; i < N ; i++)
                {
                        for(int j = 0 ; j < M ; j++)
                        {
                                int patternL = gg[i][j];
                                ok = check(patternL, i, j);
                                if(!ok) break;
                        }
                        if(!ok) break;
                }
//printf("Case #%d: ", count);
fprintf(pFile,"Case #%d: ", ++count);
                if(ok)
                {
                    //printf("YES\n");
                    fprintf(pFile,"YES\n");
                }
                else
                {
                    //printf("NO\n");
                    fprintf(pFile,"NO\n");
                }
        }
        return 0;
}
