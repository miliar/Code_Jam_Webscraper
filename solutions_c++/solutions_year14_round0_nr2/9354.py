#include<iostream>
#include<cstdio>

long double TimeCal(long double C, long double F, long double X, long double currentTime, long double currentSpeed)
{
  long double ExecTime = X / currentSpeed;
    if (ExecTime > ((X  / (currentSpeed + F)) + (C/currentSpeed)))
    {
      currentTime += (C / currentSpeed);
      return TimeCal(C, F, X, currentTime, currentSpeed + F);
    }
      return currentTime + ExecTime;
}

int main()
{
  int testcases;
  scanf("%d", &testcases);
  for (int testcase = 1; testcase <= testcases; testcase++)
  {
    long double C, F, X;
    scanf("%Lf %Lf %Lf", &C,&F,&X);
    printf("Case #%d:", testcase);
    printf(" %.7Lf\n", TimeCal(C, F, X, 0, 2));
  }
  return 0;
}