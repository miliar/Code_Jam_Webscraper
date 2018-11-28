#include <stdio.h>

unsigned long long fair_squ[] = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004, 100000020000001, 0};

void run(unsigned long long a, unsigned long long b)
{
  int index_left = 0;
  int index_right = 0;

  for (int i = 0; fair_squ[i] != 0; ++i)
    if (a <= fair_squ[i])
    {
      index_left = i;
      break;
    }

  for (int i = 0; fair_squ[i] != 0; ++i)
    if (b < fair_squ[i])
    {
      index_right = i;
      break;
    }

  printf("%d\n", index_right - index_left);
}

int main()
{
  int num_case;

  scanf("%d", &num_case);

  for (int i = 1; i <= num_case; ++i)
  {
    unsigned long long a, b;

    scanf("%llu %llu", &a, &b);

    printf("Case #%d: ", i);
    run(a, b);
  }

  return 0;
}
