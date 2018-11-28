/*
 * COMP: CODE JAM 2014
 * PROG: B.Cookie Clicker Alpha
 * LANG: C++
 * AUTH: paelletadecaragols
 */

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
  int T;
  scanf("%d", &T);

  for(int i = 0; i < T; i++)
  {
    long double C, F, X;
    scanf("%Lf %Lf %Lf", &C, &F, &X);

    long double prod = 2.0, sec = 0.0;
    while(X/prod > C/prod + X/(prod+F))
    {
      sec += C/prod;
      prod += F;
    }
    printf("Case #%d: %.7Lf\n", i+1, sec+(X/prod));
  }
}
