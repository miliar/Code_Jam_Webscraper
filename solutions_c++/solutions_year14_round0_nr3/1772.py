#include <cstdio>
#define DEBUG printf("TEST\n")

using namespace std;

int R, C, M, i, j;
int TC, itc, it;
int mark[10][10];
bool found;

int dy[10] = {-1, -1, -1, 0, 1, 1,  1,  0};
int dx[10] = {-1,  0,  1, 1, 1, 0, -1, -1};

void pb()
{
     for(int i = 0; i < R; ++i)
     {
          for(int j = 0; j < C; ++j)
          {
               printf("%c", mark[i][j] == -1 ? '*' : '.');
          }
          printf("\n");
     }
}

bool isNotEmpty(int r, int c)
{
     for(int i = 0; i  < 8; ++i)
     {
          int y = r + dy[i];
          int x = c + dx[i];
          
          if(0 <= y && y < R && 0 <= x && x < C && mark[y][x] == -1)
          {
               return true;
          }
     }
     return false;
}

int dfs(int r, int c)
{
     mark[r][c] = it;
     
     //printf("now at (%d, %d), bool() = %s\n", r, c, isNotEmpty(r, c) ? "True" : "False");
     if(isNotEmpty(r, c))
     {
          return 1;
     }
     
     int ret = 1;
     
     for(int i = 0; i < 8; ++i)
     {
          int y = r + dy[i];
          int x = c + dx[i];
          
          if(0 <= y && y < R && 0 <= x && x < C)
          {
               //printf("now at (%d, %d), candidate (%d, %d), marked %d, iteration %d\n", r, c, y, x, mark[y][x], it);
               if(mark[y][x] != it)
               {
                    ret += dfs(y, x);
               }
          }
     }
     
     return ret;
}

void comb(int start, int end, int d)
{
     if(d > 0)
     {
          for(int i = start; !found && i < end - d + 1; ++i)
          {
               mark[i / C][i % C] = -1;
               comb(i + 1, end, d - 1);
               mark[i / C][i % C] = it;
          }
     }
     else
     {
          ++it;
          
          //printf("%d\n", it);
          for(int i = 0; i < R * C; ++i)
          {
               int r = i / C;
               int c = i % C;
               
               if(mark[r][c] != -1 && !isNotEmpty(r, c))
               {
                    //printf("---------------\n%d %d\n", r, c);
                    //pb();
                    int ret = dfs(r, c);
                    if(ret == R * C - M)
                    {
                         found = true;
                         
                         for(int ir = 0; ir < R; ++ir)
                         {
                              for(int ic = 0; ic < C; ++ic)
                              {
                                   if(mark[ir][ic] == -1) printf("*");
                                   else if(ir == r && ic == c) printf("c");
                                   else printf(".");
                              }
                              printf("\n");
                         }
                    }
                    
                    return;
               }
          }
     }
}

int main()
{
     
     //freopen("2014C_small.in", "r", stdin);
     //freopen("2014C_small.out", "w", stdout);
     
     scanf("%d", &TC);
     for(itc = 1; itc <= TC; ++itc)
     {
          scanf("%d %d %d", &R, &C, &M);
          
          found = false;
          it = 0;
          for(i = 0; i < R; ++i)
          {
               for(j = 0; j < C; ++j)
               {
                    mark[i][j] = 0;
               }
          }
          
          printf("Case #%d:\n", itc);
          
          if(R * C - M == 1)
          {
               for(i = 0; i < R; ++i)
               {
                    for(j = 0; j < C; ++j)
                    {
                         if(i == 0 && j == 0) printf("c");
                         else printf("*");
                    }
                    printf("\n");
               }
          }
          else
          {
               comb(0, R * C, M);
               if(!found)
               {
                    printf("Impossible\n");
               }
          }
     }
     
     return 0;
}
