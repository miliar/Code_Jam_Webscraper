#include <iostream>
#include <cstdio>
#include <vector>

typedef long double real;

real C;
real F;
real X;

void farm_time()
{
  real prev = 0;
  real prev_rate = 0;
  real curr = 0;
  real curr_rate = 2;
  while (true)
  {
    prev = curr;
    prev_rate = curr_rate;

    curr += C / curr_rate;
    curr_rate += F;

    if ((prev + X / prev_rate) <= (curr + X / curr_rate))
    {
      printf("%.10Lf\n", prev + X / prev_rate);
      return;
    }
  }
}

int main()
{
  // Exponential(0, 2, 4, 8, 16, ...)/binary search does not seem to be neccessary due to the time constraints.
  int T = 0;
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t)
  {
    scanf("%Lf %Lf %Lf", &C, &F, &X);
    printf("Case #%d: ", t); farm_time();
  }
  
  /*
  X = 100000;
  std::vector<real> out;
  for (C = 1; C <= 10000; ++C)
  {
    for (F = 1; F <= 100; ++F)
    {
      printf("C = %Lf; F = %Lf; ", C, F);
      farm_time();
    }
  } 
  */
}

