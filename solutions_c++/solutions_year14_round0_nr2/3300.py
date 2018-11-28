#include<cstdio>
#include<iostream>

using namespace std;

int main(void)
{
  long long int t;
  long double C, F, X, rate;
  cin >> t;
  for(long long int i = 1; i <= t; i++)
  {
    cin >> C >> F >> X;

    double timeTaken = 0;
    rate = 2;
    for(rate = 2; X >= C && ((X - C) / rate > X / (rate + F)); rate += F)
    {
      timeTaken += C / rate;
    }

    timeTaken += X / rate;
    printf("Case #%lld: %.7lf\n", i, timeTaken);
  }
  return 0;
}
