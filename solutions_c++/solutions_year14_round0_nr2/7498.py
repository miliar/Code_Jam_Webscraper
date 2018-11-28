#include <iostream>
#include <vector>

#include <cctype>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <ctime>

using namespace std;

#define N 16

int main(void) {
  int cases=0;
  scanf("%d", &cases);
  int t=cases;

  double c, f, x;
  double r;
  int s;

  while (t--) {
    scanf("%lf %lf %lf", &c, &f, &x);
    //printf("%.7lf %.7lf %.7lf\n", c, f, x);

    if (x/c-2/f-1.0f<0) s=0;
    else s=(int)(x/c-2/f-1.0f)+1;

    r=0;
    for (int i=0;i<s;i++)
      r+=c/(2+i*f);
    r+=x/(2+s*f);

    printf("Case #%d: ", cases-t);
    printf("%.7lf\n", r);

  }
  return 0;
}
