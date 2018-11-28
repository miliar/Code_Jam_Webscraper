#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int smax;
char str[1009];

void ReadData()
{
  scanf("%d ", &smax);
  scanf("%s%*c", str);
}

int answer;

void Solve()
{
  answer = 0;
  int cnt = 0;
  for(int i = 0; i <= smax; i++)
  {
    if(str[i] != '0' && cnt < i)
    {
      int delta = i - cnt;
      answer += delta;
      cnt += delta;
    }
    cnt += str[i] - '0';
  }
}

void WriteData()
{
  printf("%d\n", answer);
}

int main()
{
  int QWE = 1;
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  scanf("%d", &QWE);
  for(int i = 0; i < QWE; i++)
  {
    ReadData();
    Solve();
    printf("Case #%d: ", i + 1);
    WriteData();
  }
  return 0;
}