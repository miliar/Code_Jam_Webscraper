#include <cstdio>
using namespace std;

bool isok(int X, int R, int C)
{

  if(R * C % X != 0)
    return false;
  if(X == 1 || X == 2)
    return true;
  if(X == 3)
  {
    if(R * C % 6 == 0)
      return true;
    if(R == 3 && C == 3)
      return true;
    return false;
  }
  if(R == 3 && C == 4)
    return true;
  if(R == 4 && C == 3)
    return true;
  if(R == 4 && C == 4)
    return true;
  return false;
}

int main()
{
  int T = 0;
  scanf("%d", &T);
  for(int Case = 1; Case <= T; ++Case)
  {
    int X = 0, R = 0, C = 0;
    scanf("%d%d%d", &X, &R, &C);
    if(isok(X, R, C))
      printf("Case #%d: GABRIEL\n", Case);
    else
      printf("Case #%d: RICHARD\n", Case);
  }
  return 0;
}
