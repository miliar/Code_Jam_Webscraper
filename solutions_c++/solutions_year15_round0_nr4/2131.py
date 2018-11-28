#include <iostream>

int main()
{
  int T;
  std::cin >> T;
  
  for (int t=1; t <= T; t++)
  {
    const char *result = "RICHARD";
    int X, R, C;
    std::cin >> X >> R >> C;
    if (R > C)
    {
      int t = R; R = C; C = t;
    }
    
    if ((R*C)%X == 0)
    {
      result = "GABRIEL";
      if (R < (X+1)/2 || (X == 4 && R <= 2) || (X == 6 && R <= 3) || (X >= 7))
        result = "RICHARD";
    }
    std::cout << "Case #" << t << ": " << result << std::endl;
  }
  return 0;
}
