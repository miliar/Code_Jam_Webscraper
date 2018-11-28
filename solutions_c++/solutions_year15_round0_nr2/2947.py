#include<iostream>
#include<stdio.h>
#include<algorithm>
#define SIZE 1000
using namespace std;
int Count[SIZE+1];
int main()
{
  freopen("B-large.in", "r", stdin);
  freopen("pb.txt", "w", stdout);
  int T,cases,D,i,j,n,sum,answer,Max;
  cin>>T;
  for(cases=1;cases<=T;cases++)
  {
    cin>>D;
    Max=0;
    for(i=0;i<D;i++)
    {
      cin>>Count[i];
      if(Count[i]>Max)
        Max=Count[i];
    }
    answer=10000;
    for(i=1;i<=Max;i++)
    {
      sum=0;
      for(j=0;j<D;j++)
      {
        sum+=Count[j]/i;
        if(Count[j]%i==0)
          sum--;
      }
      if(answer>sum+i)
        answer=sum+i;
    }
    printf("Case #%d: %d\n", cases, answer);
  }
  return 0;
}