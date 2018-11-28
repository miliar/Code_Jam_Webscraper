#include <cstdio>

unsigned long isPrime(unsigned long long num)
{
  unsigned long long limit = 4;
  for(unsigned long i=2; limit <= num; i++)
  {
    if (num % i == 0)
      return i;
    limit += (i + i + 1);
  }
  return 0;
}

unsigned long long find_number(unsigned num_in_base2, int base)
{
  unsigned long long result = 0;
  unsigned long long multiplier = 1;
  while(num_in_base2)
  {
    result += multiplier*(num_in_base2 & 1) ;
    multiplier *= base;
    num_in_base2 = num_in_base2>>1;
  }
  return result;
}

bool not_prime_for_all_bases(unsigned num_in_base2, unsigned long *divisors)
{
  divisors[0] = isPrime(num_in_base2);
  if(divisors[0] == 0){
    return false;
  }
  for( int i=3; i<=10; i++)
  {
    unsigned long long num_in_base_i = find_number(num_in_base2,i);
    divisors[i-2] = isPrime(num_in_base_i);
    if(divisors[i-2] == 0)
      return false;
  }
  return true;
}

void print_in_binary(unsigned num,int length)
{
  for (int i = length-1;i>=0;i--)
  {
    int x = num &(1<<i);
    if(x)
      printf("1");
    else
      printf("0");
  }
}

int main()
{
  unsigned T,N,J;
  scanf("%u%u%u",&T,&N,&J);
  unsigned seed_in_base2 = (1<<(N-1)) + 1 ;
  printf("Case #1:\n");
  unsigned  long divisors[9];
  while(J )
  {
    if(not_prime_for_all_bases(seed_in_base2,divisors))
    {
      print_in_binary(seed_in_base2,N);
      for(int i=0 ; i< 9; i++)
      {
        printf(" %lu",divisors[i]);
      }
      printf("\n");
      J--;
    }
    seed_in_base2 += 2;
  }

  return 0;
}
