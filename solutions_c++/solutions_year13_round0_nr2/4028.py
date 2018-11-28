#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
 
#include <conio.h>

using namespace std;
 
int N, M;
bool ok;
int lawn[110][110];
 
 
bool check (int pattern, int x, int y)
{
        int checkCol = 0, checkRow = 0;
        for(int col = 0 ; col < M ; col++)
        {
                if(lawn[x][col] <= pattern) checkCol++;
                else break;
        }
 
        for(int row = 0 ; row < N ; row++)
        {
                if(lawn[row][y] <= pattern) checkRow++;
                else break;
        }
 
        if(checkCol == M || checkRow == N) return true;
        else return false;
 
}
 
int main()
{
        int test, count = 1;
        scanf("%d", &test);
		FILE *fp = fopen("out.txt", "w");
        while(test--)
        {
                scanf("%d%d", &N, &M);
 
                for(int i = 0 ; i < N ; i++)
                {
                        for(int j = 0 ; j < M ; j++)
                        {
                                scanf("%d", &lawn[i][j]);
                        }
                }
 
                ok = true;
 
                for(int i = 0 ; i < N ; i++)
                {
                        for(int j = 0 ; j < M ; j++)
                        {
                                int pattern = lawn[i][j];
                                ok = check(pattern, i, j);
                                if(!ok) break;
                        }
                        if(!ok) break;
                }
 
                fprintf(fp,"Case #%d: ", count++);
                if(ok) fprintf(fp,"YES \n");
                else fprintf(fp,"NO \n");
        }
		fclose(fp);
        return 0;
}