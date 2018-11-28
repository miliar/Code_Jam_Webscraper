#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
using namespace std;
#define N 5
char s[N][N] , c;
int ca;

bool P(char x)
{
  if (x == c || x == 'T')
    return 1;
  return 0;
}

void work()
{
  int i , j;
  bool f1 = 0 , f2 = 0 , ove = 1;
  for (i = 1 ; i <= 4 ; ++ i)
    scanf("%s" , s[i] + 1);

  for (i = 1 ; i <= 4 ; ++ i)
    for (j = 1 ; j <= 4 ; ++ j)
      if (s[i][j] == '.')
        ove = 0;
  c = 'O';
  f1 |= (P(s[1][1]) && P(s[2][2]) && P(s[3][3]) && P(s[4][4]));
  f1 |= (P(s[1][4]) && P(s[2][3]) && P(s[3][2]) && P(s[4][1]));
  for (i = 1 ; i <= 4 ; ++ i)
    f1 |= (P(s[1][i]) && P(s[2][i]) && P(s[3][i]) && P(s[4][i])) ,
    f1 |= (P(s[i][4]) && P(s[i][3]) && P(s[i][2]) && P(s[i][1])) ;

  c = 'X';
  f2 |= (P(s[1][1]) && P(s[2][2]) && P(s[3][3]) && P(s[4][4]));
  f2 |= (P(s[1][4]) && P(s[2][3]) && P(s[3][2]) && P(s[4][1]));
  for (i = 1 ; i <= 4 ; ++ i)
    f2 |= (P(s[1][i]) && P(s[2][i]) && P(s[3][i]) && P(s[4][i])) ,
    f2 |= (P(s[i][4]) && P(s[i][3]) && P(s[i][2]) && P(s[i][1])) ;
  printf("Case #%d: " , ++ ca);
  if (f1)
    puts("O won");
  else if (f2)
    puts("X won");
  else if (ove)
    puts("Draw");
  else puts("Game has not completed");
}

int main()
{
  freopen("~input.txt" , "r", stdin);
  freopen("~output.txt" , "w", stdout);
  int _;cin>>_;while(_--)
    work();
  return 0;
}
