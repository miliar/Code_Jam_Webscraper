#include <cstdio>
#include <cstring>

typedef long long int lli;

lli arr[123456];

bool ispal(lli num)
{
  char snum[20];
  sprintf(snum, "%lld", num);
  int n = strlen(snum);

  for(int i = 0; i < n; i++, n--)
  {
    if(snum[i] != snum[n-1]) return false;
  }

  return true;
}

int main(void)
{
  int T;
  int ct = 0;

  scanf("%d\n", &T);

  arr[ct++] = 1LL;
  arr[ct++] = 4LL;
  arr[ct++] = 9LL;

  for(int i = 1; i <= 9; i++)
  {
    lli num = 11*i;

    if(ispal(num*num)) arr[ct++] = num*num;
  }

  for(int i = 1; i <= 9; i++)
  {
    for(int j = 0; j <= 9; j++)
    {

      lli num = 101*i + 10*j;

      if(ispal(num*num)) arr[ct++] = num*num;
    }
  }

  for(int i = 10; i <= 99; i++)
  {
      lli num = i*100 + i/10 + 10*(i%10);
      if(ispal(num*num)) arr[ct++] = num*num;
  }
  
  for(int i = 10; i <= 99; i++)
  {
    for(int j = 0; j <= 9; j++)
    {
      lli num = i*1000 + 100 * j + 10*(i%10) + i/10;
      if(ispal(num*num)) arr[ct++] = num*num;
    }
  }

  for(int i = 100; i <= 999; i++)
  {
    lli num = i * 1000 + 100 * (i%10) + 10*((i/10)%10) + i/100;
    if(ispal(num*num)) arr[ct++] = num*num;
  }


  for(int cas = 1; cas <= T; cas++)
  {
    lli a, b;
    
    scanf("%lld %lld", &a, &b);
    
    int idx1, idx2;

    int ini, fim, meio;

    ini = 0;
    fim = ct;

    while(fim > ini+1)
    {
      meio = (ini+fim)/2;
      if(arr[meio] <= a)
      {
        ini = meio;
      }
      else
      {
        fim = meio;
      }
    }

    if(arr[fim] <= a) idx1 = fim;
    else idx1 = ini;

    ini = 0;
    fim = ct;

    while(fim > ini+1)
    {
      meio = (ini+fim)/2;
      if(arr[meio] < b)
      {
        ini = meio;
      }
      else
      {
        fim = meio;
      }
    }

    if(arr[ini] >= b) idx2 = ini;
    else idx2 = fim;

    if(arr[idx1] == a) idx1--;
    if(arr[idx2] == b) idx2++;

    int res = idx2 - idx1 - 1;

    printf("Case #%d: %d\n", cas, res);
  }

  return 0;
}
