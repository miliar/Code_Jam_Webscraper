#include <algorithm>
#include <cmath>
#include <cstring>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <cstdlib>
#include <set>
#define DEBUG printf("TEST\n")

using namespace std;

int itc, tc, farm;
double C, F, X, output, a, b, t;

int main()
{
     
     scanf("%d", &tc);
     for(itc = 1; itc <= tc; ++itc)
     {
          scanf("%lf %lf %lf", &C, &F, &X);
          
          printf("Case #%d: ", itc);
          
          output = X / 2;
          
          t = .0;
          for(farm = 1; farm <= 1000000; ++farm)
          {
               t += C / ((farm - 1) * F + 2);
               
               output = min(output, t + X / (farm * F + 2));
          }
          printf("%.9lf\n", output);
     }
     
     return 0;
}
