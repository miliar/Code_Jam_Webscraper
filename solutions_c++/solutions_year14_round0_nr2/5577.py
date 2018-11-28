#include <cstdio>

using namespace std;

int main()
{
  int t;
  int cas = 1;
  scanf("%d", &t);
  while(t--)
  {
    double c, f, x;
    scanf("%lf %lf %lf", &c, &f, &x);
    double currate = 2.0;
    double newrate = 2.0;
    double timespent = 0.0;
    printf("Case #%d: ", cas++);
    if(x <= c)
    {
      printf("%.7lf\n", x / 2);  
      continue;
    }
    double balance = x-c;
    while(true)
    {
      timespent += c / currate;
      newrate = currate + f;
      if(balance/currate >  x/newrate)
        currate = newrate;
      else 
      {
        timespent += balance / currate;
        break;
      }
    }
    printf("%.7lf\n", timespent);
  }
  return 0;
}
