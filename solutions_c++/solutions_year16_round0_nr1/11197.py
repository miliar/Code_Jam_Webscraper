#include<stdio.h>

void print_arr(int* arr, int n)
{
  for (int i = 0; i < n; i++)
    printf("%d ", *(arr + i));
  printf("\n");
}

bool all_digits(int* arr)
{
  for (int i = 0; i < 10; i++)
    if (*(arr+i) == 0)
      return false;
  return true;
}

void count_digit(long long n, int* arr)
{
  while(n > 0)
  {
    int i = n % 10;
    *(arr+i) = *(arr+i) + 1;
    n /= 10;
  }
}

long long solve(long long n)
{
  int m = n;
  int digit_count[10];
  for (int i = 0; i < 10; i++)
    digit_count[i] = 0;
  count_digit(m, digit_count);
  while(!all_digits(digit_count))
  {
    m += n;
    count_digit(m, digit_count);
  }
  return m;
}

int main() {
  long long n;
  int t;
  scanf("%d", &t);
  for (int i = 0; i < t; i++)
  {
    printf("Case #%d: ", i+1);
    scanf("%lld", &n);
    if (n == 0)
      printf("INSOMNIA\n");
    else
      printf("%lld\n", solve(n));
  }
}
