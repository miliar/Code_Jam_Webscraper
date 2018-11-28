#include<iostream>
#include<stdio.h>
#define SIZE 1000
using namespace std;
char input[SIZE+10];
int main()
{
  freopen("A-large.in", "r", stdin);
  freopen("pa.txt", "w", stdout);
  int i,cases,T,n,sum,answer;
  cin>>T;
  for(cases=1;cases<=T;cases++)
  {
    cin>>n>>input;
    sum=0;
    answer=0;
    for(i=0;i<=n;i++)
    {
      if(sum<i)
      {
        answer+=(i-sum);
        sum=i;
      }
      sum+=input[i]-'0';
    }
    printf("Case #%d: %d\n", cases, answer);
  }
  return 0;
}