#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

enum {MAXN = 10};

char map[MAXN][MAXN];

bool check_c(char c,char p)
{
  return c == p || c == 'T';
}

bool check_win(char c)
{
  for(int i = 0; i < 4; i++)
    {
      bool f = true;
      for(int j = 0; j < 4; j++)
	if (!(map[i][j] == c || map[i][j] == 'T')) f = false;
      if (f) return true;
    }

  for(int j = 0; j < 4; j++)
    {
      bool f = true;
      for(int i = 0; i < 4; i++)
	if (!(map[i][j] == c || map[i][j] == 'T')) f = false;
      if (f) return true;
    }


  if (check_c(map[0][0],c) && check_c(map[1][1],c) && check_c(map[2][2],c) && check_c(map[3][3],c))
    return true;

  if (check_c(map[0][3],c) && check_c(map[1][2],c) && check_c(map[2][1],c) && check_c(map[3][0],c))
    return true;

  return false;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
  int tnum;
  scanf("%d",&tnum);

  for(int t = 1; t <= tnum; t++)
    {
      for(int i = 0; i < 4; i++) scanf("%s",map[i]);

      int sum = 0;
      for(int i = 0; i < 4; i++)
	for(int j = 0; j < 4; j++)
	  if (map[i][j] == '.') ++sum;

      printf("Case #%d: ",t);
      if (check_win('X')) puts("X won");
      else if (check_win('O')) puts("O won");
      else if (sum > 0) puts("Game has not completed");
      else puts("Draw");
    }

  puts("");
  return 0;
}
