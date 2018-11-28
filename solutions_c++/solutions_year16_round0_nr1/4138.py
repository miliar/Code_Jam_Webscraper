#include<iostream>
#include<cstring>
#include<stdio.h>
#define SIZE 1000000
using namespace std;
long long int dp[SIZE+1];
int main()
{
  freopen("A-large.in","r",stdin);
  freopen("a.txt","w",stdout);
  int cases,t,index;
  long long int input,i,j;
  bool used[10];
  for(i=1;i<=SIZE;i++)
  {
    memset(used,0,sizeof(used));
    for(j=i;;j+=i)
    {
      long long int tmp=j;
      while(tmp>0)
      {
        used[tmp%10]=true;
        tmp/=10;
      }
      for(index=0;index<10;index++)
        if(!used[index])
          break;
      if(index==10)
      {
        dp[i]=j;
        break;
      }
    }
  }
  cin>>t;
  for(cases=1;cases<=t;cases++)
  {
    cin>>input;
    printf("Case #%d: ", cases);
    if(input==0)
      cout<<"INSOMNIA"<<endl;
    else
      cout<<dp[input]<<endl;
  }
}