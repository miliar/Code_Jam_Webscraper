#include <iostream>
#include <cstdio>

using namespace std;

double getTime(double amount_to_earn, double cookie_income_per_sec, size_t farm_count)
{
  return amount_to_earn / (2 + (farm_count * cookie_income_per_sec));
}

double getMinimalGameLength(double cookie_farm_price, double cookie_income_per_sec, double cookie_to_win)
{
  double result = 0.0;
  size_t farm_count = 0;
  while (getTime(cookie_farm_price, cookie_income_per_sec, farm_count) < (getTime(cookie_to_win, cookie_income_per_sec, farm_count) - getTime(cookie_to_win, cookie_income_per_sec, farm_count+1)))
  {
    result += getTime(cookie_farm_price, cookie_income_per_sec, farm_count);
    ++farm_count;
  }
  result += getTime(cookie_to_win, cookie_income_per_sec, farm_count);
  return result;
}

int main(int argc, char** argv)
{
  size_t number_of_testcases;
  cin >> number_of_testcases;
  for (size_t tc_number = 1; tc_number <= number_of_testcases; ++tc_number)
  {
    double C, F, X;
    cin >> C >> F >> X;
    printf("Case #%u: %.7f\n", tc_number, getMinimalGameLength(C, F, X));
  }
} 
